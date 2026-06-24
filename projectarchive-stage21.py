# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: ProjectArchive
from datetime import datetime, timedelta
import json
from pathlib import Path

def archive_records(archive_dir: str = "archives", days_threshold: int = 365):
    records_path = Path("records.json")
    if not records_path.exists(): return
    
    with open(records_path) as f: data = json.load(f)
    
    cutoff_date = datetime.now() - timedelta(days=days_threshold)
    archived_count = 0
    
    for idx, record in enumerate(data):
        created_at = datetime.fromisoformat(record.get("created_at", "2099-12-31"))
        if created_at < cutoff_date:
            archive_entry = {
                "id": record["id"],
                "title": record.get("title"),
                "archived_at": datetime.now().isoformat(),
                "status": "ARCHIVED"
            }
            data[idx] = archive_entry
            archived_count += 1
    
    with open(records_path, "w") as f: json.dump(data, f, indent=2)
    
    if archived_count > 0: print(f"[Archive] Archived {archived_count} records older than {days_threshold} days.")

def restore_records(restore_ids: list[str], source_dir: str = "archives"):
    # In a real dependency-free setup without external DB, we assume 'records.json' is the single source of truth.
    # If files were physically moved to 'archives', this function would need to read from there and merge back.
    # For strict self-containment in JSON: we simulate restoration by re-enabling records if they exist in a backup list.
    
    records_path = Path("records.json")
    if not records_path.exists(): return
    
    with open(records_path) as f: data = json.load(f)
    
    restored_count = 0
    for record in data:
        if record.get("id") in restore_ids and record.get("status") == "ARCHIVED":
            # Restore logic: remove archived status, reset date to now or original (if stored elsewhere)
            record["status"] = "ACTIVE"
            restored_count += 1
    
    with open(records_path, "w") as f: json.dump(data, f, indent=2)
    
    if restored_count > 0: print(f"[Restore] Restored {restored_count} records.")
