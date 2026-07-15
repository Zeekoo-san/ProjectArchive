# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: ProjectArchive
def _show_archive_report(archive):
    """Print a compact, human-readable summary of every section in an Archive."""
    print("=" * 60)
    print("  ProjectArchive – Summary Report")
    print("=" * 60)
    for key in ["records", "decisions", "files", "tags", "timelines", "reports"]:
        if key in archive:
            items = archive[key]
            if isinstance(items, dict):
                for name, entry in sorted(items.items()):
                    print(f"\n  [{name}]")
                    if hasattr(entry, "__len__"):
                        try:
                            print("    ", "\n    ".join(str(x) for x in list(entry)[:5]))
                        except Exception:
                            print("    ", entry)
            elif isinstance(items, list):
                for i, item in enumerate(items[:10]):
                    print(f"  - {item}")
    print("\n  End of report.")

if __name__ == "__main__":
    sample = {
        "records": {"intro": "Welcome to ProjectArchive."},
        "decisions": {"D-1": "Python only, no external libs"},
        "files": ["README.md", "archive.py"],
        "tags": ["education", "open-source", "python"],
        "timelines": [{"date": "2026-03-15", "event": "ProjectArchive created"}],
        "reports": {},
    }
    _show_archive_report(sample)
