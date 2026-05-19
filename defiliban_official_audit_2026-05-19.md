# DeFiliban Official-Safe SEO Audit

Date: 2026-05-19

Scope:

- Domain: `https://defiliban.io/`
- Crawl inputs: Screaming Frog exports in `/home/qcweb/defiliban`
- GSC inputs: coverage drilldown and performance exports in `/home/qcweb/defiliban/gsc`
- Method: official Google Search guidance first, then clearly-labeled heuristics

Verdict:

- `at risk`

## Executive Summary

The site does not look blocked or fundamentally broken at the template level. Article pages sampled are crawlable, indexable, canonicalized, and already emit useful structured data.

The main problem is selection quality and crawl/index noise. Google already knows many DeFiliban URLs, but is not choosing a large portion of them for indexing. The evidence points to a combination of:

1. low-value or noisy URLs being promoted as first-class crawl targets
2. duplicate or near-duplicate article clusters
3. utility and archive pages consuming too much internal prominence
4. broken internal linking and leftover theme artifacts

## What Is Already Fine

These are positive signals from the local crawl and live page checks:

- sampled article pages return `200`, use self-canonical, and expose `index,follow`
- structured data is present on sampled article pages, including `Article` or `NewsArticle`, `BreadcrumbList`, `Organization`, and `Person`
- author-like, tag-like, and search-result URLs appear to be mostly `noindex`
- sitemap index exists and does not appear to be completely unmanaged

## Officially Supported Findings

These points are directly aligned with Google Search Central documentation.

### 1. Utility pages should not be sitemap-promoted if they are not intended as search landing pages

Issue:

- `https://defiliban.io/my-bookmarks/`
- `https://defiliban.io/customize-interests/`

Evidence:

- both return `200`
- both are `Indexable`
- both use self-canonical
- both have `3214` inlinks in the crawl
- both still appear in `https://defiliban.io/page-sitemap.xml`

Why it matters:

- Google recommends using sitemaps to tell Search about pages that matter on the site
- utility or personalized pages should not compete with editorial URLs for crawl attention

Fix:

- switch both URLs to `noindex,follow`
- remove both from XML sitemaps
- reduce crawlable sitewide exposure for logged-out users if possible

Official source:

- Google sitemap guidance: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- Google noindex guidance: https://developers.google.com/search/docs/crawling-indexing/block-indexing

### 2. External theme-demo links in sitewide navigation are a real crawl-quality defect

Issue:

- homepage HTML still contains:
  - `https://foxiz.themeruby.com/coin/category/crypto/`
  - `https://foxiz.themeruby.com/coin/category/news/`

Evidence:

- live homepage source contains both URLs
- both receive `3188` internal inlinks each in `response_codes_all.csv`
- combined navigation inlinks are `6376` in `all_inlinks.csv`

Why it matters:

- Google uses links to discover and prioritize content
- sitewide navigational links pointing to irrelevant external targets waste crawl paths and leak internal authority

Fix:

- replace the menu targets with real DeFiliban section URLs
- purge caches and re-crawl

Official source:

- Search Essentials overview: https://developers.google.com/search/docs/fundamentals/creating-helpful-content

### 3. Broken internal links should be cleaned up, especially when they are repeated at scale

Issue:

- the crawl found `464` internal `404` rows
- the largest broken target is `https://defiliban.io/cdn-cgi/l/email-protection` with `6994` internal inlinks

Why it matters:

- Google can handle ordinary `404`s, but avoidable broken internal links are still a site-quality problem and waste crawl routes

Fix:

- remove or repair the email-protection output that emits `/cdn-cgi/l/email-protection`
- then clean the top repeated article 404 targets from live content

Official source:

- Search Essentials and crawl hygiene principles: https://developers.google.com/search/docs/fundamentals/seo-starter-guide

### 4. Sitemaps and canonicals should reinforce the preferred URL set, not duplicate it

Issue:

- `?p=` URLs appear in GSC redirect and crawled-not-indexed buckets
- `uncategorized` is still indexable and active
- utility pages are canonicalized to themselves and included in sitemap

Why it matters:

- Google recommends consolidating duplicate URLs and being consistent across internal linking, canonicals, and sitemaps

Fix:

- remove low-value URLs from the sitemap set
- keep one preferred URL per content item
- stop using `Uncategorized` as an active taxonomy destination

Official source:

- Canonical guidance: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- Sitemap guidance: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap

### 5. `noindex` is the correct control for pages you want crawled but not indexed

Relevant to this site:

- some low-value pages already appear intentionally noindexed
- the remaining problem pages that should stay accessible but not rank are better handled with `noindex` than `robots.txt`

Important note:

- `robots.txt` is not a removal tool for already indexed URLs
- if Google must see the page in order to see `noindex`, do not block it from crawling first

Official source:

- https://developers.google.com/search/docs/crawling-indexing/block-indexing

## Reasonable Heuristics

These are strong operational conclusions from the data, but they are not explicit Google rules.

### 1. Deep archive pagination is probably over-indexed

Evidence:

- `571` indexable paginated HTML URLs out of `2926` indexable HTML URLs
- section counts include:
  - `/blog/page/*` = `232`
  - `/crypto/page/*` = `143`
  - `/news/page/*` = `35`
  - `/market/page/*` = `37`
- duplicate title patterns are heavy:
  - `Blog - DeFiliban` = `233`
  - `Crypto - DeFiliban` = `144`
  - `News - DeFiliban` = `36`

Interpretation:

- Google does not forbid indexable pagination, but this amount of repetitive archive inventory is unlikely to be the best use of crawl and index budget for this site

Suggested action:

- keep strong section hubs indexable
- test shifting deeper paginated pages to `noindex,follow`
- then compare GSC coverage changes after 2 to 4 weeks

### 2. The biggest indexing problem is article selection, not just archive depth

Evidence from GSC `Discovered - currently not indexed`:

- total URLs: `1000`
- matched back to crawl exports: `974`
- matched URLs returning `200`: `973`
- matched URLs still `Indexable`: `973`
- single-slug article-like URLs: `958`

Interpretation:

- Google already knows many article URLs and still is not selecting them
- this looks more like a content-quality, duplication, or publishing-pattern issue than a pure crawl-access problem

### 3. Duplicate and promotional clusters are likely suppressing index selection

Evidence inside the discovered bucket:

- `19` single-slug article-like URLs already reuse a title seen elsewhere in the crawl
- `23` single-slug article-like URLs end with duplicate-style suffixes such as `-2`, `-3`, or `-4`
- `119` single-slug article-like URLs mention `BlockDAG` in the slug or title
- example duplicate title cluster:
  - `https://defiliban.io/based-binance-alpha-listing/`
  - `https://defiliban.io/based-binance-alpha-listing-2/`
- example generic duplicate cluster:
  - `https://defiliban.io/new-policy-changes-local-businesses-12/`
  - `https://defiliban.io/local-business-policy-changes-3/`
  - both reuse the same title

Interpretation:

- this pattern strongly suggests duplicate publishing, low-differentiation rewrites, and promotional volume that Google may not consider worth indexing at scale

Suggested action:

- split the discovered bucket into:
  - keep and improve
  - merge into canonical
  - remove from sitemap promotion
  - noindex or retire

### 4. AI-bot blocking is a business choice, not a Google Search violation

Evidence:

- live `robots.txt` contains `GPTBot`, `ClaudeBot`, `Google-Extended`, and `Applebot-Extended`

Interpretation:

- this does not block Google Search indexing by itself
- it may reduce visibility in non-Google AI systems or affect Google training opt-ins, but it is not the cause of ordinary web-search indexation issues

Official context:

- AI features guidance: https://developers.google.com/search/docs/appearance/ai-features

## Coverage Drilldown Readout

GSC coverage exports currently show:

- `Bị loại trừ bởi thẻ 'noindex'`: `210`
- `Không tìm thấy (404)`: `61`
- `Trang có lệnh chuyển hướng`: `6`
- `Đã phát hiện thấy – hiện chưa được lập chỉ mục`: `1000`
- `Đã thu thập dữ liệu – hiện chưa được lập chỉ mục`: `11`

Interpretation:

- the `noindex` bucket is not the biggest problem and looks mostly intentional
- the critical bucket is `Discovered - currently not indexed`
- the small `Crawled - currently not indexed` bucket means the larger issue is what URLs the site is pushing into discovery, not just post-crawl rejection

## Priority Actions

### Fix in 24 Hours

1. Replace the two theme-demo nav URLs with real DeFiliban section URLs.
2. Set `/my-bookmarks/` and `/customize-interests/` to `noindex,follow` and remove them from sitemap.
3. Remove the `/cdn-cgi/l/email-protection` broken-link pattern.
4. Stop active use of `Uncategorized`.

### Fix in 7 Days

1. Define archive policy for paginated section URLs.
2. Clean the highest repeated internal links to dead article URLs.
3. Review low-value section archives and confirm which deserve indexation.
4. Verify whether `local-sitemap.xml` has any real business purpose.

### Fix in 30 Days

1. Segment the `1000` discovered-not-indexed URLs into canonical keep, merge, noindex, and retire buckets.
2. Reduce duplicate-title and duplicate-slug article clusters.
3. Rework internal linking so hubs promote the article set the site actually wants indexed.
4. Refresh the zero-click but impression-bearing pages first.

## Suggested Working Rule For This Site

If a page is not intended to rank on its own, it should not be:

1. indexable
2. self-canonical
3. linked sitewide
4. present in XML sitemap

DeFiliban currently violates that rule in several utility and archive cases, and the crawl data shows the cost.

## Deliverables Created

- Execution plan: `/home/qcweb/defiliban/defiliban_seo_fix_plan_2026-05-19.md`

