# === Stage 60: Add saved views for frequently used filters ===
# Project: ProjectArchive
def save_view(view_name, filter_expr):
    """Persist a frequently-used filter as a named saved view."""
    views_dir = os.path.join(base_dir, "views")
    os.makedirs(views_dir, exist_ok=True)
    filename = f"{view_name}.json"
    filepath = os.path.join(views_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump({"name": view_name, "filter": filter_expr}, f, indent=2)

def load_views():
    """Load all saved views and return a dict of name -> filter."""
    views_dir = os.path.join(base_dir, "views")
    if not os.path.isdir(views_dir):
        return {}
    views = {}
    for fname in os.listdir(views_dir):
        if fname.endswith(".json"):
            filepath = os.path.join(views_dir, fname)
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            views[data["name"]] = data["filter"]
    return views

def register_default_views():
    """Register a few ready-to-use saved views."""
    defaults = {
        "all_records": {"kind": "all"},
        "recent_decisions": {"kind": "decision", "date_range": "last_30_days"},
        "active_files": {"kind": "file", "status": "active"},
        "pending_reviews": {"kind": "record", "status": "pending_review"},
        "tagged_items": {"kind": "all", "has_tag": True},
    }
    for name, filt in defaults.items():
        save_view(name, filt)
