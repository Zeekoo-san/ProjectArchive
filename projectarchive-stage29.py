# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: ProjectArchive
from datetime import datetime, timedelta
from typing import List, Dict, Optional

def get_upcoming_reminders(reminders: List[Dict], days_ahead: int = 7) -> List[Dict]:
    now = datetime.now()
    cutoff = now + timedelta(days=days_ahead)
    upcoming = []
    for r in reminders:
        due = datetime.fromisoformat(r['due_at'].replace('Z', '+00:00')) if 'Z' in r['due_at'] else datetime.fromisoformat(r['due_at'])
        if now <= due < cutoff and not r.get('completed'):
            urgency = "urgent" if due - now < timedelta(hours=24) else ("soon" if due - now < timedelta(days=3) else "")
            upcoming.append({**r, 'days_left': (due - now).days, 'urgency': urgency})
    return sorted(upcoming, key=lambda x: x['due_at'])

def format_reminder_summary(reminders: List[Dict]) -> str:
    if not reminders:
        return "No upcoming items."
    lines = ["Upcoming Items:", f"  - {len(reminders)} pending."]
    for r in reminders[:5]:
        status = "[!]" if r.get('urgency') == 'urgent' else ("[~]" if r.get('urgency') == 'soon' else "")
        lines.append(f"{status} {r['title']} ({r['days_left']} days)")
    return "\n".join(lines)
