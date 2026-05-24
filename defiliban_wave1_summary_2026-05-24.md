# DeFiliban Wave 1 Summary

Date: 2026-05-24

Scope:

- This summarizes the first cleanup wave before the recrawl-based mobile menu follow-up.
- Counts below are pulled from the local execution files already committed in this repo.

## 1. Duplicate / Duplicate-Like URL Review

Source:

- `duplicate_post_cleanup_2026-05-19.csv`

Reviewed rows:

- `122`

Breakdown from `final_action`:

- `16` -> `keep`
- `3` -> `keep_and_improve`
- `2` -> `keep_hub_or_noindex`
- `5` -> `noindex_low_value_generic`
- `22` -> `301_to_canonical`
- `46` -> `manual_review_numeric_suffix`
- `2` -> `noindex_subpage`
- `26` -> `delete_404`

Open review queue after this stage:

- `7` rows in `remaining_duplicate_review_2026-05-21.csv`

## 2. Redirect Packages Prepared

Sources:

- `rankmath_redirect_import_broken_targets_high_confidence_2026-05-21.csv`
- `rankmath_redirect_import_review_round1_approved_2026-05-21.csv`
- `rankmath_redirect_import_review_round2_approved_2026-05-21.csv`

Prepared redirect rows:

- `321` high-confidence
- `21` approved in review round 1
- `12` approved in review round 2

Total prepared redirect rows:

- `354`

## 3. Broken Target Review Split

Sources:

- `broken_target_keep_404_2026-05-21.csv`
- `broken_target_hold_next_review_2026-05-21.csv`

Counts:

- `9` marked `keep_404`
- `7` marked `hold_next_review`

Meaning:

- `keep_404` = no safe replacement, malformed, or misleading to redirect
- `hold_next_review` = topic-near but not confirmed story-equivalent

## 4. Live Internal Link Cleanup In Post Content

Source:

- `content_fix_priority_shortlist_results_2026-05-21.csv`

Rows processed:

- `100` source-link rows

Unique source posts covered:

- `95`

Execution result:

- `81` rows = `done`
- `17` rows = `already_clean`
- `2` rows = `no_postid`

Verification result:

- `0` `verify_failed`
- `0` `error`

## 5. Archive / Indexation Cleanup

Source:

- `archive_action_2026-05-21.csv`

Tracked archive URLs:

- `11`

Wave 1 status by action bucket:

- core hubs intentionally kept indexed: `3`
  - `/blog/`
  - `/crypto/`
  - `/news/`
- archive / pagination variants kept `noindex`: `8`

Examples already shifted to `noindex` by the end of wave 1:

- `/blog/page/2/`
- `/crypto/page/2/`
- `/news/page/2/`
- `/press-release/`
- `/news/coinbase/`
- `/market/binance/page/5/`

## 6. Thin Content Cleanup

Source:

- `thin_content_action_2026-05-21.csv`

Tracked thin-content URLs:

- `10`

Breakdown:

- `3` -> `rewrite_expand_keep_index`
- `5` -> `done_404`
- `2` -> `archive_keep_noindex`

Generic thin cluster already removed in wave 1:

- `5` URLs moved to `404`

Remaining keep-and-improve article count at that stage:

- `3`

## 7. What Wave 1 Achieved

Before the next recrawl-based follow-up, wave 1 had already:

- reviewed `122` duplicate / duplicate-like rows
- prepared `354` redirect import rows
- split unresolved broken targets into `9` keep-404 and `7` hold-review cases
- cleaned `100` prioritized source-link rows across `95` posts
- stabilized the main archive noindex strategy across `11` tracked URLs
- removed `5` generic thin-content URLs and retained `3` crypto articles for rewrite

## 8. What Was Not Fully Caught Until After Wave 1

The later recrawl exposed a separate template-level issue not fully visible in the earlier action logs:

- legacy mobile menu / mobile quick-access links still emitting:
  - `/home-coin/`
  - `/coin-home-5/`
  - `/?page_id=2389`
  - `/?page_id=2413`

That issue belongs to the post-wave-1 follow-up, not to the original wave-1 execution.
