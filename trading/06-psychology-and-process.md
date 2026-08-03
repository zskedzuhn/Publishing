# 06 — Psychology & Process

Traders rarely fail because they lacked information. They fail because they did
not do what they had already decided to do.

The gap between knowing the rules and following them is where accounts die. This
chapter is about closing it — and the method is not willpower. It is structure.

---

## 1. Why your brain is badly suited to this

You are not weak-willed. You are running cognitive machinery that was useful for
most of human history and is actively harmful in markets.

**Loss aversion.** Losses register roughly twice as strongly as equivalent gains.
The behavioral consequence: you close winners early to secure the good feeling,
and hold losers to avoid realizing the bad one. This produces precisely the
inverted payoff ratio from chapter 01 — small wins, large losses, negative
expectancy — and it happens automatically unless something prevents it.

**The disposition effect.** The documented tendency to sell winners and ride
losers. It is one of the most robust findings in behavioral finance, and it is
loss aversion expressed in a brokerage account.

**Recency bias.** Three losses in a row and the strategy feels broken. Three wins
and you feel invincible and size up. Neither feeling contains information — both
are ordinary variance (chapter 01, section 5) being misread as signal.

**Confirmation bias.** Once positioned, you notice evidence supporting the
position and discount evidence against it. The moment you enter a trade, you stop
being a neutral analyst of it.

**The sunk cost fallacy.** "I've already lost this much, I can't sell now." The
money is gone regardless. The only question is whether this position is the best
use of remaining capital — and the answer, for a position that has violated your
stop, is no.

**Overconfidence.** Barber and Odean's broader research found that overconfident
investors trade more and earn less. Trading frequency correlates negatively with
returns. The Brazilian study reinforced this from another angle: among traders
who persisted more than 300 days, regression analysis found **no evidence of
learning through experience.** Screen time alone did not produce skill.

That last finding deserves emphasis, because the standard advice is "put in the
hours." The data says hours without structured feedback do essentially nothing.
Which brings us to the journal.

---

## 2. The trading journal

**This is the highest-leverage habit available to you.** Not a supplement to
trading — the mechanism by which trading becomes a skill rather than a repeated
activity.

The reason connects directly to the finding above. Experience produces learning
only when it generates a **feedback signal you can actually act on.** In trading,
raw outcomes are a terrible signal: good decisions lose, bad decisions win, and
the noise dominates over any short horizon. A journal separates decision quality
from outcome, which is the only way the feedback becomes usable.

### What to record

Use `tools/trade_journal_template.csv`. Per trade:

**Before entry** — setup name, instrument, thesis in one sentence, entry price,
stop, target, position size, planned R, emotional state (1–5).

**After exit** — exit price, actual R, whether you followed the plan, screenshot.

**The two fields that matter most:**

- **Process grade (A–F)** — did you follow your rules? *Graded independently of
  outcome.*
- **Mistake category** — if any: early entry, moved stop, oversized, revenge
  trade, FOMO, ignored invalidation, exited early.

### The four-quadrant review

Sort every trade into one of four boxes:

|  | Won | Lost |
|---|---|---|
| **Followed plan** | ✅ Correct. Repeat. | ✅ **Correct.** Repeat. |
| **Broke plan** | ⚠️ **Dangerous.** | ❌ Obvious error. |

The two counterintuitive cells carry the lesson.

**Followed plan + lost = a good trade.** Losses are a scheduled cost of a
positive-expectancy system. If you followed your rules, you did your job. Nothing
to fix.

**Broke plan + won = the most dangerous outcome in trading.** You were rewarded
for undisciplined behavior. The reward is a random draw; the habit it reinforces
is permanent. This is how traders acquire the exact behaviors that later destroy
them — one lucky reinforcement at a time. Flag these harder than losses.

Review weekly. Look for the recurring mistake category, not the recurring loser.
One specific behavioral fix per week beats a general resolution to "be more
disciplined."

---

## 3. The trading plan

Write it before you trade. Read it before every session. Revise it only on
weekends, never mid-session and never after a loss.

```markdown
# Trading Plan — [Your Name]

## Objective
[Specific and process-based. "Execute my plan on every trade for 90 days,"
 not "make $500/day." You control process; you do not control outcome.]

## Markets & Hours
Instruments: [e.g., SPY, QQQ only]
Trading window: [e.g., 9:45 – 11:00 am ET]
Never trade: first 15 min, lunch (11:30–1:30), scheduled news releases

## Setups (only these)
1. [Name] — context / trigger / stop / target / invalidation
2. [Name] — ...

## Risk Rules
- Max risk per trade: 1% ($___)
- Max daily loss: 3R ($___) → stop trading for the day
- Max weekly loss: 6R ($___) → stop trading for the week
- Max trades per day: 3
- Max concurrent positions: 2
- Max total open risk: 2%
- Minimum reward:risk: 2:1

## Hard Rules (never broken)
- Stop loss placed at entry, always
- Never widen a stop
- Never average down on a loser
- Never trade to recover a loss
- No trading when: angry, tired, distracted, intoxicated, ill

## Daily Routine
Pre-market: [checklist]
Session: [checklist]
Post-market: journal, grade, one improvement note

## Review
Weekly: statistics, mistake patterns, one specific fix
Monthly: full strategy review; expectancy over trailing 100 trades
```

---

## 4. The failure modes, by name

Naming these matters. You are far more likely to interrupt a pattern you can
identify in the moment.

**Revenge trading.** Trading to recover a loss rather than because a setup
appeared. The most destructive pattern in retail trading. *Defense:* the daily
loss limit, set in advance and treated as absolute.

**FOMO.** Entering because price is moving and you are not in it. Almost always
produces entry at the worst price — you buy the extension that the disciplined
trader is selling into. *Defense:* if it was not your setup at your trigger, it is
not your trade. Missed opportunity costs nothing.

**Averaging down.** Adding to a loser to improve average price. This increases
risk on a position that is demonstrating your thesis is wrong. It feels like
conviction; it is the mechanism behind most catastrophic single-position losses.
*Defense:* never add to a losing position. Non-negotiable.

**Moving the stop.** Widening a stop as price approaches it. Converts a defined
−1R into an undefined loss. *Defense:* bracket orders placed at entry, and the
absolute rule from chapter 04.

**Overtrading.** Trading out of boredom, or because you feel you should be doing
something. Each unnecessary trade pays spread and commission for no edge.
*Defense:* daily trade limit; close the platform when your window ends.

**Size creep.** Gradually increasing position size after wins. The account is
ordinary until an ordinary losing streak arrives at extraordinary size.
*Defense:* size as a fixed percentage, recalculated from actual equity, never
adjusted by feel.

**Strategy hopping.** Abandoning a system after a normal losing streak, adopting
a new one, repeating. Guarantees you are always trading an untested system and
never accumulate the sample size needed to evaluate anything. *Defense:* commit
to a minimum sample (100+ trades) before judging.

---

## 5. The rules for state

You will trade badly when your state is wrong, regardless of how good your plan
is. These are not soft suggestions; they are risk controls.

**Do not trade when:** angry, anxious about money, sleep-deprived, ill,
intoxicated, in the middle of a personal crisis, or immediately after a large win
(euphoria impairs judgment as reliably as fear).

**After a loss:** step away from the screen for at least five minutes before
considering another trade. Most revenge trades happen within 120 seconds of the
loss that triggered them. A five-minute gap breaks the reflex.

**After a large win:** the same caution applies, for the opposite reason.
Euphoria produces size creep and rule relaxation.

**Have a life outside trading.** Traders whose entire identity and income depend
on the day's P&L make worse decisions, because every trade carries existential
weight. Financial pressure to perform is itself a cause of poor performance —
which is the practical argument for the "only risk money you can afford to lose"
rule in chapter 03. It is not merely about protecting your savings. It is about
protecting your judgment.

---

## 6. Realistic expectations

- **Year one is tuition.** Most traders lose money in their first year. Budget
  for it and define success as process adherence, not profit.
- **Consistency precedes profitability.** Consistent execution comes first;
  profits follow if the edge exists. Never the reverse.
- **Percentage returns, not dollar targets.** A daily dollar target forces trades
  on days with no opportunity — the market does not owe you a setup today.
- **Professional returns are not lottery returns.** Skilled traders target
  double-digit annual percentage returns, not doubling monthly. Anyone showing
  you the latter is either lying or about to blow up, and in either case is not
  a model.
- **Most people should stop.** Given the base rates in the README, deciding after
  a serious, structured attempt that this is not for you is a *good* outcome —
  and a far more common correct answer than the internet suggests.

---

## What to take from this chapter

1. Your cognitive biases systematically produce inverted payoffs. Structure
   defeats them; willpower does not.
2. Experience alone produces no learning — the research is explicit. Structured
   feedback does.
3. Journal every trade. Grade process independently of outcome.
4. "Broke the plan and won" is the most dangerous cell in the matrix.
5. Name your failure modes so you can catch them in progress.
6. State management is a risk control, not a wellness tip.
7. Define success as process adherence in year one.

Next: [07 — Taxes & Record-Keeping](07-taxes-and-record-keeping.md)
