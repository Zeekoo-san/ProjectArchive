# === Stage 13: Add file save support using a configurable path ===
# Project: ProjectArchive
import os, json, datetime

def save_record(record: dict, path: str = "archive.json") -> None:
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump([], f)
    records = []
    try:
        with open(path, 'r+', encoding='utf-8') as f:
            content = f.read()
            if content.strip():
                records = json.loads(content)
            else:
                f.seek(0); f.truncate(); json.dump([], f)
                return
    except json.JSONDecodeError:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump([], f)
            return
    
    record['timestamp'] = datetime.datetime.now().isoformat()
    if 'id' not in record:
        record['id'] = len(records) + 1
    records.append(record)

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
