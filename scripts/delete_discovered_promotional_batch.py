import csv
import json
import threading
import time
import urllib.parse
from pathlib import Path

import requests


BASE = "https://defiliban.io/wp-json/mcp/v1"
TOKEN = "defiliban_super_secret_2026"
INPUT_PATH = Path(
    "/home/qcweb/defiliban/discovered_not_indexed_safe_delete_143_2026-05-26.csv"
)
LOG_PATH = Path(
    "/home/qcweb/defiliban/discovered_not_indexed_safe_delete_143_results_2026-05-26.csv"
)


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


def extract_text(response: dict) -> str:
    parts = response.get("result", {}).get("content", [])
    return "\n".join(
        part.get("text", "") for part in parts if isinstance(part, dict)
    ).strip()


def map_post(url_slug: str) -> dict:
    api = f"https://defiliban.io/wp-json/wp/v2/posts?slug={urllib.parse.quote(url_slug)}"
    response = requests.get(api, timeout=30)
    response.raise_for_status()
    posts = response.json()
    if len(posts) != 1:
        return {"post_id": "", "title": "", "status": "", "lookup_status": "lookup_failed"}
    post = posts[0]
    return {
        "post_id": post["id"],
        "title": post["title"]["rendered"],
        "status": post["status"],
        "lookup_status": "ok",
    }


def load_targets() -> list[dict]:
    with INPUT_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        row["slug"] = row["url"].rstrip("/").split("/")[-1]
    return rows


def main() -> None:
    targets = load_targets()
    client = MCPClient(BASE, TOKEN)
    client.start()
    client.call("mcp_ping", {}, 100)

    results = []
    message_id = 200

    for target in targets:
        mapped = map_post(target["slug"])
        row = {**target, **mapped}
        if not mapped["post_id"]:
            row["delete_status"] = "lookup_failed"
            row["detail"] = "Could not map slug to a single post."
            results.append(row)
            print(target["slug"], "lookup_failed", flush=True)
            continue
        try:
            deleted = client.call(
                "wp_delete_post",
                {"ID": int(mapped["post_id"]), "force": False},
                message_id,
            )
            message_id += 1
            row["delete_status"] = "trashed"
            row["detail"] = extract_text(deleted)[:500]
            print(mapped["post_id"], target["slug"], "trashed", flush=True)
        except Exception as exc:  # noqa: BLE001
            row["delete_status"] = "error"
            row["detail"] = f"{type(exc).__name__}: {exc}"
            print(mapped["post_id"], target["slug"], "error", exc, flush=True)
        results.append(row)

    fieldnames = list(targets[0].keys()) + [
        "slug",
        "post_id",
        "title",
        "status",
        "lookup_status",
        "delete_status",
        "detail",
    ]
    with LOG_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    summary = {}
    for row in results:
        summary[row["delete_status"]] = summary.get(row["delete_status"], 0) + 1
    print("summary", summary, flush=True)
    print(LOG_PATH, flush=True)


if __name__ == "__main__":
    main()
