# === Stage 26: Add weekly summary calculations ===
# Project: ProjectArchive
import os, json, datetime as dt
from pathlib import Path
def calc_weekly_summary(base_dir):
    path = Path(base_dir) / "reports" / "weekly.json"
    if not path.exists(): return []
    data = json.loads(path.read_text())
    records = [r for r in data.get("records", []) if isinstance(r, dict)]
    weeks = {}
    for rec in records:
        ts = dt.datetime.fromisoformat(rec.get("timestamp", ""))
        week_key = ts.strftime("%Y-W%W")
        if week_key not in weeks:
            weeks[week_key] = {"count": 0, "tags": set(), "decisions": []}
        weeks[week_key]["count"] += 1
        for tag in rec.get("tags", []): weeks[week_key]["tags"].add(tag)
        if rec.get("type") == "decision": weeks[week_key]["decisions"].append(rec.get("title"))
    summary = [{"week": w, **v} for w, v in sorted(weeks.items())]
    with open(path, "w", encoding="utf-8") as f: json.dump(summary, f, ensure_ascii=False, indent=2)
    return summary
