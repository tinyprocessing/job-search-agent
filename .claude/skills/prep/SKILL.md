---
name: prep
description: Prepare the user for a recruiter call, interview or offer conversation — company brief from Hirelog and the web, likely questions, the user's stories from their real CV, questions to ask, and a mock run. Use when a call is booked, or the user says "prep", "prepare me", "подготовь к звонку", "mock interview".
---

# Call / interview prep

1. **What call:** company, role, stage (recruiter, hiring manager, technical, system design, values, offer),
   date and time, who (role only), format. Add it to the tracker next step.
2. **Brief** in `applications/<slug>/call-prep.md`:
   - company in 5 lines: product, size, stage, recent news (web);
   - `hirelog_company(name)` — process stages, real interview questions, response times, red flags;
   - the posting's must-haves mapped to the user's facts (from `cv/cv.md`), and honest gaps with a line for each.
3. **Likely questions** for this stage (Hirelog `interview_question` for the company first, then typical ones)
   with short answer outlines from the user's real experience. Never invent experience.
4. **Three stories** (STAR, 60–90 seconds each): biggest technical result, a team/leadership moment,
   a failure with a lesson — all from the CV.
5. **Hard questions ready:** why leaving, salary expectations (range from `profile.md`, never the minimum),
   right to work / visa, notice period, "why us".
6. **Questions to ask them** (4–6): team, how success is measured in 6 months, the process ahead, what the
   last person in the role struggled with.
7. **Mock run** if the user wants: ask one question at a time, listen, give short feedback (what was strong,
   one thing to fix), next question.
8. **After the call:** debrief (what they asked, how it went, next step) → tracker; when the process is closed,
   share the questions with Hirelog (`interview_question`, evidence `call_happened`) — never the user's answers.
