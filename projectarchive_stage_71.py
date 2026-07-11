# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: ProjectArchive
def seed_demo():
    """Populate ProjectArchive with deterministic sample records."""
    import random
    rng = random.Random(42)
    categories = ["bug", "feature", "enhancement"]
    tags_pool = ["python", "web", "ai", "cli", "docs", "test"]
    decisions_pool = [
        ("Use pytest instead of unittest", "pytest offers better fixtures"),
        ("Adopt Markdown for docs", "easier to render and share"),
        ("Add CI pipeline", "ensures tests run on every push"),
    ]
    records_data = [
        {"id": 1, "title": "Initial setup", "category": categories[0], "date": "2025-01-01"},
        {"id": 2, "title": "Add logging", "category": categories[1], "date": "2025-01-10"},
        {"id": 3, "title": "Fix edge case in parser", "category": categories[0], "date": "2025-02-05"},
    ]
    files_data = [
        {"id": 1, "name": "README.md", "size": 4096},
        {"id": 2, "name": "setup.py", "size": 2048},
        {"id": 3, "name": "requirements.txt", "size": 512},
    ]
    tags_data = [t for t in tags_pool]
    timelines_data = [
        ("2025-01-01", "Project started"),
        ("2025-01-15", "First release published"),
        ("2025-02-01", "Community contributions enabled"),
    ]
    reports_data = [
        {"id": 1, "title": "Q1 Status Report", "date": "2025-03-01"},
        {"id": 2, "title": "Architecture Review", "date": "2025-04-01"},
    ]
    for rec in records_data:
        rec["tags"] = [rng.choice(tags_pool) for _ in range(rng.randint(1, 3))]
    for dec in decisions_pool:
        dec["decision"] = dec[0]
        dec["rationale"] = dec[1]
        dec["date"] = "2025-01-20"
        dec["tags"] = ["python", "docs"] if "doc" in dec[0].lower() else ["test", "cli"]
    for f in files_data:
        f["extension"] = f.name.rsplit(".", 1)[-1]
    return {
        "records": records_data,
        "decisions": decisions_pool,
        "files": files_data,
        "tags": tags_data,
        "timelines": timelines_data,
        "reports": reports_data,
    }
