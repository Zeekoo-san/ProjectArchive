# === Stage 67: Add a function that returns key project metrics ===
# Project: ProjectArchive
def project_metrics(records, decisions, tags):
    """Return a dict of key project metrics based on current data."""
    total_records = len(records)
    total_decisions = len(decisions)
    unique_tags = set()
    for tag_list in tags.values():
        if isinstance(tag_list, list):
            unique_tags.update(tag_list)
        else:
            unique_tags.add(tag_list)
    return {
        "total_records": total_records,
        "total_decisions": total_decisions,
        "unique_tags_count": len(unique_tags),
        "records_per_decision_ratio": round(total_records / max(total_decisions, 1), 2),
        "tag_coverage": round(len(unique_tags) / max(total_records, 1) * 100, 2) if total_records > 0 else 0.0,
    }
