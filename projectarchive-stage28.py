# === Stage 28: Add overdue item detection based on due dates ===
# Project: ProjectArchive
from datetime import date, timedelta
def check_overdue_items(items):
    today = date.today()
    overdue = []
    for item in items:
        if 'due_date' in item and isinstance(item['due_date'], str):
            due = date.fromisoformat(item['due_date'])
            days_left = (due - today).days
            if days_left < 0:
                item['status'] = 'overdue'
                item['overdue_days'] = abs(days_left)
                overdue.append(item)
    return overdue
