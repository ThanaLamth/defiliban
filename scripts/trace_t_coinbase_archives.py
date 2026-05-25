import csv
import re
from pathlib import Path

import requests


ARCHIVES = [
    "https://defiliban.io/crypto/page/147/",
    "https://defiliban.io/news/page/37/",
    "https://defiliban.io/blockchain/page/11/",
    "https://defiliban.io/blockchain/page/12/",
    "https://defiliban.io/market/page/34/",
]
TARGET = "https://defiliban.io/t/coinbase/"
OUT = Path("/home/qcweb/defiliban/wave3_t_coinbase_archive_trace_2026-05-25.csv")


CARD_RE = re.compile(
    r'<a class="p-category category-id-21" href="https://defiliban\.io/t/coinbase/"[^>]*>Coinbase</a>'
    r'.*?<a class="p-url" href="(?P<article_url>https://defiliban\.io/[^"]+/)" rel="bookmark">'
    r"(?P<title>.*?)</a>",
    re.S,
)


def clean_html_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    value = (
        value.replace("&#8217;", "'")
        .replace("&amp;", "&")
        .replace("&hellip;", "...")
        .replace("&#038;", "&")
        .replace("&quot;", '"')
    )
    return " ".join(value.split()).strip()


def main() -> None:
    rows = []
    for archive_url in ARCHIVES:
        response = requests.get(archive_url, timeout=30)
        response.raise_for_status()
        html = response.text
        matches = list(CARD_RE.finditer(html))
        if not matches:
            rows.append(
                {
                    "archive_url": archive_url,
                    "broken_target": TARGET,
                    "match_count": 0,
                    "article_url": "",
                    "article_title": "",
                    "status": "clean_now",
                    "note": "No live Coinbase archive badge found on this page at trace time.",
                }
            )
            print(archive_url, "clean_now")
            continue

        for index, match in enumerate(matches, start=1):
            rows.append(
                {
                    "archive_url": archive_url,
                    "broken_target": TARGET,
                    "match_count": len(matches),
                    "article_url": match.group("article_url"),
                    "article_title": clean_html_text(match.group("title")),
                    "status": "still_rendering_coinbase_badge",
                    "note": f"Match {index} of {len(matches)} on this archive page.",
                }
            )
        print(archive_url, f"matches={len(matches)}")

    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "archive_url",
                "broken_target",
                "match_count",
                "article_url",
                "article_title",
                "status",
                "note",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(OUT)


if __name__ == "__main__":
    main()
