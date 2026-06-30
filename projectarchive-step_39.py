# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: ProjectArchive
def repair_simple_integrity(records, decisions):
    missing_refs = set()
    for rec in records:
        if 'decision_id' in rec and rec['decision_id'] is not None:
            if rec['decision_id'] not in [d['id'] for d in decisions]:
                missing_refs.add(rec['decision_id'])
    orphans = [d for d in decisions if d.get('status') == 'archived' and d['created_at'] < min(r.get('timestamp', 0) for r in records)]
    for ref_id in missing_refs:
        recs_with_bad_ref = [r for r in records if r.get('decision_id') == ref_id]
        for r in recs_with_bad_ref:
            if 'decision_id' in r and r['decision_id'] is not None:
                del r['decision_id']
    for orphan in orphans:
        if 'id' in orphan:
            decisions.remove(orphan)
