# DataSEA — Content Repo

Content for the **DataSEA** Android app. Served to clients via [jsDelivr CDN](https://www.jsdelivr.com/?docs=gh).

## Structure

```
content_version.json         ← bump per-module versions to push updates
sections.json                ← 4 learning tracks
feed/                        ← curated articles + news (markdown + index)
daily_challenges/            ← one JSON per date — Daily Debugging Challenge
independent_quizzes/         ← standalone quiz packs
data-analyst/                ← modules organized by tier
data-engineer/
data-science-ml/
dataops-mlops/
```

Each module folder has:
- `topic.json` — metadata
- `lessons/NN-slug.md` — markdown lessons
- `cheatsheet.md` — quick reference
- `quiz.json` — 15-question quiz

## CDN URLs (app fetches from these)

```
https://cdn.jsdelivr.net/gh/ketankkeshri/DataSEA-content@main/content_version.json
https://cdn.jsdelivr.net/gh/ketankkeshri/DataSEA-content@main/sections.json
https://cdn.jsdelivr.net/gh/ketankkeshri/DataSEA-content@main/data-analyst/01-sql-basics/topic.json
https://cdn.jsdelivr.net/gh/ketankkeshri/DataSEA-content@main/data-analyst/01-sql-basics/lessons/01-intro.md
https://cdn.jsdelivr.net/gh/ketankkeshri/DataSEA-content@main/data-analyst/01-sql-basics/quiz.json
https://cdn.jsdelivr.net/gh/ketankkeshri/DataSEA-content@main/independent_quizzes/_index.json
https://cdn.jsdelivr.net/gh/ketankkeshri/DataSEA-content@main/independent_quizzes/interview-sprint.json
```

## Publishing flow

1. Run the content generator (`../app/content-generator`) or edit files manually
2. Bump versions in `content_version.json` for modules you changed
3. Commit and push to `main`
4. jsDelivr propagates within seconds
5. Apps fetch new versions on next sync (default: every 6 hours)

> Force a fresh CDN read by using `@<commit-sha>` instead of `@main` in any URL — useful for testing.
