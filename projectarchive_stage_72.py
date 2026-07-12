# === Stage 72: Add Markdown report export ===
# Project: ProjectArchive
def export_to_markdown():
    """Export project archive to a single Markdown report."""
    md = []
    md.append("# ProjectArchive Report")
    for record in records:
        md.append(f"## {record.get('title', 'Untitled')}")
        md.append(record.get("body", ""))
        if "decisions" in record:
            for d in record["decisions"]:
                md.append(f"- **Decision**: {d}")
        if "tags" in record:
            md.append(f"*Tags*: {' '.join(tags)}")
        if "timeline" in record:
            timeline = record["timeline"]
            md.append(f"*Timeline*: {', '.join(timeline)}")
    for f in files:
        md.append(f"\n## File: `{f.get('name', 'unnamed')}`")
        md.append(f"**Path**: {f.get('path', '')}")
        md.append(f"**Content**:\n```\n{f.get('content', '')}\n```\n")
    return "\n".join(md)
