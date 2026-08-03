# 07 — Taxes & Record-Keeping

> **This chapter is educational and is not tax advice.** It covers US federal
> rules at a general level as of mid-2026. Tax law is genuinely complicated,
> changes regularly, and depends on your specific circumstances. Consult a CPA
> with securities-trading experience before making any election described here —
> particularly Section 475(f), which is difficult to reverse.

Taxes are where profitable-looking years become unprofitable ones. A trader who
nets $40,000 in gains and pays 35% on all of it as short-term income keeps
$26,000 — and that is before discovering that wash sale rules have disallowed a
chunk of the losses they expected to offset.

---

## 1. Short-term capital gains

The central fact for day traders: **every position held under one year is taxed
at short-term capital gains rates, which equal your ordinary income rate.**

There is no favorable treatment. The long-term rates (0%/15%/20%) that make
buy-and-hold investing tax-efficient require a holding period of more than one
year. By definition, day trading never qualifies.

Depending on your bracket and state, you may keep only 60–70% of gross trading
profits. Model this into any expectation you set. A strategy that returns 10%
before tax does not return 10%.

---

## 2. The wash sale rule

The rule most likely to produce an unpleasant surprise.

**A wash sale occurs when you sell a security at a loss and buy a
substantially identical security within 30 days before or after the sale** — a
61-day window centered on the sale date. The loss is **disallowed** for the
current year and added to the cost basis of the replacement position.

Why this hits day traders hard: you trade the same instruments repeatedly. Sell
SPY at a loss Tuesday, buy SPY again Thursday, and you have triggered a wash
sale. Do this all year and a large fraction of your realized losses may be
deferred.

The pathological case is real and worth understanding: a trader can finish the
year having **lost money overall** but face a **taxable gain**, because losses
were disallowed while gains were fully recognized. If the replacement position is
still open at year end, the disallowed loss carries into the following tax year
rather than offsetting the gains it economically offset.

Two mitigations:

- **Close positions and stay out for 31 days** across the year end for names
  where you are carrying losses. Awkward, but it works.
- **Elect Section 475(f) mark-to-market**, which exempts you from the wash sale
  rule entirely. See below.

Additionally, without mark-to-market, **net capital losses are limited to $3,000
per year** against ordinary income, with the remainder carried forward. A trader
who loses $40,000 deducts $3,000 this year and carries $37,000 forward. That is a
slow recovery.

---

## 3. Trader Tax Status (TTS)

The IRS distinguishes an **investor** from a **trader in securities**. TTS is not
an election you file — it is a facts-and-circumstances determination based on
your actual activity.

Factors that support TTS:

- Substantial trading **volume and frequency** — generally understood to mean
  hundreds of trades per year, executed on most available trading days.
- **Short holding periods** (days, not months).
- Intent to profit from **short-term price movements** rather than dividends or
  appreciation.
- Trading conducted with **continuity and regularity**, in a businesslike
  manner — a dedicated setup, real time commitment, documented process.

There is no bright-line test in the statute, which means the determination is
inherently uncertain and depends on documentation. **Keep records that establish
your activity level.** Your trading journal from chapter 06 is directly useful
here.

**What TTS gives you:** the ability to deduct trading-related expenses (data
feeds, platform fees, education, home office, hardware) as **business expenses**
on Schedule C, rather than as miscellaneous itemized deductions — which are
currently unavailable to investors. It is also a prerequisite for the Section
475(f) election.

**What TTS does not do:** it does not by itself change how your gains are taxed,
and it does not exempt you from wash sales. That requires the separate election
below.

---

## 4. Section 475(f) mark-to-market election

Available only to taxpayers who qualify as traders in securities. It is the most
consequential tax decision a serious day trader makes.

**What it does.** You are treated as having sold every open position at fair
market value on the last business day of the year, and repurchased it on the
first day of the new year. Trading gains and losses become **ordinary income or
loss** rather than capital gains or losses.

### Advantages

- **The wash sale rule no longer applies.** The year-end deemed sale cleans the
  slate and all losses are realized.
- **The $3,000 capital loss limitation disappears.** Losses are ordinary and can
  fully offset other ordinary income, potentially generating a net operating
  loss. For a trader with a bad year, this is a very large difference.
- Simplified accounting — no lot-by-lot wash sale tracking.

### Disadvantages

- **You lose long-term capital gains treatment entirely**, including on any
  separate long-term investment positions caught by the election. (Careful
  segregation of investment accounts matters here — discuss with your CPA.)
- **Unrealized gains at year end become taxable**, even though you have not sold
  and have received no cash to pay the tax with.
- **It is difficult to revoke.** Reversing requires IRS procedures and is not
  something to plan around.

### The deadline, which catches people every year

For an existing individual taxpayer, the election for a given tax year must
generally be filed **by the tax deadline of the *prior* year** — attached to that
return or to a timely filed extension. For a calendar-year individual electing
Section 475 for **tax year 2026**, that generally meant filing the election
statement by **April 15, 2026**. Form 3115 is generally filed for the year of
change.

**Read that again.** You must decide before the year begins, not after you know
how it went. A trader who has a terrible 2026 cannot elect mark-to-market in 2027
to rescue it. This asymmetry is the single most important practical fact in this
chapter.

(New taxpayers and newly formed entities operate under different timing rules,
which is one reason an entity structure is sometimes discussed as a path to
§475 treatment mid-stream. That is a CPA conversation, not a DIY one.)

---

## 5. Futures: Section 1256

Futures and certain other contracts receive notably favorable treatment under
**Section 1256**:

- **The 60/40 rule** — gains are treated as 60% long-term and 40% short-term
  **regardless of holding period**, producing a blended rate meaningfully below
  the pure short-term rate.
- **Marked to market annually**, so wash sale rules do not apply.
- Reported in aggregate on Form 6781 rather than trade by trade.

For a high-frequency trader, this is a substantial structural advantage over
equities and is a legitimate reason to consider index futures (including micro
contracts) instead of ETFs for equivalent exposure. It is one of the few genuine
free lunches available, and it is worth understanding before choosing your
instrument.

---

## 6. Record-keeping

Keep for at least three years (seven is safer):

- **Broker statements** — monthly and annual. Download them; do not assume your
  broker retains access indefinitely, especially if you switch firms.
- **Form 1099-B** — reports proceeds and, usually, basis and wash sale
  adjustments.
- **Your own trade log** — reconcile it against broker records. Discrepancies are
  worth finding early.
- **Expense receipts** — data feeds, platform fees, education, hardware, home
  office documentation, if claiming TTS.
- **Evidence of trading activity level** — supports a TTS position if questioned.

**Reconcile monthly, not annually.** Finding a discrepancy in January for the
prior year is painful; finding it within thirty days is routine.

### On tax software

Consumer tax software frequently handles high-volume trading poorly, especially
wash sale adjustments across accounts. Dedicated trader tax software exists, and
above a few hundred trades a year, a CPA with securities experience typically
pays for themselves. Budget for it as a cost of the business.

---

## 7. Non-US readers

Everything above is US federal law. Elsewhere differs substantially:

- **UK** — Capital Gains Tax with an annual exempt amount; spread betting is
  currently tax-free for most individuals but is a different (and leveraged)
  product. Stamp duty applies to share purchases.
- **Canada** — frequent trading may be treated as **business income** (fully
  taxable at marginal rates) rather than capital gains (50% inclusion). Day
  trading inside a TFSA has been successfully challenged by the CRA.
- **Australia** — trader vs. investor distinction affects treatment; the CGT
  discount requires a 12-month holding period.
- **Germany, India, Singapore, and others** each have distinct regimes, some far
  less favorable to frequent trading.

Consult a local professional. Do not extrapolate from US material.

---

## What to take from this chapter

1. Day trading gains are always short-term — taxed at ordinary income rates.
2. Wash sales can disallow losses and, in the worst case, produce a tax bill in a
   losing year.
3. Trader Tax Status is determined by facts, not filed as an election, and
   enables business expense deductions.
4. Section 475(f) removes wash sales and the $3,000 loss cap, but costs long-term
   treatment and **must be elected in advance** — by the prior year's deadline.
5. Futures get 60/40 treatment under Section 1256, a real structural advantage.
6. Reconcile records monthly. Hire a specialist CPA once volume is meaningful.

Next: [08 — Red Flags](08-red-flags.md)
