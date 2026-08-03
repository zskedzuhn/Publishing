# Briefing — updated prompt (Aug 2026)

Changes: excludes the ~20 weekly agent-generated emails from the "important emails" section
(they were at risk of drowning the human mail), replaces them with a one-line drafts counter.
Optional: consider moving the cron from 12:30 UTC (5:30am PT) to 14:00 UTC (7am PT).

---

Generate a briefing to help me catch up. Include:

1. Schedule — List upcoming meetings and events with times, attendees, and any preparation needed
2. Important emails — Summarize unread emails that need attention, grouped by urgency. EXCLUDE agent-generated mail: skip any email whose subject contains "Run Summary", "DISPATCH:", "STATE OF ZACH", "Reddit post ready:", or "LinkedIn draft". Those are covered by item 5.
3. Messages requiring response — Flag any direct messages or mentions that need a reply, or sent emails that need to be followed up on. Same agent-mail exclusions apply.
4. Action items — List any pending tasks or follow-ups from recent activity
5. Agent queue — One line only: how many drafts are sitting in Gmail/Outlook drafts awaiting my review (LinkedIn, outreach, replies), and the single most urgent item any agent flagged since yesterday, if one exists.

Keep the briefing concise and scannable. If there's nothing notable in a section, skip it rather than saying "nothing to report."
