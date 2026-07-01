# === Stage 43: Add CSV import for the primary record type ===
# Project: ProjectArchive
import csv, json, os
from datetime import datetime
def load_csv_records(source_path: str, schema_file: str = None):
    records = []
    if not os.path.exists(source_path): return records
    with open(source_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                rec = {k.strip(): v.strip() for k, v in row.items()}
                if 'timestamp' not in rec: rec['timestamp'] = datetime.utcnow().isoformat()
                records.append(rec)
            except Exception: pass
    return records

def merge_csv_to_archive(csv_path: str, archive_dir: str):
    os.makedirs(archive_dir, exist_ok=True)
    meta_file = os.path.join(archive_dir, 'import_meta.json')
    if not os.path.exists(meta_file):
        with open(meta_file, 'w', encoding='utf-8') as f: json.dump({'imports': []}, f)
    meta = json.load(open(meta_file))
    records = load_csv_records(csv_path)
    if not records: return 0
    for rec in records:
        key = f"{rec.get('id', 'unknown')}_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"
        with open(os.path.join(archive_dir, f'{key}.json'), 'w', encoding='utf-8') as f:
            json.dump(rec, f)
    meta['imports'].append({'file': csv_path, 'count': len(records), 'date': datetime.utcnow().isoformat()})
    with open(meta_file, 'w', encoding='utf-8') as f: json.dump(meta, f)
    return len(records)
