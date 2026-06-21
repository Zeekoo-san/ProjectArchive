# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: ProjectArchive
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field
import re

@dataclass
class FilterConfig:
    status: Optional[str] = None
    category: Optional[str] = None
    owner: Optional[str] = None
    tag: Optional[str] = None
    
def apply_filters(records: List[Dict], config: FilterConfig) -> List[Dict]:
    if not records or not any(config): return records
    filtered = []
    for r in records:
        match = True
        if config.status and r.get('status') != config.status: match = False
        elif config.category and r.get('category') != config.category: match = False
        elif config.owner and r.get('owner') != config.owner: match = False
        elif config.tag:
            tags = r.get('tags', [])
            if not isinstance(tags, list): tags = [tags]
            if config.tag.lower() not in [t.lower() for t in tags]: match = False
        if match: filtered.append(r)
    return filtered

def parse_filter_args(args: List[str]) -> FilterConfig:
    cfg = FilterConfig()
    for arg in args:
        if arg.startswith('--status='): cfg.status = arg.split('=', 1)[1]
        elif arg.startswith('--category='): cfg.category = arg.split('=', 1)[1]
        elif arg.startswith('--owner='): cfg.owner = arg.split('=', 1)[1]
        elif arg.startswith('--tag='): cfg.tag = arg.split('=', 1)[1]
    return cfg

def run_archive_query(records: List[Dict], args: Optional[List[str]] = None) -> List[Dict]:
    if not records: return []
    config = parse_filter_args(args or [])
    return apply_filters(records, config)
