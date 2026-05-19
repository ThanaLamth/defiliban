---
name: qc-internal-link
description: Audit or plan internal linking using a traffic-first, authority-allocation model. Use when the user asks about internal links, link noi bo, topical authority, which pages should link to which pages, or how to improve rankings by linking strong pages to pages ranking around positions 5-10.
---

# QC Internal Link

Use this skill when the task is about:

- auditing an internal linking setup
- deciding which pages should link to which pages
- improving rankings through internal links
- evaluating topical authority and link flow
- reviewing whether a site is wasting internal links

## Core Model

Treat each internal link as an authority allocation decision, not decorative SEO.

Default assumptions:

- more internal links is not automatically better
- weak pages usually have little to pass on
- pages with traffic, rankings, and crawl attention are the main link sources
- the best targets are often pages already ranking around positions `5-10`
- internal linking is iterative and should be updated as rankings change

## Workflow

1. Identify candidate source pages.
Source pages should already have traffic, rankings, and user engagement.

2. Identify candidate target pages.
Prioritize pages close to top positions rather than pages with very low ranking potential.

3. Check whether each target can realistically rank.
Do not recommend pushing impossible head terms for a weak site unless there is clear evidence.

4. Minimize wasted dilution.
If a page links out to too many internal targets, call out authority dilution and suggest prioritization.

5. Evaluate topic fit.
Internal links should strengthen clusters and topical authority, not create random cross-topic jumps.

6. Recommend a dynamic loop.
Once a target page improves and becomes strong, use it as a new source page for the next layer.

## Output

Return:

- verdict: strong / mixed / weak internal linking
- strongest source pages
- best near-win target pages
- wasted links or diluted sections
- topical cluster opportunities
- next linking actions in priority order

## Read This Reference

Read [references/internal-link-rules.md](references/internal-link-rules.md) when you need the detailed operating rules, cautions, and the preferred GSC-driven workflow.
