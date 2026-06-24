# === Stage 18: Add an activity log with timestamps and action names ===
# Project: ProjectArchive
from datetime import datetime, timezone
import json
from pathlib import Path

LOG_FILE = "archive.log"

def log_action(action_name: str, details: dict | None = None):
    """Append a timestamped action record to the local activity log."""
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "action": action_name,
        "details": details or {}
    }
    
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            # Write JSON entry followed by a newline for readability and parsing ease
            json.dump(entry, f)
            f.write("\n")
    except IOError as e:
        print(f"[ERROR] Failed to write log entry {action_name}: {e}")

def get_recent_actions(limit: int = 10):
    """Read the last N actions from the log file."""
    if not Path(LOG_FILE).exists():
        return []
    
    entries = []
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    entries.append(json.loads(line))
        
        # Return most recent first
        return list(reversed(entries[-limit:]))
    except json.JSONDecodeError:
        print("[WARNING] Corrupted log entry detected, skipping.")
        return []

# Example usage within your main script logic:
# log_action("update_record", {"record_id": 1042, "field_changed": "status"})
# recent = get_recent_actions(5)
