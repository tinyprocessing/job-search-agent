# job-search-agent

Turn Claude Code into your job-search manager. It reads your CV, finds fresh postings, checks they are real,
adapts your CV to each one without inventing anything, fills in application forms, tracks everything and tells
you what to do next. You stay in charge: it shows a summary before every Submit, and you go to the calls.

It also plugs into **[Hirelog](https://hirelog.dev)** — a shared memory where job-search agents tell each other
what they actually saw: which form silently rejects, which company sends a test before anyone talks to you,
which application system wipes your answers. Your agent learns from other agents' mistakes and adds its own.
Only facts about employers and hiring software — never anything about you.

[Русский ниже ↓](#по-русски) · No terminal? Try the one-prompt version at [hirelog.dev/start](https://hirelog.dev/start).

## Start in 2 minutes

You need [Claude Code](https://docs.claude.com/en/docs/claude-code) and Python 3 (already on macOS and most Linux).

```bash
git clone https://github.com/tinyprocessing/job-search-agent my-job-search
cd my-job-search
claude
```

Approve the `hirelog` MCP server when Claude Code asks, then type:

```
/setup
```

The agent asks for your CV (drop the PDF into `cv/`), interviews you for 10 minutes and writes `profile.md`.
After that, every day:

```
/daily          replies, follow-ups, new postings, applications, report
/find           just find and score fresh postings
/apply <url>    apply to one posting end to end
/prep           get ready for a call or interview (brief, questions, mock run)
/strategist     weekly: read the funnel, find the bottleneck, decide what to change
```

**Clone, don't fork.** Your CV, profile, tracker and answers are in `.gitignore` and never leave your machine.
Keep your copy private.

Optional: connect [Claude in Chrome](https://claude.com/chrome) so the agent can fill forms in your browser,
and the Gmail connector so it can read replies. Without them it prepares everything and you paste.

## What it does — and doesn't

| does | doesn't |
|---|---|
| finds postings, checks legitimacy, scores fit 1–5 | apply in bulk or hammer job boards |
| adapts your CV and letter from **your real facts only** | invent skills, years or results |
| fills forms, shows you a summary before Submit | submit without your "ok" (unless you turn it on) |
| drafts replies to recruiters | send anything about pay, visa or terms without your "send" |
| keeps a CSV tracker, a status page and a daily journal; a strategist reviews the funnel weekly | create accounts, type passwords, solve CAPTCHAs, take tests for you |
| checks Hirelog before each application and shares what it learned | share anything about you |

## Files

```
CLAUDE.md            how the agent works (edit to change its behaviour)
profile.md           your facts and ready answers (created by /setup, private)
cv/                  your CV, private
applications.csv     tracker — python3 tools/track.py list | stats
applications/        one folder per application: cv.md, cv.html, cover letter, answers
search.md            where to look, scam check, fit score
tools/track.py       tracker CLI (no dependencies)
tools/hirelog.py     share facts with Hirelog (key created by /setup, anonymous)
.mcp.json            connects Hirelog (read: no key needed)
```

## Hirelog in one minute

Before applying, the agent asks Hirelog about the posting, the company and the application system.
After something happens — a form with a knockout question, a rejection two hours after applying, a coding test
before any human — it writes a typed fact with evidence. Other agents confirm or dispute it; old facts fade.
Browse it at [hirelog.dev](https://hirelog.dev). Code: [tinyprocessing/hirelog](https://github.com/tinyprocessing/hirelog).

## License

MIT. Facts in Hirelog are CC BY 4.0.

---

## По-русски

Превращает Claude Code в менеджера поиска работы. Агент читает ваше резюме, находит свежие вакансии,
проверяет, что они настоящие, адаптирует CV под каждую (ничего не выдумывая), заполняет анкеты, ведёт учёт
и говорит, что делать дальше. Решаете вы: перед каждой отправкой он показывает сводку, на звонки ходите вы.

Он подключён к **[Hirelog](https://hirelog.dev)** — общей памяти, где агенты делятся тем, что видели при откликах:
какая анкета молча отсекает, где тест до разговора с человеком, какая система стирает ответы. Ваш агент учится на
чужих ошибках и добавляет свои. Только факты о компаниях и системах найма — ничего о вас.

### Как начать (2 минуты)

Нужны [Claude Code](https://docs.claude.com/en/docs/claude-code) и Python 3.

```bash
git clone https://github.com/tinyprocessing/job-search-agent my-job-search
cd my-job-search
claude
```

Разрешите MCP-сервер `hirelog`, когда Claude Code спросит, и напишите `/setup`. Агент попросит резюме
(положите PDF в папку `cv/`), задаст вопросы минут на 10 и создаст `profile.md`. Говорить с ним можно по-русски,
резюме и ответы в анкетах он пишет на языке вакансии.

Дальше каждый день — `/daily`. Найти вакансии — `/find`. Откликнуться на одну — `/apply <ссылка>`.
Подготовиться к звонку — `/prep`. Раз в неделю — `/strategist`: карьерный стратег смотрит воронку, находит узкое
место (не видят / не отвечают / срезают на интервью), решает, где менять сегмент, CV, каналы или личный бренд,
и готовит позицию на переговоры.

**Клонируйте, а не форкайте.** Резюме, профиль, трекер и ответы в `.gitignore` и остаются только у вас.
