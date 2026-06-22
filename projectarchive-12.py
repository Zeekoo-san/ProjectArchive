# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: ProjectArchive
import json, os, sys

def load_json_safe(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[WARN] File not found: {path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"[ERROR] Malformed JSON in '{path}': {e.msg} at line {e.lineno}. Skipping.")
        return {}

def merge_records(source, target):
    for key, value in source.items():
        if isinstance(value, dict) and 'id' in value:
            existing = next((item for item in target.get('records', []) if item.get('id') == value['id']), None)
            if not existing:
                target.setdefault('records', []).append(value)
            else:
                existing.update({k: v for k, v in value.items() if k != 'id'})

if __name__ == "__main__":
    base_dir = "archive"
    files = [os.path.join(base_dir, f"{i}.json") for i in range(1, 6)]
    master = {"records": [], "decisions": [], "tags": set()}
    for path in files:
        data = load_json_safe(path)
        if not data: continue
        merge_records(data.get("records", {}), master)
        master["decisions"].extend(data.get("decisions", []))
        master["tags"].update(data.get("tags", set()))
    print(f"Processed {len(files)} files. Total records: {len(master['records'])}")
