---
name: setup
description: First-run onboarding for the job-search agent — reads the user's CV, interviews them, writes profile.md, creates the tracker and a Hirelog contributor key. Use on first run, when profile.md is missing, or when the user says "setup", "start", "begin", "начать".
---

# Setup (10–15 minutes, once)

Goal: after this, the agent knows enough to apply on the user's behalf without inventing anything.

1. **Greet and set the language.** Ask which language to talk in. Explain in 3 lines what will happen.
2. **CV.** Ask the user to put their CV into `cv/` (PDF, DOCX or pasted text). Read it and write `cv/cv.md`:
   the same content as clean Markdown — no new facts, no rewording of achievements. Show the user a 5-line
   summary of what you read and ask them to correct anything wrong.
3. **Interview** — ask in small groups (2–4 questions at a time), skip what the CV already answers:
   - target roles and seniority; stack they want / don't want;
   - work format (remote / hybrid / onsite), countries, relocation, visa status per country;
   - contract work (yes/no, how), start date / notice period;
   - pay: target range per market and a minimum (explain the minimum is never said aloud);
   - years per main skill (forms ask "years of X");
   - ready answers: why looking, biggest achievement with numbers, right-to-work line;
   - their rules: auto-submit (default **no**), skip tests before any human talk, sites or companies to avoid.
4. **Write `profile.md`** using `profile.example.md` as the structure. Show it, apply corrections.
5. **Tracker and logs:** `python3 tools/track.py list` (creates nothing until the first add — fine), create
   `status.md` (empty funnel) and `journal/<today>.md` ("setup done").
6. **Hirelog.** Check the MCP connection: call `hirelog_market()` — if it answers, reading works.
   If tools are missing, tell the user to run `/mcp` and approve `hirelog`, or:
   `claude mcp add --transport http hirelog https://hirelog.dev/mcp`.
   Then ask: "May I create an anonymous Hirelog key so the agent can share facts about employers
   (never about you)?" Yes → `python3 tools/hirelog.py key`.
7. **Browser (optional).** If Claude in Chrome is available, say the agent can fill forms in their browser;
   otherwise it prepares everything and the user pastes it.
8. **First task.** Offer to run `find` now ("let's find 10 fresh postings that fit you").

Never store passwords. Never ask for ID documents or bank details.
