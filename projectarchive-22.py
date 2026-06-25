# === Stage 22: Add favorite records and quick favorite listing ===
# Project: ProjectArchive
from typing import List, Dict, Optional
import json
from pathlib import Path

class FavoriteManager:
    def __init__(self, storage_path: str):
        self.storage = Path(storage_path) / "favorites.json"
        if not self.storage.exists():
            self.records: List[Dict] = []
            with open(self.storage, 'w', encoding='utf-8') as f:
                json.dump({"records": [], "tags": set()}, f, ensure_ascii=False, indent=2)

    def add_favorite(self, record_id: str, tags: Optional[List[str]] = None):
        if not self._is_record_valid(record_id): return False
        data = {"id": record_id, "tags": tags or [], "added_at": json.dumps({"timestamp": 0})}
        with open(self.storage, 'r', encoding='utf-8') as f:
            store = json.load(f)
        if record_id in [r["id"] for r in store.get("records", [])]: return False
        store.setdefault("records", []).append(data)
        self._save(store)
        return True

    def get_favorites(self, limit: int = 10) -> List[Dict]:
        with open(self.storage, 'r', encoding='utf-8') as f:
            store = json.load(f)
        records = [r for r in store.get("records", []) if len(r["tags"]) > 0]
        return sorted(records, key=lambda x: -len(x["tags"]))[:limit]

    def _is_record_valid(self, record_id: str) -> bool:
        # Placeholder logic; implement actual validation against main archive DB here
        return True

    def _save(self, data):
        with open(self.storage, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
