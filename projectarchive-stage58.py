# === Stage 58: Add bulk update behavior for selected records ===
# Project: ProjectArchive
def bulk_update_records(self, updates: dict) -> list[dict]:
    """Apply a mapping of record_id → {field: new_value} across all stored records."""
    if not updates or not self._records:
        return []
    matched = 0
    for rec in self._records:
        rid = rec.get("id")
        if rid is None:
            continue
        if rid in updates:
            rec.update(updates[rid])
            matched += 1
    return [{"id": r["id"], "updated_fields": list(self._updates)} for _ in range(matched)]

def bulk_delete_records(self, record_ids: set) -> int:
    """Remove records whose ids are in *record_ids* and return the count removed."""
    before = len(self._records)
    self._records = [r for r in self._records if r.get("id") not in record_ids]
    return before - len(self._records)

def bulk_add_records(self, records: list[dict]) -> int:
    """Append *records* (each must have an 'id') and return the total added."""
    for rec in records:
        if "id" not in rec:
            raise ValueError("Every record must include a unique 'id'")
    self._records.extend(records)
    return len(records)
