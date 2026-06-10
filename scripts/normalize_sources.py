#!/usr/bin/env python3
"""
Normalises the four raw MCQ source files into a single canonical shape and
writes them to `sources/<track>.json` inside the content repo.

Canonical question schema:

    {
      "id":           "DA-1" | "DE-0001" | "DS-0001" | "MO-1",
      "track":        "data-analyst" | "data-engineer" | "data-science-ml" | "dataops-mlops",
      "category":     "SQL", "Statistics & Probability", "CI/CD", ...
      "topic":        "SELECT Basics" | "" (optional sub-category),
      "difficulty":   "easy" | "medium" | "hard",
      "question":     "Which SQL clause is used to filter rows ...",
      "options":      ["WHERE", "HAVING", "ORDER BY", "GROUP BY"],
      "correctIndex": 0,
      "tags":         ["sql", "filtering", ...]
    }

The generator (`generate_daily_pool.py`) reads from these canonical files only —
no logic depends on the raw input layout. To swap in a new source bank, just
extend this script.
"""
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = REPO_ROOT / "sources"

# ── Raw inputs ─────────────────────────────────────────────────────────

INPUTS = [
    {
        "track":   "data-analyst",
        "path":    "/Users/ketankeshri/Documents/Personal/Data-Engg/fb-insta/data_analytics_questions.json",
        "id_prefix": "da",
        "json_key":  None,                       # top-level list
    },
    {
        "track":   "data-engineer",
        "path":    "/Users/ketankeshri/Documents/Personal/Data-Engg/fb-insta/data_engineering_questions.json",
        "id_prefix": "de",
        "json_key":  None,
    },
    {
        "track":   "data-science-ml",
        "path":    "/Users/ketankeshri/Documents/Personal/Data-Engg/fb-insta/ds_ml_genai_questions.json",
        "id_prefix": "ds",
        "json_key":  "questions",                # nested under "questions"
    },
    {
        "track":   "dataops-mlops",
        "path":    "/Users/ketankeshri/Downloads/DataSEA/MCQS/mlops_dataops_5000_questions.json",
        "id_prefix": "mo",
        "json_key":  "questions",
    },
]

# Strip trailing "(Question N)" / "(Q N)" cosmetic suffixes from mlops file.
TRAIL_PAT = re.compile(r"\s*\((?:Question|Q)\s*\d+\)\s*$", re.I)


def _options_and_correct_index(raw):
    """
    Returns (options_list, correct_index) from any of the input shapes:

    * dict + correct_answers letter list:
        options={"A":"x","B":"y","C":"z","D":"w"}, correct_answers=["B"] → index 1
    * list + correct_answer_index:
        options=["x","y","z","w"], correct_answer_index=1
    * list + correctAnswerIndex (camelCase variant):
        options=["x","y","z","w"], correctAnswerIndex=1
    * list + correct_option_index (mlops shape):
        options=["x","y","z","w"], correct_option_index=1
    * list + correct_answer (full text match):
        options=["x","y","z","w"], correct_answer="y" → 1
    """
    opts = raw.get("options")
    if isinstance(opts, dict):
        keys = sorted(opts.keys())                   # ['A','B','C','D']
        options_list = [opts[k] for k in keys]
        ca_list = raw.get("correct_answers") or []
        if ca_list and ca_list[0] in keys:
            return options_list, keys.index(ca_list[0])
        # Last-ditch: dict shape but answer is the full text
        ca_text = raw.get("correct_answer")
        if ca_text in options_list:
            return options_list, options_list.index(ca_text)
        return options_list, 0

    if isinstance(opts, list):
        options_list = list(opts)
        for k in ("correct_answer_index", "correctAnswerIndex", "correct_option_index"):
            if k in raw and isinstance(raw[k], int):
                return options_list, raw[k]
        ca_text = raw.get("correct_answer")
        if ca_text in options_list:
            return options_list, options_list.index(ca_text)
        # If correct_answers is a list of letters (rare for list-shaped opts):
        ca_list = raw.get("correct_answers") or []
        letters = ["A", "B", "C", "D", "E", "F"]
        if ca_list and ca_list[0] in letters:
            idx = letters.index(ca_list[0])
            if 0 <= idx < len(options_list):
                return options_list, idx
        return options_list, 0

    return [], 0


def _difficulty(raw):
    val = (raw.get("difficulty") or "easy").strip().lower()
    return val if val in {"easy", "medium", "hard"} else "easy"


def _category(raw):
    # Prefer `category`; mlops also has `domain`; some files use `category` already.
    cat = raw.get("category") or raw.get("domain") or "General"
    return str(cat).strip() or "General"


def _topic(raw):
    return str(raw.get("topic") or "").strip()


def _tags(raw, category, topic, raw_track):
    base = list(raw.get("tags") or [])
    # Always include a track tag so downstream filters are easy.
    tags = set(base)
    for t in (category, topic, raw_track):
        if t and isinstance(t, str):
            tags.add(t.lower().replace(" ", "-"))
    return sorted(tags)


def _question_text(raw):
    q = str(raw.get("question") or "").strip()
    q = TRAIL_PAT.sub("", q)
    return q


def normalize_one(raw, idx, track, id_prefix):
    options, correct_index = _options_and_correct_index(raw)
    # Use existing id if it already carries the prefix; otherwise generate one.
    src_id = raw.get("id")
    qid = (
        str(src_id) if isinstance(src_id, str) and src_id.lower().startswith(id_prefix.lower())
        else f"{id_prefix.upper()}-{idx:05d}"
    )
    category = _category(raw)
    topic = _topic(raw)
    return {
        "id":           qid,
        "track":        track,
        "category":     category,
        "topic":        topic,
        "difficulty":   _difficulty(raw),
        "question":     _question_text(raw),
        "options":      options,
        "correctIndex": int(correct_index),
        "tags":         _tags(raw, category, topic, track),
    }


def load_raw(path: str, json_key):
    with open(path) as f:
        data = json.load(f)
    if json_key is None:
        return data if isinstance(data, list) else []
    if isinstance(data, list):
        return data
    return data.get(json_key) or []


def main():
    SOURCES_DIR.mkdir(parents=True, exist_ok=True)
    for src in INPUTS:
        raw_list = load_raw(src["path"], src["json_key"])
        normalized = [
            normalize_one(q, i + 1, src["track"], src["id_prefix"])
            for i, q in enumerate(raw_list)
        ]
        out_path = SOURCES_DIR / f"{src['track']}.json"
        out_path.write_text(
            json.dumps({
                "schemaVersion": 1,
                "track":         src["track"],
                "total":         len(normalized),
                "questions":     normalized,
            }, ensure_ascii=False) + "\n",
        )
        print(f"{src['track']:18s} → {len(normalized):>5d} questions  ({out_path})")


if __name__ == "__main__":
    main()
