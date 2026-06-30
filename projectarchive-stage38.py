# === Stage 38: Add data integrity checks for broken references ===
# Project: ProjectArchive
def validate_references(db):
    broken = []
    for rec in db.records:
        if rec.get('file_id') and not any(r['id'] == rec['file_id'] for r in db.files):
            broken.append(f"Record {rec['id']} references missing file {rec['file_id']}")
        if rec.get('decision_ref') and not any(d['id'] == rec['decision_ref'] for d in db.decisions):
            broken.append(f"Record {rec['id']} references missing decision {rec['decision_ref']}")
    return broken

def repair_references(db, fixes=True):
    broken = validate_references(db)
    if not broken:
        print("All references valid.")
        return
    for msg in broken:
        rid, ref_id = msg.split()[-2], int(msg.split()[-1])
        # Attempt to find by partial name or tag if strict ID fails
        candidates = [r for r in db.records if str(r['id']) == rid]
        if not candidates: continue
        rec = candidates[0]
        print(f"Found broken ref in record {rec['id']}: {msg}")
        if fixes and rec.get('file_id') == ref_id:
            # Mark as orphaned instead of deleting data
            del rec['file_id']
        elif fixes and rec.get('decision_ref') == ref_id:
            del rec['decision_ref']
    return broken
