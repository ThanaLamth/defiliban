import csv
import json
import re
import threading
import time
from pathlib import Path

import requests


BASE = "https://defiliban.io/wp-json/mcp/v1"
TOKEN = "defiliban_super_secret_2026"
LOG_PATH = Path("/home/qcweb/defiliban/hub_metadata_fix_results_2026-05-25.csv")

HUBS = [
    {
        "type": "category",
        "url": "https://defiliban.io/market/binance/",
        "slug": "binance",
        "label": "Binance",
        "description": "Latest Binance market updates, exchange developments, listings, compliance moves, and trading-related coverage from DeFiliban.",
    },
    {
        "type": "category",
        "url": "https://defiliban.io/crypto/",
        "slug": "crypto",
        "label": "Crypto",
        "description": "Daily crypto news, market shifts, token developments, regulation updates, and ecosystem analysis across Bitcoin, Ethereum, stablecoins, and Web3.",
    },
    {
        "type": "category",
        "url": "https://defiliban.io/market/business/",
        "slug": "business",
        "label": "Business",
        "description": "Crypto business news covering corporate strategy, institutional adoption, fundraising, partnerships, and major industry moves.",
    },
    {
        "type": "page",
        "url": "https://defiliban.io/blog/",
        "page_id": 88,
        "label": "Blog",
        "description": "Latest DeFi, crypto, blockchain, and market updates from DeFiliban.",
        "content": "<!-- wp:heading {\"level\":1} --><h1>Blog</h1><!-- /wp:heading --><!-- wp:paragraph --><p>Latest DeFi, crypto, blockchain, and market updates from DeFiliban.</p><!-- /wp:paragraph -->",
    },
    {
        "type": "category",
        "url": "https://defiliban.io/news/",
        "slug": "news",
        "label": "News",
        "description": "Breaking crypto news, market-moving developments, exchange updates, regulation changes, and major Web3 stories from DeFiliban.",
    },
    {
        "type": "category",
        "url": "https://defiliban.io/cmc/",
        "slug": "cmc",
        "label": "CMC",
        "description": "CoinMarketCap-related crypto coverage, token data context, market reference topics, and supporting ecosystem updates from DeFiliban.",
    },
    {
        "type": "category",
        "url": "https://defiliban.io/blockchain/",
        "slug": "blockchain",
        "label": "Blockchain",
        "description": "Blockchain news and analysis covering infrastructure, networks, enterprise adoption, security, and protocol-level developments.",
    },
    {
        "type": "category",
        "url": "https://defiliban.io/market/",
        "slug": "market",
        "label": "Market",
        "description": "Crypto market coverage including price action, macro drivers, institutional flows, sentiment shifts, and trading-focused analysis.",
    },
    {
        "type": "category",
        "url": "https://defiliban.io/crypto/bitcoin/",
        "slug": "bitcoin",
        "label": "Bitcoin",
        "description": "Bitcoin news, ETF flows, on-chain trends, treasury moves, miner developments, and BTC market analysis from DeFiliban.",
    },
    {
        "type": "category",
        "url": "https://defiliban.io/crypto/ethereum/",
        "slug": "ethereum",
        "label": "Ethereum",
        "description": "Ethereum news covering ETH price action, staking, DeFi infrastructure, layer-2 growth, whales, and network upgrades.",
    },
    {
        "type": "category",
        "url": "https://defiliban.io/crypto/tether/",
        "slug": "tether",
        "label": "Tether",
        "description": "Tether and stablecoin coverage including USDT issuance, treasury activity, regulation, reserve questions, and market impact.",
    },
    {
        "type": "category",
        "url": "https://defiliban.io/crypto/forex/",
        "slug": "forex",
        "label": "Forex",
        "description": "Forex and macro market coverage connected to crypto sentiment, liquidity conditions, rates, and cross-asset trading signals.",
    },
    {
        "type": "category",
        "url": "https://defiliban.io/news/mining/",
        "slug": "mining",
        "label": "Mining",
        "description": "Crypto mining news covering miner strategy, hash rate, energy, hardware, treasury moves, and Bitcoin mining trends.",
    },
    {
        "type": "category",
        "url": "https://defiliban.io/news/nft/",
        "slug": "nft",
        "label": "NFT",
        "description": "NFT news and analysis covering collections, marketplaces, trading activity, creator ecosystems, and Web3 culture shifts.",
    },
    {
        "type": "category",
        "url": "https://defiliban.io/news/stocks/",
        "slug": "stocks",
        "label": "Stocks",
        "description": "Stock-market coverage relevant to crypto, including listed crypto firms, institutional equity moves, and cross-market sentiment.",
    },
    {
        "type": "category",
        "url": "https://defiliban.io/market/money/",
        "slug": "money",
        "label": "Money",
        "description": "Money and macro-finance coverage tied to crypto markets, liquidity, capital flows, risk appetite, and policy signals.",
    },
    {
        "type": "category",
        "url": "https://defiliban.io/market/trading/",
        "slug": "trading",
        "label": "Trading",
        "description": "Crypto trading coverage including derivatives, leverage, exchange activity, whale positioning, volatility, and market structure.",
    },
    {
        "type": "category",
        "url": "https://defiliban.io/projects/",
        "slug": "projects",
        "label": "Projects",
        "description": "Crypto project coverage featuring launches, updates, product developments, token ecosystems, and notable Web3 builders.",
    },
]


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


def fetch_category_map() -> dict:
    response = requests.get(
        "https://defiliban.io/wp-json/wp/v2/categories?per_page=100", timeout=30
    )
    response.raise_for_status()
    categories = response.json()
    return {item["slug"]: item["id"] for item in categories}


def fetch_live_state(url: str) -> tuple[str, int]:
    html = requests.get(url, timeout=30).text
    match = re.search(r'<meta name="description" content="([^"]*)"', html)
    meta = match.group(1) if match else ""
    h1_count = len(re.findall(r"<h1[^>]*>.*?</h1>", html, re.S))
    return meta, h1_count


def main() -> None:
    category_map = fetch_category_map()
    client = MCPClient(BASE, TOKEN)
    client.start()
    client.call("mcp_ping", {}, 100)

    results = []
    message_id = 200

    for hub in HUBS:
        result = {
            "url": hub["url"],
            "type": hub["type"],
            "label": hub["label"],
            "target_description": hub["description"],
            "update_status": "",
            "live_meta_description": "",
            "live_h1_count": "",
            "note": "",
        }
        try:
            if hub["type"] == "category":
                term_id = category_map[hub["slug"]]
                result["object_id"] = term_id
                client.call(
                    "wp_update_term",
                    {
                        "term_id": term_id,
                        "taxonomy": "category",
                        "description": hub["description"],
                    },
                    message_id,
                )
                message_id += 1
            else:
                result["object_id"] = hub["page_id"]
                client.call(
                    "wp_update_post",
                    {
                        "ID": hub["page_id"],
                        "fields": {"post_content": hub["content"]},
                    },
                    message_id,
                )
                message_id += 1
                client.call(
                    "wp_update_post_meta",
                    {
                        "ID": hub["page_id"],
                        "meta": {"rank_math_description": hub["description"]},
                    },
                    message_id,
                )
                message_id += 1

            meta, h1_count = fetch_live_state(hub["url"])
            result["live_meta_description"] = meta
            result["live_h1_count"] = h1_count

            if hub["type"] == "page" and h1_count == 0:
                result["update_status"] = "partial_template_block"
                result["note"] = (
                    "Meta description updated, but posts-page template still renders no H1."
                )
            elif meta == hub["description"]:
                result["update_status"] = "done"
                result["note"] = "Live meta description matches target."
            else:
                result["update_status"] = "verify_meta_mismatch"
                result["note"] = "Live meta description did not match target."
            print(hub["url"], result["update_status"], flush=True)
        except Exception as exc:  # noqa: BLE001
            result["update_status"] = "error"
            result["note"] = f"{type(exc).__name__}: {exc}"
            print(hub["url"], "error", exc, flush=True)
        results.append(result)

    with LOG_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "url",
                "type",
                "label",
                "object_id",
                "target_description",
                "update_status",
                "live_meta_description",
                "live_h1_count",
                "note",
            ],
        )
        writer.writeheader()
        writer.writerows(results)

    summary = {}
    for row in results:
        summary[row["update_status"]] = summary.get(row["update_status"], 0) + 1
    print("summary", summary, flush=True)
    print(LOG_PATH, flush=True)


if __name__ == "__main__":
    main()
