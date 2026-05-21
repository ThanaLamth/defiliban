# DeFiliban Broken Target Endgame

Date: 2026-05-21

Status:

- `prepared`

This closes the current redirect review workflow by separating the unresolved broken targets into:

1. `keep_404`
2. `hold_next_review`

## Outputs

- `broken_target_keep_404_2026-05-21.csv`
- `broken_target_hold_next_review_2026-05-21.csv`

## Counts

- `9` targets were marked `keep_404`.
- `7` targets were marked `hold_next_review`.

## Meaning

- `keep_404`
  These targets either have no trustworthy live replacement, point to a clearly different story, or are malformed URLs. Redirecting them would likely be worse than leaving them broken.

- `hold_next_review`
  These targets may still be recoverable, but only after manual title/content comparison. They are topic-near, not story-certain.

## Recommended Next Step

1. Import the high-confidence redirect file.
2. Import round 1 approved review redirects.
3. Import round 2 approved review redirects.
4. Leave `keep_404` alone.
5. Revisit `hold_next_review` only if you want more coverage and are willing to review article meaning manually.
