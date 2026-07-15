# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: ProjectArchive
def validate_all():
    """Run self-checks: schema, tag→file links, timeline continuity."""
    from datetime import datetime
    now = datetime.now()
    for d in records.values():
        assert isinstance(d['created_at'], datetime), f"{d['id']} missing created_at"
        if isinstance(d.get('resolved_at'), datetime):
            assert d['resolved_at'] >= d['created_at'], "resolved must be after created"

    # tag → file consistency
    for t in tags.values():
        if t['file_path']:
            assert t['file_path'].startswith('/'), f"{t['id']} relative path invalid"

    # timeline: every record has a position
    positions = set()
    for i, d in enumerate(records.values(), 1):
        assert d['position'] == i, f"{d['id']} position mismatch"
        positions.add(d['position'])
    assert len(positions) == len(records), "duplicate position exists"

    # demo: print summary
    print(f"\n=== ProjectArchive Self-Check ===")
    print(f"Records : {len(records)}  Tags : {len(tags)}  Files : {len(files)}  Timelines : {len(timelines)}")
    print(f"All validations passed at {now.isoformat()}")
