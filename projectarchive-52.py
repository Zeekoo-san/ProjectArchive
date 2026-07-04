# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: ProjectArchive
def format_timedelta(days: int, hours: int = 0) -> str:
    """Format a duration as 'X days Y hours'."""
    if days == 0 and hours == 0:
        return "now"
    parts = []
    if days > 0:
        parts.append(f"{days} day{'s' if days != 1 else ''}")
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    return " ".join(parts)

def normalize_tag(tag: str) -> str:
    """Convert a tag string to lowercase with hyphens."""
    return "-".join(word.lower() for word in tag.replace(" ", "").replace("_", "-").split("-"))

def generate_report_header(title: str, author: str, date: str) -> str:
    """Generate a markdown-style report header block."""
    lines = [f"# {title}", f"", f"Author: **{author}**", f"Date: {date}", ""]
    return "\n".join(lines)

def calculate_project_health(records_count: int, decisions_count: int, files_count: int) -> str:
    """Return a simple health status string based on record counts."""
    total = records_count + decisions_count + files_count
    if total == 0:
        return "Empty"
    ratio = (records_count / total) * 100
    if ratio > 50:
        return "Good - Active Records"
    elif ratio < 20:
        return "Warning - Low Record Activity"
    else:
        return "Stable"

def parse_decision_date(date_str: str) -> tuple[str, int]:
    """Parse a date string like 'YYYY-MM-DD' and return (year, month)."""
    parts = date_str.split("-")
    if len(parts) != 3:
        raise ValueError("Invalid date format. Expected YYYY-MM-DD.")
    year, month = parts[0], int(parts[1])
    return year, month

def filter_by_tag(records: list[str], target_tag: str) -> list[str]:
    """Filter a list of record strings that contain the normalized tag."""
    norm_tag = normalize_tag(target_tag)
    return [r for r in records if norm_tag in r.lower()]
