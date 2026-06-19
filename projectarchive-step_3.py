# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: ProjectArchive
def validate_record(record: dict) -> tuple[bool, str]:
    if not record.get("id"): return False, "Missing id"
    if not isinstance(record["title"], str): return False, "Title must be string"
    if len(record["title"]) < 1 or len(record["title"]) > 200: return False, "Title length invalid"
    required = ["id", "title", "content"]
    missing = [k for k in required if not record.get(k)]
    if missing: return False, f"Missing fields: {', '.join(missing)}"
    if isinstance(record["tags"], list):
        for tag in record["tags"]:
            if not isinstance(tag, str) or len(tag.strip()) == 0:
                return False, "Tags must be non-empty strings"
    if record.get("timeline"):
        for event in record["timeline"]:
            if not isinstance(event.get("date"), (int, float)) or event["date"] < 0:
                return False, "Timeline dates must be non-negative numbers"
    return True, ""

def sanitize_text(text: str) -> str:
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    if len(text) > 500: text = text[:497] + "..."
    return text
