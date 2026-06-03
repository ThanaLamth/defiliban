# DeFiliban Category Migration Spec

Ngày: 2026-06-03

## Mục tiêu

Tài liệu này chốt 4 việc:

- category architecture mới cho Defiliban
- mapping category hiện tại sang cấu trúc mới
- menu structure nên dùng sau khi tạo category mới
- rollout plan để chuyển dần mà không làm gãy index khi site đang tăng mạnh

## Snapshot category hiện tại

Lấy từ REST API public của site ngày 2026-06-03.

### Top-level hiện tại

| Category | Slug | Count | Ghi chú |
| --- | --- | ---: | --- |
| Blockchain | `blockchain` | 113 | archive rộng, intent mơ hồ |
| Blockchain Event | `blockchain-event` | 8 | không nên là pillar |
| CMC | `cmc` | 0 | không nên dùng |
| Crypto | `crypto` | 832 | quá rộng, cần tách dần |
| Market | `market` | 88 | quá rộng, intent trộn lẫn |
| News | `news` | 104 | có thể giữ như news stream |
| Press Release | `press-release` | 9 | nên giữ riêng |
| Projects | `projects` | 2 | quá mỏng |
| Uncategorized | `uncategorized` | 2 | cần xóa sạch |

### Child category hiện tại

| Category | Slug | Parent | Count |
| --- | --- | --- | ---: |
| Binance | `binance` | `market` | 53 |
| Bitcoin | `bitcoin` | `crypto` | 477 |
| Business | `business` | `market` | 195 |
| Coinbase | `coinbase` | `news` | 9 |
| Ethereum | `ethereum` | `crypto` | 159 |
| Forex | `forex` | `crypto` | 5 |
| Investor | `investor` | `market` | 2 |
| Mining | `mining` | `news` | 27 |
| Money | `money` | `market` | 4 |
| NFT | `nft` | `news` | 6 |
| Stocks | `stocks` | `news` | 17 |
| Tether | `tether` | `crypto` | 17 |
| Trading | `trading` | `market` | 7 |

## Kết luận ngắn

- `crypto`, `market`, `blockchain` đang quá rộng
- các category kiểu asset hoặc brand như `bitcoin`, `ethereum`, `binance`, `coinbase` không nên là trục taxonomy chính của site nếu muốn đẩy DeFiliban thành DeFi specialist
- `news` có thể giữ, nhưng chỉ nên là lớp format/editorial stream, không phải topical pillar chính
- `press-release` nên giữ tách khỏi editorial core

## Architecture mới

### Editorial pillars

Đây là 5 category top-level nên dùng cho phần editorial core:

1. `protocols`
2. `yield`
3. `liquidity`
4. `risk`
5. `infrastructure`

### Subcategory chuẩn

#### `protocols`

- `protocols/dex`
- `protocols/lending`
- `protocols/derivatives`
- `protocols/stablecoins`
- `protocols/governance`

#### `yield`

- `yield/staking`
- `yield/farming`
- `yield/strategies`

#### `liquidity`

- `liquidity/pools`
- `liquidity/capital-flows`
- `liquidity/amm`

#### `risk`

- `risk/exploits`
- `risk/liquidations`
- `risk/smart-contracts`

#### `infrastructure`

- `infrastructure/oracles`
- `infrastructure/bridges`
- `infrastructure/layer2`

### Non-editorial / special buckets

Giữ riêng, không trộn với editorial pillars:

- `news`
- `press-release`
- `sponsored-articles`

## Quy tắc dùng category mới

### Rule 1: 1 bài chỉ nên có 1 topical pillar chính

Không tiếp tục nhét 1 bài vào nhiều category rộng cùng lúc kiểu:

- `crypto`
- `market`
- `news`

Mỗi bài nên có:

- 1 pillar chính
- nếu cần thì 1 subcategory dưới pillar đó
- chỉ thêm `news` khi bài đó là fast-turn reporting đúng nghĩa

### Rule 2: Brand / token / company không nên là category core

Các topic như:

- Bitcoin
- Ethereum
- Tether
- Binance
- Coinbase

nên chuyển vai trò dần sang:

- tag
- topic page
- author-chosen entities trong bài

không nên tiếp tục là category trung tâm của site.

### Rule 3: Press release và sponsored phải tách rõ

- `press-release` dùng cho nội dung phát hành công bố
- `sponsored-articles` dùng cho nội dung commercial / partner

Không cho các bài này chui vào cùng taxonomy pillar với editorial nếu không có reason thật rõ.

### Rule 4: `news` là stream, không phải pillar

Nếu muốn giữ:

- `/news/`
- `/news/feed/`

thì coi `news` như archive cho breaking/reporting stream.

Các bài deep-dive, explainers, protocol analysis không bắt buộc phải nằm trong `news`.

## Slug list nên tạo trong WP

### Top-level

- `protocols`
- `yield`
- `liquidity`
- `risk`
- `infrastructure`
- `sponsored-articles`

### Child categories

- `dex`
- `lending`
- `derivatives`
- `stablecoins`
- `governance`
- `staking`
- `farming`
- `strategies`
- `pools`
- `capital-flows`
- `amm`
- `exploits`
- `liquidations`
- `smart-contracts`
- `oracles`
- `bridges`
- `layer2`

## Mapping category cũ sang category mới

Đây là mapping thực dụng cho current site.

| Current category | Count | Hành động | Target / ghi chú |
| --- | ---: | --- | --- |
| `crypto` | 832 | giữ tạm, dừng dùng cho bài mới | remap dần sang 5 pillar |
| `market` | 88 | giữ tạm, dừng dùng cho bài mới | remap sang `yield`, `liquidity`, `risk` tùy intent |
| `blockchain` | 113 | giữ tạm, dừng dùng cho bài mới | remap sang `infrastructure` hoặc `protocols` |
| `news` | 104 | giữ | chỉ dùng cho breaking/reporting stream |
| `press-release` | 9 | giữ | bucket riêng, không trộn editorial |
| `blockchain-event` | 8 | dừng mở rộng | nếu là event recap thì map sang pillar phù hợp, nếu chỉ announcement thì cân nhắc `press-release` |
| `projects` | 2 | gộp dần | thường map sang `protocols` |
| `cmc` | 0 | không dùng | để rỗng hoặc xóa sau |
| `uncategorized` | 2 | dọn ngay | gán lại category chuẩn rồi làm count = 0 |
| `bitcoin` | 477 | không dùng cho bài mới | chuyển dần thành tag/topic, bài thì map theo intent thật |
| `ethereum` | 159 | không dùng cho bài mới | chuyển dần thành tag/topic |
| `tether` | 17 | không dùng cho bài mới | thường map sang `protocols/stablecoins` hoặc tag |
| `binance` | 53 | không dùng cho bài mới | thường là tag/entity; bài map theo intent |
| `coinbase` | 9 | không dùng cho bài mới | thường là tag/entity; bài map theo intent |
| `business` | 195 | dừng dùng cho bài mới | map tùy bài: `protocols`, `yield`, `liquidity`, `risk` |
| `trading` | 7 | dừng dùng cho bài mới | thường map sang `liquidity` hoặc `risk` |
| `money` | 4 | dừng dùng cho bài mới | map theo intent thật |
| `investor` | 2 | dừng dùng cho bài mới | thường tag, không cần category |
| `forex` | 5 | dừng dùng cho bài mới | thường không fit core; nếu giữ thì tag |
| `mining` | 27 | dừng dùng cho bài mới | nếu không phải core DeFi thì hạ xuống tag hoặc stream phụ |
| `nft` | 6 | dừng dùng cho bài mới | nếu không phải core DeFi thì tag hoặc stream phụ |
| `stocks` | 17 | dừng dùng cho bài mới | không phải core DeFi; nên giảm prominence |

## Mapping theo intent bài viết

Đây là rule quan trọng nhất khi remap bài cũ:

### Nhóm protocol / product

- DEX launches / upgrades -> `protocols/dex`
- Lending markets / vault mechanics -> `protocols/lending`
- Perps / options / leverage venues -> `protocols/derivatives`
- Stablecoin issuance / collateral / peg design -> `protocols/stablecoins`
- DAO votes / token governance / treasury motions -> `protocols/governance`

### Nhóm yield

- staking yields / validator economics -> `yield/staking`
- LP farming / emissions / incentives -> `yield/farming`
- vault rotations / basis / carry / structured yield -> `yield/strategies`

### Nhóm liquidity

- pool launches / TVL / depth changes -> `liquidity/pools`
- flows between chains / exchanges / protocols -> `liquidity/capital-flows`
- AMM design / rebalancing / fee dynamics -> `liquidity/amm`

### Nhóm risk

- hacks / drains / compromise reports -> `risk/exploits`
- leverage unwinds / cascades -> `risk/liquidations`
- audit issues / code risk / governance risk from contracts -> `risk/smart-contracts`

### Nhóm infrastructure

- oracle changes / price feed incidents -> `infrastructure/oracles`
- bridge launches / bridge exploits / interoperability rails -> `infrastructure/bridges`
- L2 migration / rollup infra / execution scaling -> `infrastructure/layer2`

## Menu structure nên dùng

### Primary nav

1. Home
2. News
3. Protocols
4. Yield
5. Liquidity
6. Risk
7. Infrastructure
8. Press Release

### Submenu đề xuất

#### Protocols

- DEX
- Lending
- Derivatives
- Stablecoins
- Governance

#### Yield

- Staking
- Farming
- Strategies

#### Liquidity

- Pools
- Capital Flows
- AMM

#### Risk

- Exploits
- Liquidations
- Smart Contracts

#### Infrastructure

- Oracles
- Bridges
- Layer 2

### Không nên để nổi ở primary nav

- Crypto
- Market
- Blockchain
- Bitcoin
- Ethereum
- Binance
- Coinbase
- Mining
- Stocks
- CMC

## Homepage structure nên đổi theo category mới

Trên homepage, các section chính nên xoay quanh 5 pillar mới thay vì:

- Market News
- Crypto News

Khung hợp lý hơn:

1. Latest News
2. Protocols
3. Yield
4. Liquidity
5. Risk
6. Infrastructure
7. Press Release

Nếu muốn giữ `News` ở homepage, chỉ nên dùng như:

- latest reporting stream
- not as substitute for topical architecture

## Rollout plan an toàn

Site đang tăng index mạnh, nên không thay toàn bộ taxonomy trong một lần.

### Wave 1: tạo khung mới

1. Tạo toàn bộ category mới trong WP
2. Viết description ngắn cho 5 pillar
3. Đưa 5 pillar mới vào menu
4. Sửa homepage blocks sang URL category mới
5. Từ thời điểm này, bài mới chỉ dùng category mới

### Wave 2: remap bài mạnh

1. Chọn 30-50 bài mạnh nhất
2. Gán lại category theo intent thật
3. Sửa internal link trong các bài cornerstone để trỏ sang pillar mới
4. Theo dõi index/impression của category mới trong GSC

### Wave 3: dọn legacy

1. Dừng hoàn toàn việc gán bài mới vào `crypto`, `market`, `blockchain`
2. Làm count của `uncategorized` về 0
3. Gộp dần các category asset/brand thành tag/topic
4. Chỉ khi category mới đã có lực thì mới noindex, merge, hoặc redirect category cũ

## Việc nên làm ngay

1. Tạo 5 pillar + toàn bộ subcategory
2. Giữ `news` và `press-release`, chưa đụng `crypto` / `market` / `blockchain`
3. Sửa menu theo kiến trúc mới
4. Sửa homepage sang section mới
5. Chọn batch remap đầu tiên gồm:
   - `business`
   - `bitcoin`
   - `ethereum`
   - `binance`
   - `tether`

Lý do:

- đây là các bucket đang hút nhiều bài nhất
- nếu tiếp tục để nguyên, topical signal của site sẽ vẫn rất rộng và loãng

## Việc chưa nên làm ngay

- xóa hàng loạt category cũ
- redirect hàng loạt archive cũ
- ép toàn bộ 800+ bài trong `crypto` sang category mới trong một lượt

## Definition of done cho wave đầu

Wave đầu được xem là đạt khi:

- category mới đã tồn tại đầy đủ
- menu và homepage đã trỏ sang category mới
- bài mới không còn vào `crypto`, `market`, `blockchain`
- `uncategorized` về 0
- đã remap ít nhất 30 bài mạnh sang kiến trúc mới

## Kết luận cuối

Nếu mục tiêu là biến Defiliban thành site DeFi protocol deep-dive specialist, thì trọng tâm không phải là xóa category cũ thật nhanh.

Trọng tâm đúng là:

1. dựng taxonomy mới thật rõ
2. dùng taxonomy mới cho bài mới ngay lập tức
3. remap dần các bài mạnh nhất
4. chỉ dọn legacy sau khi category mới đã có tín hiệu index và internal authority
