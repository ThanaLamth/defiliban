# DeFiliban Internal Link Cleanup Phase 1

Date: 2026-05-21

Skill lens:

- `qc-internal-link`

Verdict:

- `mixed`

The site-level internal-link problem is no longer the old sitewide email-protection issue. The main remaining waste is contextual links inside articles that still point to removed or outdated article URLs.

## What Matters First

Internal links are authority allocation. The highest-priority fixes are not random low-count 404s, but broken links inside still-live article pages that:

- are themselves `200` live
- are topically relevant
- can pass authority to a real replacement URL

## Current Priority Batch

Top broken target from the original crawl:

- `/cdn-cgi/l/email-protection` had `6994` inlinks

That problem was already cleaned earlier and should stay out of recurrence monitoring.

The next practical batch is four broken article targets with live source pages:

1. `/bitcoin-etf-flows-today-111m-single-day-outflow-as-7-day-drain-hits-211m/`
2. `/blackrock-withdraws-6167-btc-coinbase-outflows/`
3. `/binance-adds-new-spot-trading-pairs-on-april-6-2026/`
4. `/hyperbridge-exploit-mints-1b-bridged-dot-on-ethereum/`

## Fix Rule

- If an exact or near-exact live replacement exists, replace the link.
- If no good replacement exists, remove the hyperlink and keep the sentence as plain text.
- Do not create self-links when the source article is itself the closest replacement.

## Replacement Decisions

- Bitcoin ETF outflow target -> replace with `/bitcoin-etf-flows-today-outflow-111m/`
- Binance spot pairs target -> replace with `/binance-adds-new-spot-trading-pairs-april-6-2026/`
- Hyperbridge exploit target -> replace with `/hyperbridge-exploit-1b-bridged-dot-ethereum/`
- BlackRock Coinbase outflows target -> no exact live replacement confirmed; remove the link if the suggested contextual replacement feels weak

## Batch File

Use:

- `internal_link_cleanup_batch1_2026-05-21.csv`

This file contains source URL, broken target, anchor text, action, and replacement URL.

## After Fixing Batch 1

1. Re-crawl the 11 source URLs in the batch.
2. Confirm those four broken targets no longer receive internal inlinks.
3. Then move to the next tier of broken targets with 2-3 inlinks each.
