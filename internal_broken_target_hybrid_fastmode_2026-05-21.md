# DeFiliban Broken Target Hybrid Fast Mode

Date: 2026-05-21

Status:

- `prepared`

This package switches from slow per-post cleanup to a hybrid workflow:

1. Import redirects for high-confidence broken targets.
2. Keep low-confidence cases in a manual review queue.
3. Only clean HTML in posts for the highest-priority rows after redirects are live.

## Outputs

- `rankmath_redirect_import_broken_targets_high_confidence_2026-05-21.csv`
- `broken_target_redirect_mapping_2026-05-21.csv`
- `broken_target_redirect_review_queue_2026-05-21.csv`
- `content_fix_priority_shortlist_2026-05-21.csv`

## Counts

- `377` broken targets remained after phase 9, excluding `/cdn-cgi/l/email-protection`.
- `321` targets were mapped at high confidence and are ready for redirect import.
- `56` targets were left in review because the mapping was ambiguous or weak.
- `100` high-priority source-link rows were shortlisted for later HTML cleanup.

## Recommended Order

1. Import `rankmath_redirect_import_broken_targets_high_confidence_2026-05-21.csv` into Rank Math Redirections.
2. Purge cache.
3. Re-crawl or spot-check a sample of imported redirects.
4. Use `content_fix_priority_shortlist_2026-05-21.csv` for manual or scripted HTML cleanup in the most important source posts.
5. Review `broken_target_redirect_review_queue_2026-05-21.csv` separately before importing anything from that set.

## Notes

- This does not change plugin files or plugin state. It only prepares data files for import and cleanup.
- The redirect import file uses the Rank Math CSV format already used earlier in this project.
- High-confidence mapping required a strong slug match against a live `200 Indexable` page, with an extra margin rule when multiple candidates were close.
