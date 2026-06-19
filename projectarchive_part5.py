# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: ProjectArchive
def update_record(self, record_id: str, updates: dict) -> bool:
    if record_id not in self.records:
        raise ValueError(f"Record {record_id} does not exist")
    
    for key, value in updates.items():
        if key == "tags":
            current_tags = set(self.records[record_id].get("tags", []))
            new_tags = set(value)
            self.records[record_id]["tags"] = list(current_tags.union(new_tags))
        elif key == "status":
            self.records[record_id][key] = value
        else:
            if key in self.records[record_id]:
                self.records[record_id][key] = value
    
    return True
