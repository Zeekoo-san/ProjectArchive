# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: ProjectArchive
def compare_snapshots(before, after):
    """Compare two snapshot dicts and return a summary of changes."""
    if before is None:
        return {"status": "new", "changes": {}, "description": "First snapshot — all fields are new."}
    if after is None:
        return {"status": "removed", "changes": {}, "description": "Snapshot removed between versions."}

    changes = {}
    for key in set(list(before.keys()) + list(after.keys())):
        b, a = before.get(key), after.get(key)
        if b == a:
            continue
        if isinstance(b, dict) and isinstance(a, dict):
            sub = compare_snapshots(b, a)
            changes[key] = sub["changes"]
        else:
            changes[key] = {"from": b, "to": a}

    return {
        "status": "updated" if changes else "unchanged",
        "changes": changes,
        "description": f"{len(changes)} field(s) changed.",
    }
