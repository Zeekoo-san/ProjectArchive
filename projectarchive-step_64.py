# === Stage 64: Add validation for relationship references ===
# Project: ProjectArchive
def _validate_references(records):
    """Cross-check every record's 'references' list against known IDs."""
    all_ids = set()
    for rec in records:
        if "id" in rec:
            all_ids.add(rec["id"])
    valid_refs = {r.get("id") for r in records if isinstance(r, dict) and r.get("type")}
    for rec in records:
        refs = rec.get("references", [])
        for ref in refs:
            if not isinstance(ref, (dict, str)):
                continue
            if isinstance(ref, dict):
                ref_id = ref.get("id")
                if ref_id and ref_id not in all_ids and ref_id not in valid_refs:
                    rec.setdefault("_warnings", []).append(
                        f"Reference id {ref_id} not found in any record."
                    )
            elif isinstance(ref, str) and ref.strip():
                pass  # bare strings treated as acceptable references
    return records
