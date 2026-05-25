import csv
import json
import threading
import time
import urllib.parse
from pathlib import Path

import requests


BASE = "https://defiliban.io/wp-json/mcp/v1"
TOKEN = "defiliban_super_secret_2026"
TARGET_TERM_ID = 21
CSV_PATH = Path("/home/qcweb/defiliban/wave3_t_coinbase_sources_2026-05-25.csv")
LOG_PATH = Path("/home/qcweb/defiliban/wave3_t_coinbase_fix_results_2026-05-25.csv")


class MCPClient:
    def __init__(self, base: str, token: str) -> None:
        self.base = base.rstrip("/")
        self.token = token
        self.endpoint = None
        self.responses = {}
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)

    def start(self) -> None:
        threading.Thread(target=self._listen, daemon=True).start()
        deadline = time.time() + 15
        while time.time() < deadline:
            with self.lock:
                if self.endpoint:
                    break
            time.sleep(0.1)
        if not self.endpoint:
            raise RuntimeError("No MCP endpoint received")
        self._post(
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "initialize",
                "params": {
                    "protocolVersion": "2025-06-18",
                    "capabilities": {},
                    "clientInfo": {"name": "codex", "version": "1.0"},
                },
            }
        )
        self.wait(1)
        self._post(
            {
                "jsonrpc": "2.0",
                "method": "notifications/initialized",
                "params": {},
            }
        )

    def _listen(self) -> None:
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "text/event-stream",
        }
        with requests.get(
            f"{self.base}/sse", headers=headers, stream=True, timeout=60
        ) as response:
            event = None
            data = []
            for raw in response.iter_lines(decode_unicode=True):
                line = raw if raw is not None else ""
                if line == "":
                    if event or data:
                        self._handle({"event": event, "data": "\n".join(data)})
                    event = None
                    data = []
                    continue
                if line.startswith("event:"):
                    event = line.split(":", 1)[1].strip()
                elif line.startswith("data:"):
                    data.append(line.split(":", 1)[1].strip())

    def _handle(self, message: dict) -> None:
        if message["event"] == "endpoint":
            with self.lock:
                self.endpoint = message["data"]
                self.cond.notify_all()
            return
        if message["event"] == "message":
            data = json.loads(message["data"])
            if "id" in data:
                with self.lock:
                    self.responses[data["id"]] = data
                    self.cond.notify_all()

    def _post(self, payload: dict) -> None:
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        response = requests.post(
            self.endpoint, headers=headers, json=payload, timeout=30
        )
        response.raise_for_status()

    def wait(self, message_id: int, timeout: int = 30) -> dict:
        deadline = time.time() + timeout
        with self.lock:
            while time.time() < deadline:
                if message_id in self.responses:
                    return self.responses.pop(message_id)
                self.cond.wait(timeout=max(0.1, deadline - time.time()))
        raise TimeoutError(message_id)

    def call(self, name: str, args: dict, message_id: int) -> dict:
        self._post(
            {
                "jsonrpc": "2.0",
                "id": message_id,
                "method": "tools/call",
                "params": {"name": name, "arguments": args},
            }
        )
        return self.wait(message_id, 60)


def extract_json_text(response: dict) -> str:
    parts = response.get("result", {}).get("content", [])
    return "\n".join(
        part.get("text", "") for part in parts if isinstance(part, dict)
    ).strip()


def load_target_posts() -> list[dict]:
    urls = []
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            if row["recommended_action"].startswith("replace_with_"):
                urls.append(row["source_url"])

    mapped = []
    for url in urls:
        slug = url.rstrip("/").split("/")[-1]
        api = (
            "https://defiliban.io/wp-json/wp/v2/posts?slug="
            f"{urllib.parse.quote(slug)}"
        )
        response = requests.get(api, timeout=30)
        response.raise_for_status()
        posts = response.json()
        if len(posts) == 1:
            mapped.append(
                {
                    "source_url": url,
                    "slug": slug,
                    "post_id": posts[0]["id"],
                    "title": posts[0]["title"]["rendered"],
                }
            )
        else:
            mapped.append(
                {
                    "source_url": url,
                    "slug": slug,
                    "post_id": "",
                    "title": "",
                    "status": "lookup_failed",
                }
            )
    return mapped


def main() -> None:
    targets = load_target_posts()
    client = MCPClient(BASE, TOKEN)
    client.start()
    client.call("mcp_ping", {}, 100)

    results = []
    message_id = 200

    for item in targets:
        if not item.get("post_id"):
            results.append(
                {
                    **item,
                    "status": "lookup_failed",
                    "old_terms": "",
                    "new_terms": "",
                    "detail": "slug lookup failed",
                }
            )
            continue

        post_id = int(item["post_id"])
        try:
            current = client.call(
                "wp_get_post_terms",
                {"ID": post_id, "taxonomy": "post_tag"},
                message_id,
            )
            message_id += 1
            terms = json.loads(extract_json_text(current) or "[]")
            old_terms = "|".join(f"{t['term_id']}:{t['name']}" for t in terms)
            remaining = [
                int(term["term_id"])
                for term in terms
                if int(term["term_id"]) != TARGET_TERM_ID
            ]
            had_target = any(
                int(term["term_id"]) == TARGET_TERM_ID for term in terms
            )

            if had_target:
                update = client.call(
                    "wp_add_post_terms",
                    {
                        "ID": post_id,
                        "taxonomy": "post_tag",
                        "terms": remaining,
                        "append": False,
                    },
                    message_id,
                )
                message_id += 1
                detail = extract_json_text(update)
            else:
                touch = client.call(
                    "wp_update_post",
                    {
                        "ID": post_id,
                        "fields": {"post_title": item["title"]},
                    },
                    message_id,
                )
                message_id += 1
                detail = f"target tag not present; touched post: {extract_json_text(touch)}"

            verify = client.call(
                "wp_get_post_terms",
                {"ID": post_id, "taxonomy": "post_tag"},
                message_id,
            )
            message_id += 1
            verified_terms = json.loads(extract_json_text(verify) or "[]")
            new_terms = "|".join(
                f"{t['term_id']}:{t['name']}" for t in verified_terms
            )
            still_has_target = any(
                int(term["term_id"]) == TARGET_TERM_ID for term in verified_terms
            )
            if had_target and not still_has_target:
                status = "updated"
            elif not had_target:
                status = "not_present"
            else:
                status = "verify_failed"

            results.append(
                {
                    **item,
                    "status": status,
                    "old_terms": old_terms,
                    "new_terms": new_terms,
                    "detail": detail[:500],
                }
            )
            print(post_id, item["slug"], status, flush=True)
        except Exception as exc:  # noqa: BLE001
            try:
                client.call("mcp_ping", {}, message_id)
                message_id += 1
                ping_note = "mcp_ping_ok"
            except Exception:  # noqa: BLE001
                ping_note = "mcp_ping_failed"
            results.append(
                {
                    **item,
                    "status": "error",
                    "old_terms": "",
                    "new_terms": "",
                    "detail": f"{type(exc).__name__}: {exc}; {ping_note}",
                }
            )
            print(post_id, item["slug"], "error", exc, flush=True)

    with LOG_PATH.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = [
            "source_url",
            "slug",
            "post_id",
            "title",
            "status",
            "old_terms",
            "new_terms",
            "detail",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    summary = {}
    for row in results:
        summary[row["status"]] = summary.get(row["status"], 0) + 1
    print("summary", summary, flush=True)
    print(LOG_PATH, flush=True)


if __name__ == "__main__":
    main()
