# Project Rules — read before any action

## What this repo actually is

This is not application code. It's operational config for Zach's businesses:

- `theme/` — Liquid sections for the **musicsplitsheets.com** Shopify store.
- `marketing/routines/*.md` — the standing prompts for four autonomous agents
  (SPLIT MERCHANT, THE MANAGER, A&R HEAD, THE SCOUT) plus THE COORDINATOR and a
  morning briefing prompt. These are pasted by hand into an external dashboard —
  editing the file here does **not** update the running agent until Zach pastes it in.
- `marketing/*.md` — outreach copy and campaign notes for musicsplitsheets.com.

There is no build or test command. "Correct" here means: internally consistent
facts (prices, dates, URLs, retired pages) across every file that repeats them,
and no accidental contradiction of a rule a routine depends on.

## How the routines relate to each other

The four operational agents aren't independent — they feed a reporting chain,
and editing one can quietly break what another depends on:

- Each of SPLIT MERCHANT, THE MANAGER, A&R HEAD, and THE SCOUT reads its own
  prior run summaries at the start of every run (its MEMORY PROTOCOL) — that
  history is its only persistent memory, so a run summary that silently ends
  up in drafts instead of sent breaks that agent's memory going forward.
- THE COORDINATOR runs weekly, reads all four agents' run summaries/digests by
  subject-line match (`SPLIT MERCHANT`, `THE MANAGER`, `A&R HEAD`, `THE SCOUT`),
  and synthesizes them into one "STATE OF ZACH" email. If you rename an agent
  or change its run-summary subject format, update THE COORDINATOR's search
  terms in the same change or its digest silently goes blind to that agent.
- `briefing-v2.md` (the morning briefing) deliberately excludes all
  agent-generated mail (`Run Summary`, `DISPATCH:`, `STATE OF ZACH`, `Reddit
  post ready:`, `LinkedIn draft`) from the "important emails" section and
  rolls it into a one-line drafts counter instead — this keeps the ~20/week
  agent mail from drowning real human mail. If you add a new agent or a new
  recurring subject pattern, add it to this exclusion list too.
- THE MANAGER treats musicsplitsheets.com (SPLIT MERCHANT's business) as an
  internal resource for BHM roster registration checks — a cross-business
  reference, not a duplicate. Don't "simplify" it away as redundant.
- SPLIT MERCHANT sends from Gmail (`zskedzuhn@gmail.com`); THE MANAGER drafts
  in Outlook (`zach@blushhillmgmt.com`); A&R HEAD and THE SCOUT both act on
  `zskedzuhn@gmail.com`. Dispatch emails from Zach's dashboard must land in
  the inbox each agent actually reads, or the MEMORY PROTOCOL silently misses
  them (A&R HEAD's own prompt flags this exact failure mode for Niels-related mail).

## Always

- Read the whole routine file before editing it, not just the section you're
  changing — these prompts cross-reference their own rules (MEMORY PROTOCOL,
  CRITICAL RULE blocks, DAILY TASK STRUCTURE) and a change in one place can
  silently break another.
- When you edit a routine prompt, update its "Changes:" line at the top of the
  file (the changelog under the H1) so Zach knows what to re-paste and why.
- Keep facts consistent across files whenever you touch one of them:
  - Prices: split sheet $7, bundle $12, catalogue audits from $497 (roster
    audits from $1,997). These appear in `README.md`, `theme/sections/*.liquid`,
    and multiple routine files — grep for the old numbers ($3/$5) if you're
    touching pricing anywhere.
  - The AUGUST discount code is templates-only, expires **Aug 31, 2026**, and
    must never appear in copy dated after that.
  - `/pages/create` is retired — never add a link to it.
- Preserve each agent's send-vs-draft posture exactly as written — it's a
  deliberate, per-agent decision, not an oversight:
  - SPLIT MERCHANT, A&R HEAD's own run-summary, and THE SCOUT's own run-summary:
    send directly.
  - THE MANAGER: everything except its own run summary is draft-only, always.
  - A&R HEAD and THE SCOUT: all *outreach* is draft-only; only run summaries send.
- Preserve each agent's brand-voice rules verbatim (e.g. "no em dashes," "no
  hype language," "creatives not artists" for BHM) — these are style contracts,
  not filler.

## Never

- Never call a live tool (Gmail send, Shopify publish/write, Outlook send) as a
  side effect of editing a file in this repo. Editing `the-manager-v2.md` must
  never itself send an email or touch a store. If a task asks you to actually
  run one of these routines live, treat that as a distinct, explicit request —
  confirm before taking any real send/publish/write action.
- Never edit the live Shopify theme. Theme changes are staged on the duplicate
  theme named in `README.md` ("Conversion Update — Aug 2026" or its successor);
  publishing is a manual step Zach does in Shopify admin.
- Never promote the Mini High Speed Handheld Fan product in any split-sheet
  content, blog copy, or outreach — it's intentionally off-brand and hidden.
- Never reintroduce paid third-party playlist placement as a recommendation
  (A&R HEAD, THE MANAGER) — firm policy, stated twice for a reason.
- Never touch `/migrations` or secrets-like files (none currently exist here,
  but if one appears, treat it as out of scope without explicit instruction).
- Anything ambiguous about whether a change is "just editing the prompt" vs.
  "taking the real-world action described in the prompt": stop and ask.
