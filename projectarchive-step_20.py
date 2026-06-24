# === Stage 20: Add duplicate detection for newly created records ===
# Project: ProjectArchive
from typing import Optional, List
import hashlib
from datetime import datetime

def detect_duplicates(records: List[dict], new_record: dict) -> tuple[str | None, bool]:
    """Detects if a new record is a duplicate of existing ones based on content hash."""
    def get_content_hash(record: dict) -> str:
        text = f"{record.get('title', '')} {record.get('content', '')}"
        return hashlib.sha256(text.encode()).hexdigest()

    new_hash = get_content_hash(new_record)
    for existing in records:
        if get_content_hash(existing) == new_hash:
            return "duplicate", True
    return None, False

def add_record_with_check(records: List[dict], new_record: dict) -> dict | None:
    """Adds a record only if it is not a duplicate."""
    dup_msg, is_dup = detect_duplicates(records, new_record)
    if is_dup:
        print(f"[WARN] Duplicate detected and skipped: {new_record.get('title', 'unknown')}")
        return None
    records.append(new_record)
    return new_record
