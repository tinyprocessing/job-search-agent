---
name: find
description: Find fresh job postings that fit profile.md, check each for legitimacy and fit, and add them to the tracker. Use when the user says "find", "search jobs", "what's new", "найди вакансии".
---

# Find postings

1. Read `profile.md` (roles, format, countries, rules) and `search.md`.
2. Search the sources in `search.md` for the last 1–7 days (browser if connected, otherwise web search).
   Prefer the employer's own careers page over aggregators. Human pace — open postings one by one.
3. For each posting:
   - skip if already tracked (`track.py add` refuses duplicate links);
   - `hirelog_check_posting(url, company)` — note any corroborated red flag, test-before-talk or knockout;
   - legitimacy check and fit 1–5 from `search.md`;
   - `python3 tools/track.py add --company … --role … --link … --location … --source … --fit N --status Found|Skipped|Suspicious --notes "<why, 1 line>"`.
4. Report: a short table of `Found` postings by fit (company, role, format, why it fits, risk) and how many were
   skipped and why. Propose which ones to apply to first.
5. If you noticed something useful about a board or employer (reposts, fake listings, location rules),
   write it to Hirelog (`tools/hirelog.py note`, evidence `page_observed`).
