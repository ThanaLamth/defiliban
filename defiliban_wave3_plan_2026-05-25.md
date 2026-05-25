# DeFiliban Wave 3 Plan

Date: 2026-05-25

Primary source:

- `/home/qcweb/defiliban crawl 2nd 24-5-2026/internal_all.csv`
- `/home/qcweb/defiliban crawl 2nd 24-5-2026/all_inlinks.csv`
- `/home/qcweb/defiliban crawl 2nd 24-5-2026/meta_description_all.csv`
- `/home/qcweb/defiliban crawl 2nd 24-5-2026/h1_all.csv`

Related output:

- `defiliban_wave3_actions_2026-05-25.csv`

## Summary

Wave 1 and wave 2 removed the large duplicate, template-menu, and archive noise.

Wave 3 should focus on:

1. residual broken / redirected internal links that still have small but real inlink counts
2. indexable hub pages that are intentionally live but still missing basic metadata

## Why Wave 3 Is Different

The site is no longer dominated by one giant template bug.

Current crawl state shows:

- the old mobile-menu problem URLs are gone from `internal_all`
- utility pages are already `noindex`
- archive-noindex rules are mostly stable

What remains is smaller and more editorial:

- `301` and `404` targets with `2-37` internal links
- indexable hubs missing meta descriptions
- one indexable hub missing an `H1`

## Wave 3 Branch A: Residual Internal Link Cleanup

From the second recrawl:

- residual `301` rows with `>=2` inlinks: `40`
- residual `404` rows with `>=2` inlinks: `46`
- total residual-link action rows written to CSV: `86`

Top remaining `301`:

- `https://defiliban.io/t/coinbase/`
  - `23` inlinks
  - redirects to `https://defiliban.io/news/coinbase/`

Top remaining `404`:

- `https://defiliban.io/cdn-cgi/l/email-protection`
  - `37` inlinks
  - source pattern is article-body obfuscated email links

Next most common residual link issues are mostly small:

- several `301` targets at `2-3` inlinks
- several `404` targets at `2-3` inlinks

Recommended sequence:

1. fix `/t/coinbase/` sources first
2. remove or replace `/cdn-cgi/l/email-protection` links in article bodies
3. then batch through the remaining `2-3` inlink rows from the CSV

## Wave 3 Branch B: Hub Metadata Cleanup

From the second recrawl:

- indexable URLs missing meta descriptions: `18`
- indexable URLs missing `H1`: `1`

The missing meta descriptions are mostly section / hub pages, for example:

- `/market/binance/`
- `/crypto/`
- `/market/business/`
- `/blog/`
- `/news/`
- `/cmc/`
- `/blockchain/`
- `/market/`
- `/crypto/bitcoin/`
- `/crypto/ethereum/`
- `/crypto/tether/`
- `/crypto/forex/`
- `/news/mining/`
- `/news/nft/`
- `/news/stocks/`
- `/market/money/`
- `/market/trading/`
- `/projects/`

The missing `H1` case is:

- `/blog/`

Recommended action:

1. write unique meta descriptions for the `18` indexable hubs
2. add a real visible `H1` to `/blog/`
3. while editing those hubs, confirm each one truly deserves to stay indexed

## What Not To Prioritize In Wave 3

The crawl also shows many indexable article titles longer than `65` characters:

- `1217` indexable title rows over `65` characters

This is not the best next batch.

Reason:

- title-length issues at this scale are broad editorial normalization work
- residual broken links and missing hub metadata are more contained and more actionable right now

## Deliverable For Execution

Use:

- `defiliban_wave3_actions_2026-05-25.csv`

That file includes:

- residual `301` / `404` link targets with priority
- indexable hubs missing meta descriptions

## Practical Wave 3 Order

1. clean `/t/coinbase/`
2. clean `/cdn-cgi/l/email-protection`
3. batch the remaining residual `301` / `404` rows from the CSV
4. fill metadata for the `18` indexable hubs
5. add `H1` to `/blog/`
