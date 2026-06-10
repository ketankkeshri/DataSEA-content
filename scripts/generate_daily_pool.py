#!/usr/bin/env python3
"""
Generates track-scoped Daily-5 / quiz-pool monthly bucket files from the four
synthetic MCQ source files at ~/Downloads/DataSEA/MCQS.

Output layout (committed to the content repo, served via jsDelivr):

    daily_pool/
      _index.json                       # global metadata (tracks, months, dates)
      data-analyst/
        2026-06.json                    # one file per (track, month)
        2026-07.json
        ...
      data-engineer/
        2026-06.json
        ...
      data-science-ml/
        ...
      dataops-mlops/
        ...

Each monthly file contains all the questions whose `availableFrom` falls in
that month. The app filters at runtime with `availableFrom <= today` so future
questions are downloaded but kept invisible until their date.

Allocation:
  * 5 Daily-5 questions / day / track, starting on START_DATE.
  * data-analyst (10k) → ~5.5 years of daily-5
  * data-engineer / data-science-ml / dataops-mlops (5k each) → ~2.7 years

Run from anywhere:
    python3 scripts/generate_daily_pool.py
"""
import json
import random
from datetime import date, timedelta
from pathlib import Path

# ── Config ──────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = REPO_ROOT / "sources"
OUT_DIR = REPO_ROOT / "daily_pool"

START_DATE = date(2026, 6, 10)
DAILY_5_PER_DAY = 5
RNG_SEED = 42

# Canonical sources, produced by normalize_sources.py — one file per track.
# Each file is `{schemaVersion, track, total, questions: [...]}` with a single
# unified question schema, so this generator no longer cares about per-input quirks.
SOURCES = [
    "data-analyst",
    "data-engineer",
    "data-science-ml",
    "dataops-mlops",
]

# ── Schedule shape ─────────────────────────────────────────────────────

def to_schedule_question(track, raw):
    """
    Convert a canonical source question (from sources/<track>.json) into the
    daily-pool question shape — adds source + xp/coins, preserves everything
    else. `availableFrom` is set later by assign_dates().
    """
    difficulty = (raw.get("difficulty") or "easy").lower()
    if difficulty not in {"easy", "medium", "hard"}:
        difficulty = "easy"
    xp, coins = {"easy": (10, 2), "medium": (15, 3), "hard": (25, 5)}.get(
        difficulty, (10, 2),
    )
    return {
        "id":           raw["id"],
        "track":        track,
        "source":       "daily-pool",
        "category":     raw.get("category", "General"),
        "topic":        raw.get("topic", ""),
        "difficulty":   difficulty,
        "question":     raw.get("question", ""),
        "options":      raw.get("options") or [],
        "correctIndex": int(raw.get("correctIndex", 0)),
        "tags":         raw.get("tags") or [],
        "xp":           xp,
        "coins":        coins,
    }


def load_track(track):
    path = SOURCE_DIR / f"{track}.json"
    with open(path) as f:
        data = json.load(f)
    return [to_schedule_question(track, q) for q in data.get("questions", [])]


# ── Date assignment ────────────────────────────────────────────────────

def assign_dates(questions, rng):
    """
    5 questions/day, with a rotating 2-2-1 difficulty pattern so every day
    surfaces all three difficulty levels:

        Day n % 3 == 0 → 2 easy + 2 medium + 1 hard
        Day n % 3 == 1 → 1 easy + 2 medium + 2 hard
        Day n % 3 == 2 → 2 easy + 1 medium + 2 hard

    Over each 3-day cycle the day consumes 5 easy + 5 medium + 5 hard, so an
    evenly-balanced source pool (1/3 each) drains uniformly. Within each daily
    slot questions are drawn at random from the appropriate difficulty queue.

    Days continue beyond the balanced run by filling 5 from whatever's left —
    in practice that tail never appears for evenly-tagged inputs.
    """
    # Bucket by difficulty, shuffle each independently
    buckets = {"easy": [], "medium": [], "hard": []}
    for q in questions:
        d = q["difficulty"] if q["difficulty"] in buckets else "easy"
        buckets[d].append(q)
    for v in buckets.values():
        rng.shuffle(v)

    pattern = [
        (2, 2, 1),  # day 0
        (1, 2, 2),  # day 1
        (2, 1, 2),  # day 2
    ]

    assigned = []
    day = 0
    total = sum(len(v) for v in buckets.values())
    while sum(len(v) for v in buckets.values()) > 0:
        want_e, want_m, want_h = pattern[day % len(pattern)]
        picks = []
        # Pull from the requested difficulty if available, else fall back to any
        def take(bucket_key, n):
            taken = []
            while n > 0 and buckets[bucket_key]:
                taken.append(buckets[bucket_key].pop())
                n -= 1
            return taken, n
        e_picks, want_e_rest = take("easy",   want_e)
        m_picks, want_m_rest = take("medium", want_m)
        h_picks, want_h_rest = take("hard",   want_h)
        picks = e_picks + m_picks + h_picks
        # Backfill any shortfall from whichever bucket still has items
        shortfall = DAILY_5_PER_DAY - len(picks)
        if shortfall > 0:
            for key in ("easy", "medium", "hard"):
                while shortfall > 0 and buckets[key]:
                    picks.append(buckets[key].pop())
                    shortfall -= 1
        avail = (START_DATE + timedelta(days=day)).isoformat()
        for q in picks:
            q["availableFrom"] = avail
            q["bucket"] = "daily-5"
        assigned.extend(picks)
        day += 1
        if day > total:  # safety: shouldn't happen
            break
    return assigned


def bucket_by_month(questions):
    out = {}
    for q in questions:
        ym = q["availableFrom"][:7]                          # YYYY-MM
        out.setdefault(ym, []).append(q)
    return out


# ── Output ─────────────────────────────────────────────────────────────

def write_pool():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    index = {
        "schemaVersion": 2,
        "generatedAt": date.today().isoformat(),
        "startDate": START_DATE.isoformat(),
        "dailyFivePerDay": DAILY_5_PER_DAY,
        "tracks": {},
    }
    rng = random.Random(RNG_SEED)

    for track in SOURCES:
        print(f"Loading {track}…", end=" ", flush=True)
        questions = load_track(track)
        assign_dates(questions, rng)
        by_month = bucket_by_month(questions)

        track_dir = OUT_DIR / track
        track_dir.mkdir(parents=True, exist_ok=True)
        # Wipe old month files for an idempotent regen
        for old in track_dir.glob("*.json"):
            old.unlink()

        months = sorted(by_month.keys())
        for month in months:
            payload = {
                "schemaVersion": 2,
                "track": track,
                "month": month,
                "questions": by_month[month],
            }
            (track_dir / f"{month}.json").write_text(
                json.dumps(payload, separators=(",", ":")) + "\n",
            )

        last_date = max(q["availableFrom"] for q in questions)
        first_date = min(q["availableFrom"] for q in questions)
        index["tracks"][track] = {
            "totalQuestions": len(questions),
            "firstDate": first_date,
            "lastDate": last_date,
            "months": months,
        }
        print(f"{len(questions)} q · {len(months)} months · "
              f"{first_date} → {last_date}")

    (OUT_DIR / "_index.json").write_text(json.dumps(index, indent=2) + "\n")
    print(f"\nIndex: {OUT_DIR / '_index.json'}")
    print(f"Done. {OUT_DIR}")


if __name__ == "__main__":
    write_pool()
