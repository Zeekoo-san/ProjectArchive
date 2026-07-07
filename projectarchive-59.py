# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: ProjectArchive
def bulk_delete(records, confirm_flag=False):
    """Delete multiple records only when explicitly confirmed by the caller."""
    if not confirm_flag:
        raise PermissionError(
            "Bulk delete requires an explicit confirmation flag. "
            "Pass confirm_flag=True to proceed."
        )
    deleted = [r for r in records]
    return {"deleted": deleted, "count": len(deleted)}
