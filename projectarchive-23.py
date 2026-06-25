# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: ProjectArchive
def _get_tags(record):
    return record.get('tags', []) if isinstance(record, dict) else []

def tag_record(record, action='add', tags=None):
    current = _get_tags(record)
    if action == 'add':
        for t in (tags or []):
            if t not in current:
                current.append(t)
    elif action == 'remove':
        current[:] = [t for t in current if t != tags]
    return record

def summarize_by_tags(records, tag=None):
    filtered = records if tag is None else [r for r in records if tag in _get_tags(r)]
    counts = {}
    for r in filtered:
        for t in _get_tags(r):
            counts[t] = counts.get(t, 0) + 1
    return sorted(counts.items(), key=lambda x: -x[1])
