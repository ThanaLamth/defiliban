# DeFiliban Internal Link Cleanup Phase 8

Date: 2026-05-21

Status:

- `done`

This phase rechecked the next six broken article targets that had clear live replacements on site.

## Targets Reviewed

1. `/michael-saylor-hints-at-another-bitcoin-buy-with-huge-orange-dot/`
2. `/blockchain-capital-plans-700m-raise-for-two-funds/`
3. `/t-rowe-price-crypto-etf-s-1-names-anchorage/`
4. `/upbit-to-list-usd-ai-chip-with-krw-trading-pair-on-april-21/`
5. `/grayscale-ethereum-mini-trust-staked-102400-eth-237m/`
6. `/remixpoint-buys-19-72-btc-holdings-hit-1471-btc/`

## What Happened

- `12` source-link rows across `11` unique source posts were swept in this phase.
- `2` rows were already clean on recheck, so no new edit was needed.
- `10` rows still contained the old href and were updated live:
- `https://defiliban.io/top-5-crypto-news-24-hours-bitcoin-price-drops-trump-iran-threat/`
- `https://defiliban.io/bitcoin-etf-inflows-defi-impact/`
- `https://defiliban.io/tether-froze-344-million-usdt-us-law-enforcement-requests/`
- `https://defiliban.io/lido-proposes-up-to-2500-steth-for-rseth-relief-effort/`
- `https://defiliban.io/500m-usdt-transferred-tether-treasury-binance/`
- `https://defiliban.io/us-bitcoin-spot-etfs-202-million-net-inflow-march-16/`
- `https://defiliban.io/chip-listed-on-coinbase-spot-market/`
- `https://defiliban.io/bitcoin-etfs-weekly-inflows-823-million-daily-streak/`
- `https://defiliban.io/xrp-etfs-april-inflows-81-6m-best-month-2026/`
- `https://defiliban.io/riot-platforms-deposits-another-500-btc-to-nydig/`

## Verification

- Rechecked source rows either returned `already_clean` or were updated to `done`.
- For the ten edited rows, verification after update showed `old_left = 0`.
- No plugin or settings changes were used. This phase only touched post content links.

## Notes

- The source post `chip-listed-on-coinbase-spot-market` had two links pointing to the same broken target. The first update replaced both hrefs at once, so the second row rechecked as `already_clean`.

## Batch File

- `internal_link_cleanup_batch8_2026-05-21.csv`
