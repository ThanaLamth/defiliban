# DeFiliban Phase: Archive + Thin Content

Date: 2026-05-21

Verdict:

- `partially aligned`

This phase is much cleaner than the original crawl. The main archive-pagination problem is mostly under control live, and most low-value generic thin URLs are already gone. The remaining work is narrow:

1. keep strong archive hubs indexed
2. keep weak archive variants noindexed
3. decide whether `/market/investor/` is a real search landing page
4. rewrite 3 remaining thin-ish crypto articles instead of deleting them

## Official Basis

These actions are consistent with Google Search Central:

- Use sitemaps to surface URLs that matter: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- Use `noindex` for crawlable pages you do not want indexed: https://developers.google.com/search/docs/crawling-indexing/block-indexing
- Consolidate duplicate or alternate URLs consistently: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- Focus on helpful, people-first content rather than mass low-value inventory: https://developers.google.com/search/docs/fundamentals/creating-helpful-content

## Archive Status

Live checks now show:

- `/blog/`, `/crypto/`, `/news/` are still `index,follow`
- `/blog/page/2/`, `/crypto/page/2/`, `/news/page/2/` are now `noindex,follow`
- `/press-release/` is `noindex,follow`
- `/news/coinbase/` is `noindex,follow`
- `/t/coinbase/` now `301`s to `/news/coinbase/`
- `/market/binance/page/5/` is `noindex,follow`
- `/market/investor/` is still `index,follow` and still appears in `category-sitemap.xml`

Priority decision:

- If `Investor` is not a true editorial hub with a real topic plan, set `/market/investor/` to `noindex,follow` and remove it from the category sitemap.
- If it is meant to be a strategic hub, keep it indexed but it needs stronger copy, a clearer intro, and a defined internal-link role.

## Thin Content Status

The generic non-crypto thin cluster is already effectively cleaned:

- `/company-policy-change-employees/` = `404`
- `/government-renewable-energy-policy/` = `404`
- `/new-policy-changes-impact-businesses/` = `404`
- `/policy-changes-impacting-local-businesses/` = `404`
- `/local-business-policy-changes/` = `404`

The remaining thin-ish URLs worth keeping are:

- `/blackrock-bitcoin-trust-outflow/`
- `/cardano-ada-holdings-audit/`
- `/microstrategy-bitcoin-acquisition-strategy/`

These should be rewritten, not deleted.

## Recommended Sequence

1. Archive: decide `/market/investor/`
2. Archive: leave current pagination and noindex archive controls as they are
3. Content: rewrite the 3 keep-and-improve articles
4. Re-crawl those 3 URLs plus `/market/investor/`

## Files

- `archive_action_2026-05-21.csv`
- `thin_content_action_2026-05-21.csv`
