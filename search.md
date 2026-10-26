# Where to look and how to judge a posting

## Where
- Company careers pages (best: direct, current, real form).
- LinkedIn Jobs (filter by last 24 h / week), Indeed, Wellfound (startups), Otta/Welcome to the Jungle,
  Remote-first boards (Remote OK, We Work Remotely, Himalayas), Hacker News "Who is hiring?" (1st of each month).
- Local boards for your country (ask the user which ones they use).
- Recruiter posts in social feeds ("hiring", "looking for") — reply fast, they get the best leads.
- Before trusting a board, `hirelog_search(query="<board name>")` — reposters and aggregators are marked there.

## Is it real? (any 2 → `Suspicious`, don't apply)
- No company name, or the company has no site / no LinkedIn page / no employees.
- Contact only through Telegram/WhatsApp, or "send your CV to a gmail address".
- Pay far above market for little experience; "no interview needed".
- Asks for money, ID documents, bank details or a "training fee" before an offer.
- The same text posted under many company names; the link goes to an aggregator, not to the employer.
- `hirelog_check_posting` returns a corroborated `red_flag`.

## Fit 1–5
- **5** — role, level, stack, location/format and pay all match; you would be sad to miss it.
- **4** — one soft gap (one missing tool, slightly different level).
- **3** — reasonable: core matches, two gaps or unclear format/pay.
- **2** — a stretch: different stack or format that is barely possible.
- **1** — not a match.

Fit ≥ 4 → adapted CV + letter. Fit 3 → base CV + short letter. Fit ≤ 2 → `Skipped` with a reason,
unless the user's Rules say otherwise.

## Before applying, also check
- Posted when? Older than 2–3 weeks and 100+ applicants → only for fit 4–5.
- Location rules: "remote" often means "remote within one country".
- Visa: does it say no sponsorship, and does the user need it there?
- A knockout question in the form ("Do you have the right to work in …?") — check `hirelog_check_posting` first.
