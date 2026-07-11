# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: ProjectArchive
def clear_state():
    """Reset all project data to a clean state, protected by a confirmation flag."""
    if not _confirm("⚠️  This will delete ALL records, decisions, files, tags, timelines, and reports. Continue?"):
        return False
    for key in list(_db.keys()):
        del _db[key]
    print("✅ ProjectArchive has been cleared to a clean state.")
    return True
