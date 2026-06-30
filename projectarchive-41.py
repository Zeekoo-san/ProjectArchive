# === Stage 41: Add plain text import for a simple line-based format ===
# Project: ProjectArchive
class PlainTextImporter:
    def __init__(self, delimiter=','):
        self.delimiter = delimiter
        self._records = []

    def load(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                if not line.strip(): continue
                parts = line.rstrip('\n').split(self.delimiter)
                record = {
                    'id': len(self._records),
                    'data': parts[0] if len(parts) > 1 else '',
                    'timestamp': parts[1] if len(parts) > 2 else ''
                }
                self._records.append(record)

    def get_records(self):
        return self._records
