# DeFiliban SEO Fix Plan

Date: 2026-05-19

Scope:

- Domain: `https://defiliban.io/`
- Crawl source: Screaming Frog exports in `/home/qcweb/defiliban`
- GSC source: coverage and performance exports in `/home/qcweb/defiliban/gsc`

Verdict:

- `at risk`

This plan converts the audit into execution tasks for `SEO` and `dev`.

## Main Diagnosis

The site has a workable article template, but too much crawl and index noise is competing with the URLs that should matter most.

The biggest issues are:

1. sitewide navigation links pointing to external theme demo URLs
2. utility pages that are indexable, sitemap-listed, and heavily linked
3. deep paginated archives kept indexable with weak titles/H1s
4. many internal links to dead or unstable article URLs
5. a large `Discovered - currently not indexed` bucket in GSC, mostly article-like URLs returning `200`
6. duplicate or promotional article clusters that are likely diluting indexing and quality signals

## Fix In 24 Hours

### 1. Replace theme demo links in the main navigation

Owner:

- `dev`

Issue:

- the sitewide nav links `Cryptocurrency` and `News` currently point to:
  - `https://foxiz.themeruby.com/coin/category/crypto/`
  - `https://foxiz.themeruby.com/coin/category/news/`

Why it matters:

- creates sitewide 301 noise
- leaks authority and user flow to a theme demo URL
- signals incomplete theme cleanup

Evidence:

- `6376` inlinks from navigation in `all_inlinks.csv`

Action:

- update nav/mega-menu targets to the real DeFiliban section URLs
- purge all caches
- verify on homepage and article pages

Done when:

- no internal nav links point to `foxiz.themeruby.com`
- Screaming Frog no longer reports those two URLs as high-inlink 301 destinations

### 2. Noindex utility pages and remove them from the sitemap

Owner:

- `SEO + dev`

URLs:

- `https://defiliban.io/my-bookmarks/`
- `https://defiliban.io/customize-interests/`

Why it matters:

- both are indexable
- both are in `page-sitemap.xml`
- both have `3214` inlinks
- both look like utility or personalization pages, not search assets

Action:

- change to `noindex,follow`
- remove from XML sitemap
- reduce or remove sitewide crawlable nav links if possible for logged-out users

Done when:

- both pages return `200`
- both pages show `noindex,follow`
- neither URL appears in `page-sitemap.xml`

### 3. Fix the `cdn-cgi/l/email-protection` internal-link pattern

Owner:

- `dev`

Issue:

- one broken internal target gets `6994` internal inlinks

Why it matters:

- huge sitewide internal 404 target
- crawl waste
- avoidable technical noise

Action:

- remove or repair the obfuscated email link implementation
- confirm header/content no longer emit links to `/cdn-cgi/l/email-protection`

Done when:

- the URL no longer appears as a 404 destination with sitewide internal inlinks

### 4. Remove `Uncategorized` from active taxonomy use

Owner:

- `SEO + editorial + dev`

Issue:

- `https://defiliban.io/uncategorized/` is still indexable and present in category sitemap

Action:

- assign all posts to real categories
- disable or redirect `Uncategorized` if no editorial reason remains

Done when:

- no new posts publish under `Uncategorized`
- the archive is either gone, redirected, or intentionally kept with a clear purpose

## Fix In 7 Days

### 5. Rework pagination indexation strategy

Owner:

- `SEO + dev`

Issue:

- `571` indexable paginated HTML URLs out of `2926` indexable HTML URLs
- examples:
  - `/blog/page/*` = `232`
  - `/crypto/page/*` = `143`
  - `/news/page/*` = `35`

Why it matters:

- many deep archive pages are self-canonical and fully indexable
- titles and H1s are repetitive
- a large share of the site's indexable HTML is archive pagination rather than distinct content
- likely contributes to the `1000` URL GSC bucket `Discovered - currently not indexed`

Action:

- keep main archive hubs indexable:
  - `/blog/`
  - `/crypto/`
  - `/news/`
  - other strong section hubs that genuinely help users
- evaluate deep paginated URLs and likely shift them to `noindex,follow`
- preserve crawl paths for discovery, but stop treating deep page 20/50/100 as standalone search pages

Done when:

- there is a documented rule for archive pagination
- deep pagination no longer self-canonical + index,follow by default unless intentionally justified

### 6. Clean internal contextual links to removed article URLs

Owner:

- `SEO + editorial`

Issue:

- many dead article URLs still receive contextual internal links inside article bodies

Action:

- start with the highest repeated 404 targets from the audit
- replace internal links with:
  - the current live replacement article
  - the parent topic hub
  - or remove the link entirely

Priority examples:

- `bitcoin-etf-flows-today-111m-single-day-outflow-as-7-day-drain-hits-211m`
- `blackrock-withdraws-6167-btc-coinbase-outflows`
- `binance-adds-new-spot-trading-pairs-on-april-6-2026`
- `hyperbridge-exploit-mints-1b-bridged-dot-on-ethereum`

Done when:

- top broken internal article links are replaced on source pages
- internal 404 inlinks fall materially on recrawl

### 7. Audit indexable low-value archive variants under section paths

Owner:

- `SEO`

Focus:

- `/market/investor/`
- `/market/binance/page/5/`
- similar low-value section archives

Why it matters:

- some indexable archive-like URLs have low word count and generic heading structure
- they may be soaking crawl without earning meaningful search demand

Action:

- classify each as:
  - keep indexable
  - keep but improve
  - noindex
  - consolidate into stronger parent archive

Done when:

- every indexable archive-like section has a documented purpose

### 8. Verify `local-sitemap.xml` is intentional

Owner:

- `dev + SEO`

Issue:

- `local-sitemap.xml` currently points to `locations.kml`
- this is unusual for a crypto news site unless a local SEO feature genuinely exists

Action:

- confirm what plugin or feature created it
- keep only if there is a real business use case
- otherwise remove the local sitemap artifact

Done when:

- the team can explain why `local-sitemap.xml` exists
- if no valid use case, remove it from active sitemap architecture

## Fix In 30 Days

### 9. Reduce the `Discovered - currently not indexed` bucket

Owner:

- `SEO + dev + editorial`

Current signal:

- GSC `Discovered - currently not indexed`: `1000` URLs

Interpretation:

- Google knows about too many URLs it does not think are worth indexing yet
- this is not just a pagination problem:
  - `974` URLs from this bucket were matched back to the crawl exports
  - `973` of those matched URLs return `200` and are still `Indexable`
  - `958` are single-slug article-like URLs rather than section pagination
- likely caused by a mix of:
  - weak or duplicated article/value patterns
  - promotional or syndicated-looking content clusters
  - archive depth and broad internal discovery paths
  - utility and template noise

Action:

1. complete the 24h and 7-day fixes first
2. re-crawl the site
3. compare the GSC bucket after 2-4 weeks
4. if still large, segment by URL type:
   - articles
   - pagination
   - category-like URLs
   - media or utility pages
5. separately triage the article-like URLs in this bucket:
   - keep and improve
   - merge into the canonical version
   - noindex
   - remove from sitemap and internal promotion

Done when:

- the bucket shrinks materially
- the remaining URLs in the bucket are mostly valid new content awaiting normal indexing

### 10. Triage duplicate and promotional article clusters

Owner:

- `SEO + editorial`

Current signal:

- `24` article-like URLs in the `Discovered - currently not indexed` set already reuse a title seen elsewhere in the crawl
- `23` article-like URLs in that same bucket end with duplicate-style slug suffixes such as `-2`, `-3`, or `-4`
- `119` article-like discovered URLs mention `BlockDAG` in the slug or title

Interpretation:

- this pattern suggests a mix of duplicate publishing, near-duplicate rewrites, and promotional volume that Google may not be selecting for indexing

Action:

1. export the full discovered URL set into review buckets:
   - exact duplicate or obvious near-duplicate
   - sponsored / promotional / syndication-like
   - original news worth improving
2. for duplicates:
   - keep one canonical article
   - redirect or deindex the weaker copies based on implementation fit
3. for low-value promotional pieces:
   - stop pushing them through main sitemap and homepage/archive prominence unless they serve a real business goal
4. for worthwhile originals:
   - improve titles, intros, source transparency, and internal linking from real hubs

Done when:

- duplicate title/suffix clusters are materially reduced
- sitemap and internal linking prioritize the article set the team actually wants indexed

### 11. Review article quality patterns on zero-click / high-impression pages

Owner:

- `SEO + editorial`

Evidence from GSC:

- some pages already get impressions with weak or zero CTR, for example:
  - `/crypto-tax-stablecoin-exemption/`
  - `/btc-short-liquidity-cluster-above-74k-negative-funding-short-squeeze/`
  - `/ripple-ceo-testifies-crypto-regulation/`

Action:

- audit top impression / low-click pages for:
  - title quality
  - SERP intent alignment
  - clearer summary paragraphs
  - stronger source transparency
  - better internal links from section hubs

Done when:

- the top low-CTR impression pages have been individually reviewed and updated where needed

### 12. Create a durable archive policy

Owner:

- `SEO lead`

Document:

- which page types can be indexed
- which must be noindexed
- when a category is strong enough to stand as a hub
- which utility pages must never be in sitemap
- how pagination should behave

Why it matters:

- prevents the same crawl/index bloat from returning after future publishing or theme changes

Done when:

- archive/indexation rules exist as a written SOP and are shared with dev and editorial

## Validation Checklist After Fixes

Run a fresh crawl and confirm:

- no sitewide nav links to `foxiz.themeruby.com`
- `/my-bookmarks/` and `/customize-interests/` are noindex and absent from sitemap
- `cdn-cgi/l/email-protection` is no longer a major internal 404 target
- indexable pagination count is materially reduced if the new policy is implemented
- internal 404 inlinks have dropped
- `Uncategorized` is cleaned up
- `local-sitemap.xml` is either justified or removed

## Next Data Pull

After fixes, compare:

- new Screaming Frog crawl
- GSC coverage bucket sizes
- GSC page impressions/clicks for the same 28-day period

The most important KPI is not just fewer errors. It is:

- fewer low-value URLs competing for crawl and indexing
- stronger concentration of signals on real article and hub URLs
