# === Stage 31: Add compact table rendering for long lists ===
# Project: ProjectArchive
def render_compact_table(records, max_cols=10):
    if not records: return ""
    cols = min(len(records[0]), max_cols)
    widths = [max(len(str(r[i])) for r in records) + 2 for i in range(cols)]
    header = " | ".join(f"{w:^{width}}" for w, width in zip(["ID", *["Val"]*(cols-1)], widths))
    lines = [header]
    for r in records:
        row = " | ".join(str(r[i])[:widths[i]-2].center(widths[i]) if i < cols else "" for i in range(cols))
        lines.append(row)
    return "\n".join(lines)
