# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: ProjectArchive
def _split_and_tag(text: str) -> list[dict]:
    """Split a record body into lines and attach tags."""
    return [
        {"line": line, "tags": []} for line in text.splitlines(keepends=True)
    ]


def _format_timelines(entries: list[dict]) -> str:
    """Format timeline entries as 'YYYY-MM-DD | tag' blocks."""
    parts = []
    for entry in entries:
        if not entry.get("timestamp"):
            continue
        ts = entry["timestamp"][:10]
        tags = ", ".join(entry.get("tags", []))
        line = f"{ts} | {tags}" if tags else ts
        parts.append(line)
    return "\n".join(parts)


def _generate_report(records: list[dict]) -> dict:
    """Generate a summary report from the records."""
    by_tag = {}
    for rec in records:
        tags = rec.get("tags", [])
        if not tags:
            continue
        for tag in tags:
            by_tag.setdefault(tag, []).append(rec)

    return {
        "total_records": len(records),
        "tagged_records": sum(len(v) for v in by_tag.values()),
        "unique_tags": list(by_tag.keys()),
        "by_tag": {k: len(v) for k, v in by_tag.items()},
    }


def parse_and_report(text: str) -> dict:
    """Parse a record string and return its structured form plus report."""
    lines = _split_and_tag(text)
    if not lines:
        return {"parsed": None, "report": {}}

    entry = {"timestamp": "", "tags": [], "body": text}
    for line in lines:
        stripped = line["line"].strip()
        if stripped.startswith("Timestamp:"):
            entry["timestamp"] = stripped.split(":", 1)[1].strip()
        elif stripped.startswith("Tags:"):
            entry["tags"] = [t.strip() for t in stripped.split(":")[1].split(",")]

    report = _generate_report([entry])
    return {"parsed": entry, "report": report}
