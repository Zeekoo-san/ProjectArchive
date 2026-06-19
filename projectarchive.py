# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: ProjectArchive
from typing import Dict, List, Optional
import uuid
from datetime import datetime

class Record:
    def __init__(self, title: str, content: str, tags: List[str], author: str):
        self.id = str(uuid.uuid4())[:8]
        self.title = title
        self.content = content
        self.tags = tags
        self.author = author
        self.created_at = datetime.now().isoformat()

    def to_dict(self) -> Dict:
        return {k: v for k, v in self.__dict__.items()}

class ProjectArchive:
    def __init__(self):
        self.records: List[Record] = []
        self.decisions: Dict[str, Record] = {}
        self.files: Dict[str, str] = {}
        self.timelines: Dict[str, List[Dict]] = {}
        self.reports: List[Dict] = []

    def add_record(self, title: str, content: str, tags: Optional[List[str]] = None) -> Record:
        record = Record(title=title, content=content, tags=tags or [], author="system")
        self.records.append(record)
        return record

    def log_decision(self, decision_id: str, text: str) -> Dict:
        rec = Record(f"Decision #{decision_id}", text, ["decisions"], "admin")
        self.decisions[decision_id] = rec.to_dict()
        return {"status": "logged", "id": decision_id}

    def upload_file(self, filename: str, content: str) -> Dict:
        if not filename.endswith(('.txt', '.md', '.json')): raise ValueError("Unsupported type")
        self.files[filename] = content
        return {"status": "uploaded", "name": filename}

    def add_timeline_event(self, project_id: str, event_type: str, details: Dict) -> None:
        if project_id not in self.timelines: self.timelines[project_id] = []
        self.timelines[project_id].append({"type": event_type, **details})

    def generate_report(self) -> List[str]:
        lines = [f"=== ProjectArchive Report ({len(self.records)} records) ==="]
        for r in sorted(self.records, key=lambda x: x.created_at):
            lines.append(f"[{r.id}] {r.title} by {r.author}")
        return lines

archive = ProjectArchive()
archive.add_record("Welcome", "This is the start of our knowledge archive.", ["intro"])
archive.log_decision("DEC-001", "We will use in-memory storage for this demo.")
archive.upload_file("readme.md", "# Project Archive\nA simple tool.\n")
archive.add_timeline_event("proj-alpha", "init", {"status": "created"})
