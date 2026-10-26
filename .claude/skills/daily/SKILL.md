---
name: daily
description: Daily job-search routine — check replies, update statuses, follow up, find new postings, apply to the best ones, record outcomes in Hirelog, update status and journal. Use when the user says "daily", "what's today", "что сегодня", or at the start of a working session.
---

# Daily routine (30–60 minutes)

1. **Replies.** If email (Gmail connector) or LinkedIn is available: find new messages from tracked companies
   and recruiters (last 3 days). Update statuses (`Screen`, `Interview`, `Rejected`, …). Draft replies;
   anything about pay, terms, visa or relocation is a draft for the user, sent only after "send".
2. **Due items.** `python3 tools/track.py list --due` → follow-ups (one polite follow-up after 7–10 days, then stop),
   calls to prepare (`hirelog_company` + 3 stories from the CV + questions to ask them).
3. **Hirelog for closed events.** For every rejection, test invitation, knockout or finished call since yesterday —
   1–3 facts (`tools/hirelog.py note`). Rejection timing → `response_time`; location/visa rule → `outcome_pattern`
   or `remote_policy`; questions asked → `interview_question`. If a Hirelog fact proved right or wrong → `hirelog_vote`.
4. **Find** (skill `find`) if fewer than ~10 postings are waiting in `Found`.
5. **Apply** (skill `apply`) to the top 2–5 by fit.
6. **Wrap up:** `python3 tools/track.py stats` → `status.md`; append to `journal/<today>.md`: what was done,
   what is next. One-paragraph report to the user: replies, applications sent, what needs them.

Once a week: look at the funnel by segment (role, country, format) and propose one change that would raise
replies. Small numbers are small numbers — "2 of 30", not "6.7 %".
