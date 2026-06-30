# === Stage 40: Add plain text report export ===
# Project: ProjectArchive
def export_report_to_text(records, decisions, tags, timelines):
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(f"=== ProjectArchive Report ===\n\n")
        for r in records:
            f.write(f"[Record] {r.get('id')}: {r.get('title')} - {r.get('summary', '')}\n")
        f.write("\n--- Decisions ---\n")
        for d in decisions:
            f.write(f"[Decision] {d.get('id')}: {d.get('decision_title')}\n{d.get('rationale', '')}\n\n")
        f.write("--- Tags ---\n")
        for t in tags:
            f.write(f"{t['name']} ({t['count']})\n")
        f.write("\n--- Timelines ---\n")
        for tl in timelines:
            f.write(f"[Timeline] {tl.get('title')}: {', '.join(tl.get('events', []))}\n\n")
