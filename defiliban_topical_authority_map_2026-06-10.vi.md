# Defiliban Topical Authority Map

Ngày: 2026-06-10

## Mục tiêu

Tài liệu này chốt 4 việc:

- topical authority chính của Defiliban nên xoay quanh gì
- cấu trúc 3 tầng: `pillar -> cluster -> everyday-life angle`
- nhóm nào nên ưu tiên build trước
- internal link flow nên đi như nào để authority dồn đúng chỗ

## Thesis

Defiliban không nên cố thành một site finance quá rộng.

Defiliban nên build theo hướng:

- `DeFi protocol deep-dive specialist`
- có thêm lớp `real-life utility`
- nhưng utility phải luôn quay về:
  - stablecoins
  - payments
  - self-custody
  - yield
  - risk
  - infrastructure

## 5 Pillars Chính

1. `Protocols`
2. `Yield`
3. `Liquidity`
4. `Risk`
5. `Infrastructure`

Đây là trục authority chính.

`News` chỉ là stream / fallback.

`Press Release` là bucket thương mại, không tính là editorial pillar.

## Tầng 1 -> Tầng 2 -> Tầng 3

### 1. Protocols

#### Tầng 2: Core clusters

- `DEX`
- `Lending`
- `Derivatives`
- `Stablecoins`
- `Governance`

#### Tầng 3: Everyday-life angles

- best ways people actually swap on-chain
- how lending markets affect borrowers and savers
- what stablecoins people use for day-to-day value storage
- how DAO votes affect users, fees, rewards, or access
- what a new protocol launch changes for normal users

#### Content lane examples

- explainers
- protocol comparison
- product update impact
- governance outcome summaries
- tokenomics change breakdowns

### 2. Yield

#### Tầng 2: Core clusters

- `Staking`
- `Farming`
- `Strategies`

#### Tầng 3: Everyday-life angles

- where people park idle stablecoins
- how users think about passive on-chain income
- what APY actually means after fees and token emissions
- how to compare staking vs farming vs vaults
- how yield products fail and what users lose

#### Content lane examples

- APY explainers
- staking strategy guides
- reward cut / incentive update coverage
- vault risk breakdowns
- yield comparison pages

### 3. Liquidity

#### Tầng 2: Core clusters

- `Pools`
- `Capital Flows`
- `AMM`

#### Tầng 3: Everyday-life angles

- why users get better or worse execution
- how liquidity moves affect token prices and slippage
- what pool depth means for traders and LPs
- how cross-chain flows change where users deploy capital
- how AMM mechanics affect normal swap behavior

#### Content lane examples

- TVL / flow analysis
- AMM explainer
- pool migration stories
- liquidity fragmentation stories
- slippage / execution quality guides

### 4. Risk

#### Tầng 2: Core clusters

- `Exploits`
- `Liquidations`
- `Smart Contracts`

#### Tầng 3: Everyday-life angles

- how people lose funds in wallet or contract interactions
- what liquidation means for leveraged users
- how approval risks and malicious contracts work
- how to assess smart contract risk before depositing
- what users should do after a protocol incident

#### Content lane examples

- exploit reports
- post-mortem explainers
- liquidation education
- wallet safety guides
- approval / revoke guides

### 5. Infrastructure

#### Tầng 2: Core clusters

- `Oracles`
- `Bridges`
- `Layer 2`

#### Tầng 3: Everyday-life angles

- how people move money across chains
- what bridge risk means in practice
- why fees change between chains
- how oracle failures affect borrowers, traders, and LPs
- why users care about layer-2 speed and cost

#### Content lane examples

- bridge explainers
- chain migration stories
- oracle incident coverage
- L2 adoption stories
- cost / speed comparison pages

## Real-Life Utility Lanes Defiliban Có Thể Chạy

Các lane này chạy được vì vẫn nằm trong trục DeFi:

### 1. Stablecoin Payments

- paying freelancers in USDC
- cross-border payments
- settlement speed
- merchant adoption
- payroll / remittance angle

Map chủ yếu vào:

- `Protocols`
- `Infrastructure`
- `News`

### 2. Preserving Value

- stablecoins as cash alternative
- tokenized gold only when crypto angle rõ
- depeg risk
- treasury / reserve transparency

Map chủ yếu vào:

- `Protocols`
- `Risk`

### 3. On-Chain Income

- staking
- farming
- vault strategies
- risk-adjusted yield

Map chủ yếu vào:

- `Yield`
- `Risk`

### 4. Self-Custody And Safety

- wallet setup
- seed phrase risk
- phishing
- malicious approvals
- bridge and contract safety

Map chủ yếu vào:

- `Risk`
- `Infrastructure`

### 5. Retail DeFi Usage

- how users swap
- how users borrow
- how users bridge
- how users avoid liquidation

Map chủ yếu vào:

- `Protocols`
- `Liquidity`
- `Risk`

## Không Nên Build Thành Lane Chính

Các nhóm dưới đây không nên là lane authority chính của Defiliban:

- gold rate today
- gold price today
- silver price today
- nse / sensex / nifty generic
- stock price lookup
- local consumer finance utility
- personal finance chung chung
- commodity news không có crypto angle

Nếu dùng được thì chỉ là:

- `conditional coverage`
- có crypto / DeFi angle rất rõ

## Priority Build Order

### Wave 1: authority core

Ưu tiên build ngay:

1. `Protocols`
2. `Risk`
3. `Yield`

Lý do:

- sát định vị nhất
- dễ tạo cluster rõ nhất
- có nhiều intent evergreen + news
- giúp site khác biệt hơn generic crypto news

### Wave 2: market structure depth

Tiếp theo:

4. `Liquidity`
5. `Infrastructure`

Lý do:

- mạnh về chuyên môn
- hỗ trợ topical depth
- tạo khác biệt so với site chỉ đăng tin

### Wave 3: life-utility layer

Chỉ thêm mạnh sau khi wave 1-2 có nền:

- stablecoin payments
- on-chain savings / preserving value
- self-custody safety
- remittance / global payouts

## Hub And Cluster Model

Mỗi pillar nên có:

- `1 hub archive/category`
- `3-5 cluster pages`
- `10-30 supporting articles`

### Ví dụ tối thiểu

#### Protocols

- hub: `/protocols/`
- clusters:
  - DEX
  - Lending
  - Stablecoins
  - Governance

#### Risk

- hub: `/risk/`
- clusters:
  - Exploits
  - Liquidations
  - Smart Contracts

#### Yield

- hub: `/yield/`
- clusters:
  - Staking
  - Farming
  - Strategies

## Internal Link Flow

Internal links nên đi theo logic authority, không random.

### Flow 1: hub -> cluster

- pillar page link xuống cluster quan trọng nhất
- cluster intro block link sang 3-5 bài mạnh nhất

### Flow 2: cluster winners -> near-win pages

- bài nào bắt đầu có rank / impression / traffic
- dùng nó làm source page để đẩy các bài cùng cluster đang ở vị trí 5-10

### Flow 3: everyday-life pages -> core cluster

- bài utility không nên đứng một mình
- phải link về:
  - cluster page
  - pillar hub
  - 1-2 explainer nền tảng

### Flow 4: risk pages receive links sitewide

Các bài:

- exploit
- liquidation
- self-custody safety

nên được link từ nhiều cluster khác vì đây là nơi người dùng và Google đều quan tâm.

## Content Mix Khuyên Dùng

Cho mỗi pillar:

- `30%` news / fast updates
- `40%` explainers / breakdowns
- `20%` comparisons / strategic guides
- `10%` glossary / utility / evergreen support

Nếu Defiliban chỉ đẩy news:

- authority sẽ mỏng
- khó thành specialist site

Nếu Defiliban chỉ đẩy evergreen:

- sẽ thiếu freshness và crawl attention

## 30 Ngày Tới Nên Làm Gì

1. Chốt 3 pillar đầu:
   - Protocols
   - Risk
   - Yield
2. Với mỗi pillar, chọn 10 bài tốt nhất hiện có để remap / gom cụm
3. Tạo 1 list 20 headline mới cho mỗi pillar
4. Viết 3-5 bài explainer nền:
   - one per cluster chính
5. Từ bài mới, link ngược về pillar hub và cluster liên quan
6. Track xem bài mới đang dồn nhiều vào `News` quá không

## Definition Of Done

Defiliban bắt đầu có topical authority thật khi:

- bài mới không còn rơi chủ yếu vào `News`
- 5 pillar có bài đều và rõ cluster
- mỗi pillar có ít nhất 1 cluster nổi bật
- các bài utility đều link ngược về core DeFi topics
- internal links bắt đầu dồn từ bài mạnh sang near-win pages cùng cụm

## Kết Luận

Defiliban xây topical authority được ngay, không cần đợi.

Nhưng phải xây theo hướng:

- `DeFi specialist first`
- `life utility second`
- `generic finance never`

Nếu phải chọn một câu duy nhất để giữ kỷ luật content, thì là:

> Mọi lane đời sống của Defiliban đều phải quay lại một vấn đề thật của người dùng trong stablecoins, DeFi usage, yield, risk, hoặc infrastructure.
