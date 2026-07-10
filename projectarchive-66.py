# === Stage 66: Add export of a short status dashboard ===
# Project: ProjectArchive
def export_status_dashboard(records, tags):
    """Export a short status dashboard summarizing project health."""
    total_records = len(records)
    active_tags = set(t for t in tags if "active" in str(t).lower())
    tag_count = len(active_tags)

    print(f"\n{'='*50}")
    print("  ProjectArchive - Status Dashboard")
    print(f"{'='*50}")
    print(f"Total records: {total_records}")
    print(f"Active tags: {tag_count}")
    if total_records > 0:
        avg_tags_per_record = tag_count / total_records
        print(f"Avg tags/record: {avg_tags_per_record:.2f}")
    print(f"Dash export complete.")
