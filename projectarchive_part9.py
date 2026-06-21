# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: ProjectArchive
from datetime import datetime
def sort_records(records, key='date', reverse=False):
    if key == 'title': return sorted(records, key=lambda r: (r.get('priority') or 0, r['title'].lower()), reverse=reverse)
    if key == 'date': return sorted(records, key=lambda r: r.get('created_at') or datetime.min, reverse=True)
    if key == 'last_update': return sorted(records, key=lambda r: r.get('updated_at') or datetime.min, reverse=True)
    if key == 'priority': return sorted(records, key=lambda r: (r.get('priority') or 0), reverse=reverse)
    raise ValueError(f"Unsupported sort key: {key}")

def get_sorted_records(all_records, filters=None):
    filtered = all_records
    if filters:
        for k, v in filters.items():
            filtered = [r for r in filtered if str(r.get(k)) == str(v)]
    return sort_records(filtered)
