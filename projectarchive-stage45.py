# === Stage 45: Add restore from backup with validation ===
# Project: ProjectArchive
import os, json, hashlib, datetime

def validate_backup(backup_path):
    if not os.path.exists(backup_path) or not os.path.isdir(backup_path):
        return False, "Backup path does not exist or is not a directory."
    
    required_files = ['records.json', 'decisions.json', 'files_index.json', 'tags.json']
    for f in required_files:
        if not os.path.exists(os.path.join(backup_path, f)):
            return False, f"Missing critical file: {f}"
    
    try:
        with open(os.path.join(backup_path, 'records.json'), 'r', encoding='utf-8') as fp:
            json.load(fp)
    except (json.JSONDecodeError, IOError):
        return False, "Invalid JSON in records.json."
    return True, "Backup validated successfully."

def restore_from_backup(source_dir, dest_path, dry_run=False):
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    
    valid, msg = validate_backup(source_dir)
    if not valid:
        print(f"Restore aborted: {msg}")
        return False
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{os.path.basename(source_dir)}_{timestamp}.tar.gz" # Placeholder for actual tar logic or copy
    
    if dry_run:
        print(f"[DRY RUN] Would restore {source_dir} to {dest_path}")
        return True

    import shutil
    try:
        shutil.copytree(source_dir, dest_path)
        print(f"Restored from backup '{backup_name}' to '{dest_path}'.")
        
        # Optional: Remove old backups older than 7 days if desired logic exists here
        # For now, just successful restore.
        return True
    except Exception as e:
        print(f"Restore failed: {e}")
        return False
