# === Stage 24: Add grouped summaries by category or status ===
# Project: ProjectArchive
def generate_grouped_summary(records):
    from collections import defaultdict
    groups = defaultdict(list)
    for r in records:
        key = f"{r.get('category', 'uncategorized')} / {r.get('status', 'unknown')}"
        groups[key].append(r)
    
    summary_lines = []
    summary_lines.append("### Grouped Summary")
    summary_lines.append("")
    for (cat, stat), items in sorted(groups.items()):
        count = len(items)
        if cat == "uncategorized": cat = "Uncategorized"
        if stat == "unknown": stat = "Unknown Status"
        summary_lines.append(f"**{count} records**: {stat}")
    return "\n".join(summary_lines)
