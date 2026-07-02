# === Stage 46: Add a schema version field and migration helper ===
# Project: ProjectArchive
from pathlib import Path
import json, uuid
from datetime import datetime

SCHEMA_VERSION = 2
MIGRATION_LOGS = []

def migrate_record(record: dict) -> dict:
    if record.get("__schema_version", 1) < SCHEMA_VERSION:
        record["__schema_version"] = SCHEMA_VERSION
        if "created_at" not in record and "id" in record:
            record["created_at"] = datetime.fromisoformat(record["id"].split("-")[0]).strftime("%Y-%m-%dT%H:%M:%S")
        MIGRATION_LOGS.append(f"Migrated {record.get('type', 'unknown')} #{record.get('id')[:8]} to v{SCHEMA_VERSION}")
    return record

def ensure_schema_compliance(path: Path) -> None:
    if not path.exists(): return
    with open(path, "r", encoding="utf-8") as f: data = json.load(f)
    for item in data.get("records", []): migrate_record(item)
    with open(path, "w", encoding="utf-8") as f: json.dump(data, f, ensure_ascii=False, indent=2)
