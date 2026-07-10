# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: ProjectArchive
def render_changelog(records, decisions, files, tags, timelines):
    """Generate a compact changelog from project activity logs."""
    lines = ["ProjectArchive Changelog", "=" * 40]
    
    # Records section
    if records:
        lines.append("\n[Records]")
        for r in records[-10:]:
            lines.append(f"  - {r.get('date', 'N/A')}: {r.get('summary', '')}")
    
    # Decisions section
    if decisions:
        lines.append("\n[Decisions]")
        for d in decisions[-5:]:
            lines.append(f"  - {d.get('title', 'Decision')}: {d.get('rationale', '')[:60]}")
    
    # Files section
    if files:
        lines.append("\n[Files]")
        for f in files[-10:]:
            lines.append(f"  - {f['name']}: {f.get('size', 'N/A')} bytes")
    
    # Tags section
    if tags:
        lines.append("\n[Tags]")
        lines.append(f"  Active tags: {', '.join(tags[-10:])}")
    
    # Timelines section
    if timelines:
        lines.append("\n[Timelines]")
        for t in timelines[-5:]:
            lines.append(f"  - {t['name']}: {len(t['events'])} events")
    
    return "\n".join(lines)
