# === Stage 37: Add recommendations for the next useful action ===
# Project: ProjectArchive
import os, json, datetime
from pathlib import Path

def generate_next_action_report(archive_path: str = "data/archive.json") -> dict:
    """Generate a compact report with recommendations for the next useful action."""
    archive_file = Path(archive_path)
    if not archive_file.exists():
        return {"status": "error", "message": f"Archive file {archive_path} not found."}

    try:
        with open(archive_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"status": "error", "message": "Failed to read archive JSON file."}

    records_count = len(data.get("records", []))
    tags_set = set(tag for rec in data.get("records", []) for tag in rec.get("tags", []))
    last_modified = max((r["timestamp"] for r in data.get("records", []) if "timestamp" in r), default=datetime.datetime.now())

    recommendations = []
    if len(tags_set) < 5:
        recommendations.append(f"Add more tags to improve categorization (currently {len(tags_set)}).")
    if records_count > 0 and last_modified.replace(tzinfo=None) + datetime.timedelta(days=7) < datetime.datetime.now():
        recommendations.append("Review recent activity or add a new record.")

    return {
        "status": "success",
        "metrics": {"records": records_count, "unique_tags": len(tags_set)},
        "recommendations": recommendations if recommendations else ["No immediate actions required."]
    }
