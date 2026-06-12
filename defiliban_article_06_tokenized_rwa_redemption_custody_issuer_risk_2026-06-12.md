---
title: "What Redemption, Custody, and Issuer Risk Look Like in Tokenized RWA Products"
slug: "what-redemption-custody-and-issuer-risk-look-like-in-tokenized-rwa-products"
meta_title: "Tokenized RWA Risk: Redemption, Custody, and Issuer Risk Explained"
meta_description: "Tokenized RWA products can look safe because they are backed by Treasuries or money market assets, but users still need to understand redemption conditions, custody stack dependence, and issuer or legal-structure risk."
category: "Risk"
lane: "RWA / Tokenization"
format: "Trust / Risk Explainer"
target_keywords:
  - "tokenized RWA risk"
  - "redemption risk tokenized assets"
  - "custody risk tokenized treasuries"
  - "issuer risk tokenized RWA"
  - "tokenized treasury redemption and custody"
---

# What Redemption, Custody, and Issuer Risk Look Like in Tokenized RWA Products

Tokenized RWA products can look safer than many crypto-native assets because they are linked to Treasuries, money market funds, or other real-world instruments. But that surface-level comfort often hides the real risk map.

The main question is not only whether an asset is "backed."

The more important questions are:

1. how do you actually get out?
2. who sits in the custody and recordkeeping stack?
3. what legal claim does the token really give you?

As of **June 2026**, that is where the quality gap between tokenized RWA products becomes easier to see.

![Editorial explainer diagram showing the three main risk layers in tokenized RWA products: redemption risk, custody and service-provider risk, and issuer or legal-structure risk, with concrete examples of what users should check before treating a tokenized asset as cash-like or low risk.](assets/rwa/tokenized-rwa-risk-redemption-custody-issuer-diagram-2026-06-12.png)

*Editorial explainer: tokenized RWA risk usually sits in the exit path, custody stack, and legal structure more than in the marketing phrase "backed by real-world assets."*

> **Summary callout:** The most common mistake in tokenized RWA analysis is to treat "onchain" as if it removes offchain dependence. It does not. A token may move onchain 24/7 while redemption still depends on issuer rules, fund windows, transfer agents, custodians, and investor eligibility.

## Quick Answer

If you only need the short version, this is it:

Tokenized RWA risk usually shows up in three places:

1. **redemption risk**: whether users can actually exit at par, in what size, on what timetable, and under what conditions
2. **custody and service-provider risk**: whether the product depends on transfer agents, custodians, wallet approval systems, banks, fund administrators, or exchange partners that can interrupt operations
3. **issuer and legal-structure risk**: whether the token is a fund share, a note, a claim on a specific vehicle, or some other wrapper with different legal rights

Those three layers matter more than the headline claim that a product is backed by Treasuries or cash-like assets.

One distinction should come early: **transferability is not the same as redeemability**. A token may be easy to move between approved wallets while still having tighter limits, windows, or eligibility rules around primary redemption.

Another distinction also matters: **self-custody of the token is not the same as self-custody of the underlying asset**. In most tokenized RWA products, the real-world assets are still held and serviced through offchain institutions.

## Best Fit / Not Ideal For

**Best fit for:**

1. readers comparing tokenized Treasury and money market products on trust and operating risk
2. treasury teams deciding whether a tokenized RWA product is cash-like enough for working capital
3. DeFi users trying to understand why some RWA tokens are useful collateral but not true stablecoin substitutes
4. analysts who want a practical framework for redemption and legal-structure risk

**Not ideal for:**

1. readers looking for a simple APY ranking
2. users assuming every tokenized Treasury product behaves like an open retail stablecoin
3. anyone looking for a purely tax-focused or jurisdiction-specific legal memo

## Tokenized RWA Risk at a Glance

| Risk layer | What to check | Why it matters | Concrete examples |
| --- | --- | --- | --- |
| Redemption risk | minimum size, timing, investor eligibility, settlement asset, instant-capacity limits | a product can be money-good in theory but operationally hard to exit | OUSG instant minimum **$5,000**; non-instant redemption minimum **$50,000**. USYC minimum investment **$100,000**; redemptions above instant capacity settle **T+0** or **T+1** |
| Custody and service-provider risk | transfer agent role, wallet approval, underlying custodian, banking or exchange dependencies | tokenized ownership still relies on offchain institutions and record systems | Franklin's prospectus says the transfer agent maintains the official ownership record via a blockchain-integrated system; OUSG routes deposited USDC to the fund's Coinbase account |
| Issuer and legal-structure risk | is the token a fund share, note, share class, or other claim; who can hold it; what rights exist | different structures create different rights in redemption, transfer, and insolvency-style scenarios | USYC is a tokenized money market fund for eligible non-U.S. persons; OUSG is a qualified-access product; USDY is a tokenized note for qualifying non-U.S. investors |
| Secondary liquidity risk | whether trading venues or counterparties exist beyond issuer redemption | onchain transfer alone does not guarantee deep exit liquidity | BENJI supports peer-to-peer transfer, but that is not the same as guaranteed wide market depth |

## Key Takeaways

1. Tokenized RWA risk is usually less about wild price volatility and more about operational exit design.
2. "Backed by Treasuries" is useful, but it does not answer who can redeem, how fast, in what size, and through which service providers.
3. The custody stack matters because the underlying assets, official records, and permissioned wallet systems often remain offchain-first even when token movement is onchain.
4. Legal structure matters because a tokenized fund share, a tokenized note, and a stablecoin-like wrapper do not give the same rights.
5. The strongest products are usually the ones that make all three layers legible: redemption, custody, and issuer structure.

## Why "Backed by Real Assets" Is an Incomplete Risk Framework

The phrase "real-world asset" often makes users think the hard part is solved.

It is not.

In practice, tokenization compresses distribution, transfer, and sometimes settlement. It does **not** remove:

1. investor onboarding and compliance gates
2. transfer-agent dependence
3. fund or note documentation
4. custody arrangements
5. redemption windows, cutoffs, and capacity limits

That is why the right trust question is not "is the backing real?"

It is: **what path takes me from token in wallet to dollars in hand, and what can block that path?**

## 1. Redemption Risk: The Exit Path Is a Product Feature

The first real risk layer is redemption.

If a product claims Treasury or money market backing, users naturally assume the path back to cash should be straightforward. But the operating details can vary a lot.

### Redemption risk is about more than whether redemption exists

Users should ask:

1. who is allowed to redeem directly?
2. what is the minimum size?
3. is redemption instant, same day, or subject to the next NAV cycle?
4. do redemptions happen in fiat, stablecoins, or both?
5. are there instant-liquidity thresholds or queues?

These are not edge-case details. They determine whether a tokenized RWA product behaves like a cash management tool, a restricted fund token, or a slower institutional wrapper.

### Example: OUSG makes the operating model explicit

Ondo's OUSG docs are useful because they make several constraints clear.

Ondo says OUSG offers instant, 24/7 minting and redemption for supported flows, but it also states:

1. the instant transaction minimum is **$5,000** for both investments and redemptions
2. for non-instant transactions, the minimum investment is **$100,000**
3. for non-instant transactions, the minimum redemption is **$50,000**
4. access is limited to investors eligible for its Qualified Access Funds and who complete onboarding

That is a strong product for qualified users, but it is not the same thing as an open retail dollar token with universal same-size access.

Ondo also provides a concrete operating example: if a user deposits **100,000 USDC**, the smart contract determines the OUSG amount based on NAV and routes the USDC to the fund's Coinbase account to purchase the underlying holdings.

That one workflow already shows all three risk layers:

1. redemption and issuance depend on product rules
2. underlying movement depends on service providers
3. the token sits on top of a fund structure rather than replacing it

### Example: USYC shows that near-instant does not mean unlimited instant

Circle's USYC page is another good example because it is very specific.

Circle describes USYC as a tokenized money market fund designed to provide institutional-grade, yield-bearing collateral. It also says:

1. the minimum investment is **$100,000**
2. USYC is available only to **eligible non-U.S. persons**
3. subscriptions and redemptions are conducted in **USDC**
4. redemptions below the instant-redemption capacity settle in **one block time**
5. redemptions above the instant-redemption capacity settle **T+0** or **T+1**

That is a good example of why users should separate **liquidity quality** from **liquidity marketing**.

USYC may be fast and useful for institutions, but the terms still tell you that speed is partly capacity-dependent and access-dependent.

### Example: BENJI shows why transfer and redemption are separate questions

Franklin Templeton's onchain fund materials are especially useful here because they reveal a more traditional fund logic underneath tokenized rails.

The Franklin OnChain U.S. Government Money Fund prospectus says:

1. shares can be purchased or redeemed through the app or institutional web portal on business days
2. requests are processed at the next calculated NAV
3. the fund's NAV is calculated on business days

At the same time, Franklin has emphasized in public materials that BENJI supports peer-to-peer transferability, near-instant settlement, and daily dividend distribution.

Those things can all be true together.

That is the point.

The token may move quickly, but the fund redemption process still follows a governed structure. That makes BENJI operationally advanced, but not identical to an always-open primary redemption stablecoin.

### What users miss most: primary redemption and secondary liquidity are not the same

A tokenized RWA product can have:

1. a credible primary redemption path with the issuer
2. limited direct access to that path
3. some degree of secondary transferability
4. uneven real market depth in secondary venues

This is exactly why users should not treat "tokenized" and "liquid" as synonyms.

## 2. Custody Risk: Onchain Ownership Still Depends on Offchain Institutions

The second risk layer is custody and service-provider dependence.

Many tokenized RWA products create the impression that blockchain ownership has replaced traditional financial plumbing.

In reality, it usually sits on top of that plumbing.

### Custody risk is not only about losing a wallet key

In tokenized RWA products, custody risk can mean:

1. the underlying asset custodian
2. the transfer agent that maintains the official ownership record
3. the approved-wallet framework that determines who can hold or receive tokens
4. the banking or exchange partner used for subscriptions and redemptions
5. the administrator, accountant, or other fund service providers that keep the product operational

So even if token transfers happen on a public blockchain, users are still exposed to an offchain operating stack.

### Franklin's prospectus is one of the clearest examples

The Franklin OnChain U.S. Government Money Fund prospectus says the fund's transfer agent maintains the official record of share ownership through a **proprietary blockchain-integrated system** that uses features of traditional book-entry form and public blockchain networks.

That matters because it tells users several things at once:

1. the blockchain is part of the system of record, but not the whole governance layer
2. the transfer agent remains central to the authoritative ownership record
3. public-wallet behavior does not mean the system is fully permissionless

The same prospectus also says:

1. only wallets created by or approved by the transfer agent are authorized to purchase, redeem, receive, hold, or transfer fund shares
2. for transfer-agent-hosted wallets, the private key is held by the transfer agent
3. for investor-managed wallets, the investor or third-party wallet custodian may hold the key, but the wallet still requires transfer-agent approval
4. disruption across fund accountants, custodians, sub-custodians, or transfer agents could impair functionality or prevent investors from purchasing, redeeming, or transferring shares

This is exactly what serious custody analysis looks like.

The token is onchain. The risk stack is still institutional.

### OUSG shows service-provider dependence in a simpler way

Ondo's docs explain that deposited USDC for OUSG is routed to the fund's Coinbase account and then used to purchase the underlying holdings.

That does not mean Coinbase is the risk story by itself.

It means users should think in layers:

1. smart contract layer
2. issuer and fund layer
3. banking, exchange, and settlement partner layer

If any of those layers is constrained, the user experience can change fast even if the token itself keeps moving onchain.

### The real custody lesson

Tokenized RWA products often improve **visibility** and **programmability** more than they eliminate **intermediation**.

That is still valuable.

It just means users should not confuse better rails with no rails.

## 3. Issuer and Legal-Structure Risk: Not Every RWA Token Gives the Same Claim

The third layer is issuer and legal structure.

This is where many comparisons become misleading, because users often group together:

1. tokenized fund shares
2. tokenized notes
3. tokenized money market products
4. stablecoin-adjacent dollar-yield wrappers

These can look similar in a dashboard and still carry meaningfully different rights.

### Legal structure changes what the token actually is

Users should ask:

1. is the token a direct fund share, a beneficial interest, a note, or a wrapper around another claim?
2. who is the issuer?
3. what documents govern transfer and redemption?
4. who is allowed to hold the product?
5. what happens if the issuer, administrator, or service providers fail?

That last question is especially important because users often translate "backed by Treasuries" into "low legal risk."

Those are not the same thing.

### Example: USYC is a tokenized money market fund, not a generic dollar token

Circle is very clear that USYC is a tokenized money market fund. It is also clear that the product is available only to eligible non-U.S. persons and that additional eligibility restrictions may apply.

That immediately tells users:

1. this is not designed as a universal retail payment token
2. legal access conditions are part of the product itself
3. redemption and transfer behavior should be read through a fund-access lens

### Example: OUSG is a qualified-access product

Ondo's docs say investors must be eligible for its Qualified Access Funds and complete onboarding. Ondo's eligibility materials further explain that investors generally need to satisfy both **accredited investor** and **qualified purchaser** criteria for the relevant fund access path.

That creates a very different legal and operational profile from a broad stablecoin.

It may still be a strong institutional product. But the product's usefulness depends on understanding that it is a qualified-access Treasury exposure, not just a token with yield.

### Example: USDY shows why not every Treasury-linked token is a fund share

Ondo's USDY materials are helpful because they show a different structure again.

Ondo describes USDY for qualifying non-U.S. individual and institutional investors and distinguishes between:

1. **USDY**, an accumulating token
2. **rUSDY**, a rebasing token that keeps a **$1.00** price

That is a reminder that token mechanics and legal structure interact.

Two products can both be Treasury-linked and still behave differently in:

1. accounting treatment
2. price behavior
3. transfer integration
4. user expectations around redemption and ownership

## What This Looks Like in Real Operating Terms

The easiest way to understand tokenized RWA risk is to compare how different products make different tradeoffs.

### Model 1: Institutional speed with explicit gating

OUSG is strong when the user values:

1. clear instant and non-instant lanes
2. Treasury-heavy exposure
3. USDC-based subscription and redemption
4. 24/7 tokenized operations for qualified users

It is less ideal if the user assumes:

1. universal retail access
2. no onboarding burden
3. any-size redemption at any time with no constraints

### Model 2: Collateral-first money market utility

USYC is strong when the user values:

1. institutional-grade collateral design
2. integration with USDC workflows
3. near-instant redemption below capacity thresholds
4. short-term government-security backing

It is less ideal if the user assumes:

1. open retail availability
2. unlimited instant liquidity
3. identical behavior to a plain stablecoin balance

### Model 3: Transfer-rich onchain fund structure

BENJI is strong when the user values:

1. peer-to-peer transferability
2. regulated fund structure
3. smart-contract and wallet integration
4. a documented recordkeeping system tied to transfer-agent controls

It is less ideal if the user assumes:

1. fully permissionless wallet behavior
2. direct redemption that ignores NAV timing and fund windows
3. no transfer-agent or service-provider dependence

## What Users Usually Miss When They Call All RWAs "Safe"

The category can be genuinely safer than many crypto-native products on market-risk grounds.

But "safer" is not the same as "simple."

Users usually underestimate five things:

1. **gated access risk**: the product may be high quality but not open to them
2. **workflow risk**: the exit path may be slower or more conditional than the token UX suggests
3. **service-provider concentration**: one transfer agent, custodian, or settlement partner can matter a lot
4. **legal-claim complexity**: a token may represent a specific class of exposure, not generalized ownership of cash-like assets
5. **capacity mismatch**: a product may work well for treasury parking or collateral use but poorly for unpredictable payment needs

This is why tokenized RWA products should usually be evaluated as **capital-management tools** first, and only sometimes as **cash substitutes**.

## A Simple Decision Framework

If you want to judge whether a tokenized RWA product is operationally strong enough for your use case, ask these eight questions.

### 1. Who can redeem directly?

If only a narrow class of approved investors can redeem, that changes how much the product behaves like a general cash instrument.

### 2. What are the size thresholds?

Minimums often tell you who the product is really designed for. A product with a **$100,000** minimum is making a very different market choice from one with smaller operational thresholds.

### 3. Is redemption truly instant, or only instant up to capacity?

This distinction matters a lot in treasury planning and stress periods.

### 4. What asset do you receive when you exit?

USDC redemption, fiat redemption, and fund-share transfer are not interchangeable outcomes.

### 5. Who controls the authoritative ownership record?

If a transfer agent or approved-wallet framework controls the official record, users should treat that as a core dependency.

### 6. What kind of token is this legally?

Fund share, note, wrapper, and rebasing share class are not cosmetic differences.

### 7. How many institutions sit in the operating path?

The more critical partners involved in custody, banking, exchange settlement, administration, or recordkeeping, the more important operational resilience becomes.

### 8. Is this product best used as cash, collateral, or parked capital?

A lot of confusion disappears when the user is honest about the use case.

### Practical rule of thumb

Tokenized RWA products are strongest when:

1. redemption terms are explicit
2. the custody and recordkeeping stack is legible
3. the legal claim is clear
4. the product's constraints match the intended use case
5. the user does not expect the token to behave like unrestricted retail cash if it was not built for that job

They are weaker when:

1. redemption sounds faster in marketing than it looks in documentation
2. the service-provider stack is hidden or hand-waved
3. transferability is used to blur over eligibility or custody constraints
4. users do not know what the token actually represents in legal terms

## Bottom Line

Redemption, custody, and issuer risk are the real operating core of tokenized RWA products.

That does not make the category weak.

It makes the category legible.

The strongest tokenized RWA products are not the ones that merely say "backed by Treasuries." They are the ones that make the path from token to claim to exit understandable enough that users know exactly what kind of instrument they are holding.

In **2025-2026**, that is where the category has matured: from proving that assets can be tokenized to proving that tokenized ownership can be trusted under real operating conditions.

## FAQ

### Are tokenized Treasury products basically the same as stablecoins?

No. Some may feel stablecoin-adjacent, but many are fund shares, money market interests, or notes with different redemption rules, investor restrictions, and legal claims.

### Why does redemption risk matter if the underlying assets are high quality?

Because users experience products through the exit path, not through the marketing description of the underlying portfolio.

### If I self-custody the token, am I self-custodying the underlying asset?

Usually no. In most tokenized RWA structures, the underlying assets remain in offchain custody or fund structures handled by institutional service providers.

### Why is transferability not enough?

Because a token can be easy to transfer between approved wallets and still have restricted primary redemption, limited secondary depth, or heavy onboarding requirements.

### What is the single best first check?

Read the redemption mechanics and investor eligibility before looking at APY.

## Source Notes

The analysis above is based primarily on official materials from:

1. [Ondo: OUSG overview](https://docs.ondo.finance/qualified-access-products/ousg)
2. [Ondo: OUSG eligibility](https://docs.ondo.finance/qualified-access-products/eligibility)
3. [Ondo: OUSG onboarding and KYC](https://docs.ondo.finance/qualified-access-products/onboarding-and-kyc)
4. [Ondo: USDY basics](https://docs.ondo.finance/general-access-products/usdy/basics)
5. [Circle: USYC](https://www.circle.com/usyc)
6. [Circle blog: Tokenized Money Market Funds 101, published November 18, 2025](https://www.circle.com/blog/tokenized-money-market-funds-101-liquidity-meets-yield)
7. [Franklin Templeton press release on BENJI, April 30, 2026](https://www.franklintempleton.com/press-releases/news-room/2026/franklin-templeton-stellar-development-foundation-mark-five-years-of-benji-the-first-u.s.-registered-tokenized-money-market-fund)
8. [Franklin OnChain U.S. Government Money Fund prospectus](https://www.franklintempleton.com/forms-literature/download-preview/9001-P)

## Suggested Internal Links

1. Target: `Why Tokenized Treasuries Are Becoming a Default Yield Layer for On-Chain Capital`
Anchor: `tokenized treasuries` or `default yield layer`
Best placement: in sections explaining why operational quality matters more as the category matures

2. Target: `What Reserve Transparency Really Tells Users About a Stablecoin Issuer`
Anchor: `backing and redemption risk` or `trust framework`
Best placement: in sections comparing stablecoin reserve logic with tokenized RWA legal-structure and redemption analysis

3. Target: `Why Yield-Bearing Stablecoins Are Becoming a New DeFi Battleground`
Anchor: `yield-bearing stablecoins` or `productive dollar balances`
Best placement: in sections distinguishing tokenized RWA products from stablecoin-adjacent yield instruments

4. Target: `How Users Are Actually Using USDC and USDT for Real Payment Workflows`
Anchor: `real payment workflows` or `payment stablecoins`
Best placement: in sections explaining why payment balances and parked capital often need different products
