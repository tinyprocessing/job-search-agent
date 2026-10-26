---
name: apply
description: Apply to one job posting end to end — Hirelog check, adapted CV and letter from real facts, form filling, summary before submit, tracker update, and sharing what was learned with Hirelog. Use when the user says "apply", "откликнись", or gives a posting URL or tracker id.
---

# Apply to one posting

1. Get the posting (URL or tracker id). Read it fully.
2. `hirelog_check_posting(url, company)` and `hirelog_company(company)`. If a corroborated fact says the user
   will be filtered out (location, visa, test before talk) — tell them and suggest skipping.
3. Make `applications/<company>-<role>/`:
   - `cv.md` — from `cv/cv.md` only: reorder bullets, sharpen the summary, add 5–10 keywords from the posting
     **that are true for the user**. Never add skills, years or results that are not in `cv/cv.md` / `profile.md`.
   - `cv.html` — fill `templates/cv.html`; tell the user: open → Print → Save as PDF (or do it in the browser).
   - `cover_letter.md` — 120–200 words: why this company (one specific thing from the posting), one matching
     achievement with a number, availability. Only if there is a field for it or it clearly helps.
4. Before the form: find the application system from the URL (greenhouse, lever, ashby, workable, teamtailor,
   smartrecruiters, workday, recruitee, …) and call `hirelog_ats(slug)`. Apply the workarounds.
5. Fill the form from `profile.md` (browser if connected; otherwise give the user a copy-paste list of answers).
   Account, password, CAPTCHA, "are you human", file picker the tool can't reach → one line to the user.
6. **Summary before Submit** — unusual answers (visa, salary, relocation), open-text answers in full, attached
   files. Submit only after "ok", unless `profile.md` → Rules says auto-submit: yes.
7. `python3 tools/track.py update <id> --status Applied --next "check reply <date +7d>"`. Save open-text
   answers to `answers.md`.
8. **Hirelog:** write 1–3 facts you observed (knockout questions, account walls, test invitations, form bugs,
   remote/visa rules stated in the form). Evidence `form_observed`. Nothing about the user.
