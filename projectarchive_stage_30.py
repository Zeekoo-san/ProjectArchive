# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: ProjectArchive
from datetime import datetime, timezone
import re
from typing import Optional, Tuple

def parse_date(date_str: str) -> Optional[datetime]:
    """Parse date string into a naive datetime object (UTC). Returns None on failure."""
    if not date_str or not isinstance(date_str, str):
        return None
    
    # Normalize whitespace and strip common prefixes/suffixes
    clean = re.sub(r'\s+', ' ', date_str.strip())
    
    patterns = [
        ("%Y-%m-%d", "YYYY-MM-DD"),
        ("%Y/%m/%d", "YYYY/MM/DD"),
        ("%d.%m.%Y", "DD.MM.YYYY"),
        ("%d/%m/%Y", "DD/MM/YYYY"),
        ("%B %d, %Y", "Month DD, YYYY"),
        ("%b %d, %Y", "Mon DD, YYYY"),
    ]
    
    for fmt, desc in patterns:
        try:
            dt = datetime.strptime(clean, fmt)
            return dt.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
            
    # Fallback to ISO format if standard ones fail but string looks like a date
    if clean.startswith(('20', '19')) and len(clean) >= 4:
        try:
            return datetime.fromisoformat(clean.replace('Z', '+00:00'))
        except ValueError:
            pass
            
    raise ValueError(f"Unable to parse date string: '{date_str}'. Supported formats include YYYY-MM-DD, DD.MM.YYYY, and ISO.")

def format_date(dt: Optional[datetime], fmt: str = "%Y-%m-%d") -> str:
    """Format a datetime object into a string. Returns empty string if input is None."""
    if dt is None:
        return ""
    try:
        return dt.strftime(fmt)
    except Exception as e:
        raise ValueError(f"Failed to format date {dt}: {e}")
