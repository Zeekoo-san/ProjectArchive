# === Stage 11: Add JSON export for the current application state ===
# Project: ProjectArchive
import json, os, datetime
def export_state(path="state.json"):
    state = {"timestamp": str(datetime.datetime.now()), "records": [], "decisions": [], "files": [], "tags": set(), "timelines": []}
    for r in records: state["records"].append({"id": r.id, "title": r.title, "summary": r.summary})
    for d in decisions: state["decisions"].append({"id": d.id, "context": d.context, "outcome": d.outcome})
    for f in files: state["files"].append({"name": f.name, "path": f.path, "size": os.path.getsize(f.path) if os.path.exists(f.path) else 0})
    state["tags"] = list(state["tags"])
    with open(path, "w", encoding="utf-8") as fh: json.dump(state, fh, indent=2, ensure_ascii=False)
