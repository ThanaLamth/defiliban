# DeFiliban Google News Readiness

Date: 2026-05-27

## Official Baseline

Google News now evaluates eligible web content automatically. There is no longer a manual requirement to submit a publication for a News source page.

Primary official references:

- Google News automatically-generated publication pages
- Google News technical guidelines
- Google News content policies
- Google Search article structured data guidance

## Current Verdict

- Technical eligibility: close
- Transparency readiness: incomplete
- Content trust readiness: weak to mixed
- Overall Google News readiness: not blocked technically, but not yet strong enough to rely on News inclusion

## What DeFiliban Already Has

- Stable main section URLs such as `/news/`, `/crypto/`, and market/category paths
- HTML-rendered article cards and section links on core pages
- Article pages with titles, dates, and bylines on live content
- Article schema present on the site
- `rb-etemplate` sitemap removed from live sitemap discovery flow
- `rb-etemplate` URLs now excluded from sitemap and set to `noindex`
- Large attachment-style promo cleanup completed

## What Still Limits Google News Inclusion

### 1. Transparency Signals Are Incomplete

Google News policies emphasize clear information about:

- who wrote the content
- who publishes the site
- the organization behind the publication
- how readers can contact the publication

Current gaps still visible on DeFiliban:

- footer social icons still contain placeholder `#` links
- About / publisher identity is not yet strong enough
- Contact / editorial transparency should be more explicit
- author profile depth is not yet consistent

### 2. Historical Content Quality Is Mixed

The site had a large volume of:

- promo-style articles
- presale / prediction pages
- attachment-style junk URLs
- low-trust advertorial-like content

Even after cleanup, that history weakens trust until the site runs a sustained period of cleaner publishing.

### 3. News-vs-Non-News Separation Is Not Strong Enough

For Google News, the publication should look consistently like a news publisher.

Content that should not dominate the site:

- price predictions
- presales
- "best crypto to buy" style pages
- sponsored/promotional pages without strong disclosure

## Minimum Conditions DeFiliban Should Maintain

- news sections remain crawlable through HTML links
- article URLs stay stable and unique
- byline and publish date are visible on article pages
- template/query URLs stay out of index and out of sitemap
- low-value promo content does not keep reappearing

## Recommended Schema Baseline

Keep article pages consistent with:

- `Article` or `NewsArticle`
- `headline`
- `image`
- `author`
- `datePublished`
- `dateModified`

Schema is not a guarantee of News inclusion, but it helps Google understand article pages correctly.

## Practical Readiness Assessment

### Ready Now

- technical cleanup direction
- sitemap cleanup for template URLs
- attachment-style promo cleanup

### Not Ready Yet

- publisher transparency
- long enough clean publishing streak
- strong separation between news and promotional content

## Final Judgment

DeFiliban is no longer held back by the obvious technical junk that previously polluted crawl and discovery. The next constraint is not crawlability; it is trust, transparency, and content quality consistency.

To improve the chance of appearing on Google News surfaces, DeFiliban should spend the next publishing cycle acting like a clean, transparent news site rather than a mixed crypto promo site.
