# === Stage 25: Add daily summary calculations ===
# Project: ProjectArchive
from datetime import date, timedelta
def calculate_daily_summary(records):
    today = date.today()
    summary = {"date": str(today), "total_records": 0, "new_entries": 0}
    for rec in records:
        if isinstance(rec.get("created_at"), str):
            try:
                d = datetime.strptime(rec["created_at"], "%Y-%m-%d").date()
                summary["total_records"] += 1
                if d == today:
                    summary["new_entries"] += 1
            except ValueError:
                pass
    return summary
