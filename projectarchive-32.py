# === Stage 32: Add pagination helpers for long console output ===
# Project: ProjectArchive
def paginate_output(text, max_lines=15):
    if len(text.splitlines()) <= max_lines:
        print(text)
        return
    lines = text.splitlines()
    for i in range(0, len(lines), max_lines):
        chunk = '\n'.join(lines[i:i+max_lines])
        print(f"[Page {i//max_lines + 1}]")
        print(chunk)
