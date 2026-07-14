# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: ProjectArchive
def _ensure_dir(path: str) -> None:
    """Create *path* if it does not already exist."""
    import os
    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)


def _read_jsonl(file_path: str) -> list[dict]:
    """Read a JSON Lines file into a list of dicts."""
    records = []
    with open(file_path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def _write_jsonl(records: list[dict], file_path: str) -> None:
    """Write a list of dicts to a JSON Lines file."""
    import os
    _ensure_dir(os.path.dirname(file_path))
    with open(file_path, "w", encoding="utf-8") as fh:
        for rec in records:
            fh.write(json.dumps(rec) + "\n")


def _load_records() -> list[dict]:
    """Load all project records from the archive."""
    return _read_jsonl(ARCHIVE_DIR / "records.jsonl")


def _save_record(record: dict) -> None:
    """Append a single record to the archive."""
    records = _load_records()
    records.append(record)
    _write_jsonl(records, ARCHIVE_DIR / "records.jsonl")
