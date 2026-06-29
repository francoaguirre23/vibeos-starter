# Keeping things private

A short, plain-language safety standard. The default is simple: **your work stays on your machine.**

## The simple rule (the default)

1. **Your projects are local.** Everything under `projects/` is gitignored. It never leaves your
   machine unless you deliberately choose to share a specific file.
2. **Your identity card is local.** `USER.md` is gitignored too.
3. **Don't put secrets in files.** No passwords, API keys, or tokens in any tracked file. Use a
   `.env` file (also gitignored) if a project needs them.
4. **Before you push anywhere public, run the clean-ship check:**
   ```sh
   bash scripts/clean_ship_check.sh
   ```
   It scans for personal info, secrets, and machine paths and tells you if anything would leak.
   Git history is permanent — fix anything it flags *before* the first push.

If you follow those four points, you're covered for almost everything a solo builder does.

## When you need more (opt-in, for teams or sensitive work)

If you start handling other people's data, working under an NDA, or sharing a workspace with
teammates, you'll want a real classification model — labeling each project Public / Internal /
Confidential / NDA and controlling what may enter git, the synthesis corpus, and the shared
memory. That fuller "fail-closed" model is documented as an advanced add-on; it's deliberately
not in the default path because most people building their own AI team don't need it on Day 1.

The principle to remember if you get there: **anything not explicitly marked shareable is treated
as private.** Forgetting to label something should keep it in, never let it out.
