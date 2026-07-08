# === Stage 63: Add relationships between records where useful ===
# Project: ProjectArchive
# Step 63 – Add relationship helpers to ProjectArchive
class Relationship:
    """A single link between two records."""
    def __init__(self, source_id, target_id, kind="references", description=""):
        self.source_id = source_id
        self.target_id = target_id
        self.kind = kind
        self.description = description

    def to_dict(self):
        return {
            "source": self.source_id,
            "target": self.target_id,
            "kind": self.kind,
            "description": self.description,
        }


class RelationshipManager:
    """Manages all relationships for a project."""
    def __init__(self):
        self._rel = []

    def add(self, src, tgt, kind="references", desc=""):
        self._rel.append(Relationship(src, tgt, kind, desc))

    def get_for_record(self, record_id):
        return [r for r in self._rel if r.source_id == record_id]

    def get_inverse_for_record(self, record_id):
        return [r for r in self._rel if r.target_id == record_id]

    def to_dict(self):
        return {"relationships": [r.to_dict() for r in self._rel]}


# Example usage: link two existing records
manager = RelationshipManager()
manager.add("record_04", "record_07", kind="extends", description="This record extends the earlier one")
