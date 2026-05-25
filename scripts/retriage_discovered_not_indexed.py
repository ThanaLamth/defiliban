import csv
from collections import Counter
from pathlib import Path


DISCOVERED_PATH = Path(
    "/home/qcweb/defiliban/gsc/defiliban.io-Coverage-Drilldown-2026-05-18__3_/Bс║гng.csv"
)
OLD_TRIAGE_PATH = Path(
    "/home/qcweb/defiliban/discovered_not_indexed_triage_2026-05-19.csv"
)
CURRENT_SEARCH_PATH = Path(
    "/home/qcweb/defiliban crawl 2nd 24-5-2026/search_console_all.csv"
)
FULL_OUT = Path(
    "/home/qcweb/defiliban/discovered_not_indexed_retriage_2026-05-25.csv"
)
SHORTLIST_OUT = Path(
    "/home/qcweb/defiliban/discovered_not_indexed_priority_shortlist_2026-05-25.csv"
)
SUMMARY_OUT = Path(
    "/home/qcweb/defiliban/discovered_not_indexed_summary_2026-05-25.md"
)

KEEP_HUBS = {
    "https://defiliban.io/market/",
    "https://defiliban.io/crypto/",
    "https://defiliban.io/news/",
    "https://defiliban.io/blog/",
    "https://defiliban.io/market/binance/",
    "https://defiliban.io/crypto/bitcoin/",
    "https://defiliban.io/market/business/",
    "https://defiliban.io/crypto/ethereum/",
    "https://defiliban.io/cmc/",
    "https://defiliban.io/crypto/tether/",
    "https://defiliban.io/crypto/forex/",
    "https://defiliban.io/news/stocks/",
    "https://defiliban.io/news/nft/",
    "https://defiliban.io/market/trading/",
    "https://defiliban.io/market/money/",
    "https://defiliban.io/blockchain/",
    "https://defiliban.io/projects/",
}

PROMO_PATTERNS = [
    "presale",
    "to-buy",
    "price-prediction",
    "100x",
    "massive-gains",
    "best-crypto",
    "top-crypto",
    "worth-buying",
    "which-is-the-best",
    "long-term-crypto-investment",
    "built-cryptos-most-organic-community",
    "blockdag",
    "rollblock",
    "roobet",
    "ineminer",
    "trading-championship",
    "lead-trader",
    "cardholders",
    "prediction-market",
    "prediction-markets",
    "casino",
    "proof-pods",
]

LOW_VALUE_PR_PATTERNS = [
    "launches-spot",
    "launches-elite",
    "listed-on-",
    "lists-",
    "featured-on-",
    "launch",
    "announces",
    "announced",
    "introduces",
]

TECHNICAL_PATTERNS = [
    "?rb-etemplate=",
]


def read_current_search() -> dict:
    rows = {}
    with CURRENT_SEARCH_PATH.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            rows[row["Address"]] = row
    return rows


def read_old_triage() -> dict:
    rows = {}
    with OLD_TRIAGE_PATH.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            rows[row["url"]] = row
    return rows


def priority_rank(priority: str) -> int:
    order = {"high": 0, "medium": 1, "low": 2}
    return order.get(priority, 9)


def safe_int(value: str | None) -> int:
    try:
        return int(value or 0)
    except ValueError:
        return 0


def classify(url: str, old_row: dict, current_row: dict | None) -> tuple[str, str, str]:
    slug = url.split("defiliban.io/")[-1].lower()
    flags = old_row.get("flags", "")
    word_count = safe_int(old_row.get("word_count"))
    inlinks = safe_int(old_row.get("inlinks"))
    duplicate_title_count = safe_int(old_row.get("duplicate_title_count"))

    if any(pattern in url for pattern in TECHNICAL_PATTERNS):
        return (
            "fix_technical_url",
            "high",
            "Template/query URL should not be a crawlable destination.",
        )

    if current_row is None:
        return (
            "ignore_already_handled",
            "low",
            "URL is missing from the latest local crawl, likely already removed or no longer internally reachable.",
        )

    current_status = current_row["Status Code"]
    current_indexability = current_row["Indexability"]
    current_indexability_status = current_row["Indexability Status"]

    if current_status == "404":
        return (
            "ignore_already_handled",
            "low",
            "Currently 404 in the latest local crawl.",
        )

    if current_indexability_status == "noindex":
        return (
            "ignore_already_handled",
            "low",
            "Currently noindex in the latest local crawl.",
        )

    if url in KEEP_HUBS:
        return (
            "keep_and_push",
            "high",
            "Core hub/category page worth keeping indexed and strengthening.",
        )

    if any(pattern in slug for pattern in PROMO_PATTERNS):
        return (
            "delete_or_noindex",
            "high",
            "Promotional or low-trust investment-style URL; better pruned or deprioritized.",
        )

    if any(pattern in slug for pattern in LOW_VALUE_PR_PATTERNS) and (
        word_count < 900 or inlinks < 80
    ):
        return (
            "delete_or_noindex",
            "medium",
            "Launch/listing/announcement-style URL with weak crawl-quality signals.",
        )

    if "numeric_suffix" in flags or "suffix_2_3_4" in flags:
        return (
            "delete_or_noindex",
            "medium",
            "Numeric-suffix or duplicate-like URL is a weak candidate for crawl prioritization.",
        )

    if duplicate_title_count > 10 and word_count < 700:
        return (
            "deprioritize",
            "medium",
            "Weak title uniqueness and thin-ish content signals; not a priority URL to push right now.",
        )

    if word_count >= 900 and inlinks >= 60 and duplicate_title_count <= 1:
        return (
            "keep_and_push",
            "medium",
            "Editorial URL with stronger content and internal-link signals than the average discovered set.",
        )

    if word_count >= 750 and duplicate_title_count <= 1:
        return (
            "deprioritize",
            "low",
            "Legitimate editorial URL, but not strong enough to prioritize before a fresh recrawl.",
        )

    return (
        "deprioritize",
        "low",
        "Indexable URL currently discovered but not a high-priority push candidate based on local signals.",
    )


def main() -> None:
    current_search = read_current_search()
    old_triage = read_old_triage()
    rows = []

    with DISCOVERED_PATH.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            url = row["URL"]
            old_row = old_triage.get(url, {})
            current_row = current_search.get(url)
            action_bucket, priority, reason = classify(url, old_row, current_row)
            out = {
                "url": url,
                "last_crawled_gsc": row["Lần thu thập dữ liệu cuối cùng"],
                "current_status_code": current_row["Status Code"] if current_row else "MISSING",
                "current_indexability": current_row["Indexability"] if current_row else "MISSING",
                "current_indexability_status": current_row["Indexability Status"] if current_row else "",
                "inlinks_old_triage": old_row.get("inlinks", ""),
                "word_count_old_triage": old_row.get("word_count", ""),
                "duplicate_title_count_old_triage": old_row.get("duplicate_title_count", ""),
                "flags_old_triage": old_row.get("flags", ""),
                "title_old_triage": old_row.get("title", ""),
                "action_bucket": action_bucket,
                "priority": priority,
                "reason": reason,
            }
            rows.append(out)

    with FULL_OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    shortlist = [
        row
        for row in rows
        if row["action_bucket"] in {"fix_technical_url", "keep_and_push", "delete_or_noindex"}
    ]
    shortlist.sort(
        key=lambda row: (
            priority_rank(row["priority"]),
            row["action_bucket"],
            -safe_int(row["inlinks_old_triage"]),
            row["url"],
        )
    )

    with SHORTLIST_OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(shortlist)

    bucket_counts = Counter(row["action_bucket"] for row in rows)
    priority_counts = Counter(row["priority"] for row in rows)

    top_keep = [row["url"] for row in shortlist if row["action_bucket"] == "keep_and_push"][:20]
    top_delete = [
        row["url"] for row in shortlist if row["action_bucket"] == "delete_or_noindex"
    ][:20]
    top_fix = [row["url"] for row in shortlist if row["action_bucket"] == "fix_technical_url"][:10]

    SUMMARY_OUT.write_text(
        "\n".join(
            [
                "# Discovered Not Indexed Summary",
                "",
                "Date: 2026-05-25",
                "",
                f"Total URLs triaged: `{len(rows)}`",
                "",
                "## Action Buckets",
                *(f"- `{key}`: `{value}`" for key, value in sorted(bucket_counts.items())),
                "",
                "## Priority Counts",
                *(f"- `{key}`: `{value}`" for key, value in sorted(priority_counts.items())),
                "",
                "## Top Technical Fix URLs",
                *(f"- {url}" for url in top_fix),
                "",
                "## Top Keep And Push URLs",
                *(f"- {url}" for url in top_keep),
                "",
                "## Top Delete Or Noindex URLs",
                *(f"- {url}" for url in top_delete),
                "",
                "## Notes",
                "- `ignore_already_handled` means the latest local crawl already shows the URL as missing, 404, or noindex.",
                "- `keep_and_push` means the URL is either a core hub or a stronger editorial candidate worth crawl/index attention.",
                "- `delete_or_noindex` means the URL looks promotional, low-trust, duplicate-like, or weak enough to prune before asking Google to crawl more.",
                "- `deprioritize` means the URL is not urgent to push before the next recrawl and a fresh GSC export.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    print("total_rows", len(rows))
    print("bucket_counts", dict(bucket_counts))
    print("priority_counts", dict(priority_counts))
    print(FULL_OUT)
    print(SHORTLIST_OUT)
    print(SUMMARY_OUT)


if __name__ == "__main__":
    main()
