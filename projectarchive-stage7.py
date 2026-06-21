# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: ProjectArchive
def format_record(record):
    return f"[{record['id']}] {record.get('title', 'No Title')} | Tags: {', '.join(record.get('tags', []))} | Date: {record.get('date', '')}"

def format_decision(decision):
    status = "✅" if decision.get("status") == "accepted" else "⏳"
    return f"{status} [{decision['id']}] {decision.get('title')} - Decision by: {decision.get('author')}\n   Context: {decision.get('context', '')[:50]}...\n   Rationale: {decision.get('rationale', 'N/A')}"

def format_timeline_event(event):
    return f"{event['date']} — {event.get('type', 'Event'):12} : {event.get('description', 'No description')}"

def format_report_section(section, data):
    lines = [f"\n=== {section.upper()} ==="]
    if isinstance(data, list) and len(data) > 0:
        for item in data[:5]:
            lines.append(f"• {item}")
        if len(data) > 5:
            lines.append(f"... and {len(data)-5} more")
    else:
        lines.append(str(data))
    return "\n".join(lines)

def format_file_entry(file_info):
    size = file_info.get('size', '0')
    ext = file_info.get('extension', '')
    return f"📄 {file_info['name']} ({ext}) • Size: {size} bytes • Uploaded by: {file_info.get('uploader', 'Unknown')}"

def format_tag_cloud(tags):
    if not tags:
        return "No tags yet."
    sorted_tags = sorted(set(tags), key=lambda x: tags.count(x), reverse=True)
    return ", ".join(f"{tag} ({tags.count(tag)})" for tag in sorted_tags[:10])
