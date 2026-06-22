# === Stage 14: Add file load support with fallback demo data ===
# Project: ProjectArchive
def load_file(path: str) -> dict | None:
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        if not content.strip():
            return {"id": 0, "type": "empty", "content": "", "timestamp": datetime.now().isoformat()}
        lines = [l for l in content.splitlines() if l]
        return {
            "id": len(lines),
            "type": "text",
            "content": "\n".join(lines),
            "timestamp": datetime.now().isoformat(),
            "source": path,
            "tags": ["loaded"]
        }
    except FileNotFoundError:
        return {
            "id": 0,
            "type": "demo",
            "content": "# Demo Data\nThis file was not found.\nUse this placeholder for testing.",
            "timestamp": datetime.now().isoformat(),
            "source": path,
            "tags": ["fallback"]
        }
