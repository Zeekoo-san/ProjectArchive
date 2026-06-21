# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: ProjectArchive
class SearchIndex:
    def __init__(self):
        self._index = {}  # field_name -> {value_lower: [record_ids]}

    def index_record(self, record_id, fields_to_index):
        for field in fields_to_index:
            value = getattr(record, field) if hasattr(record, field) else str(getattr(record, 'content', ''))
            lower_val = value.lower()
            if lower_val not in self._index[field]:
                self._index.setdefault(field, {})[lower_val] = set()
            self._index[field][lower_val].add(record_id)

    def search(self, query, fields_to_search):
        results = set()
        for field in fields_to_search:
            if field not in self._index:
                continue
            lower_query = query.lower().strip()
            if lower_query in self._index[field]:
                results.update(self._index[field][lower_query])
        return list(results)

    def clear(self):
        self._index.clear()
