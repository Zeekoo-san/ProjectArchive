# === Stage 36: Add templates for quickly creating common records ===
# Project: ProjectArchive
from datetime import datetime
import json, os, uuid

ARCHIVE_DIR = "archive"
TEMPLATES_FILE = f"{ARCHIVE_DIR}/templates.json"

def get_templates():
    if not os.path.exists(TEMPLATES_FILE):
        return {
            "decision": {"type": "decision", "fields": ["title", "context", "rationale", "consequences"]},
            "record": {"type": "record", "fields": ["summary", "details", "references"]}
        }
    with open(TEMPLATES_FILE) as f: return json.load(f)

def save_templates(data):
    os.makedirs(ARCHIVE_DIR, exist_ok=True)
    with open(TEMPLATES_FILE, 'w') as f: json.dump(data, f, indent=2)

def create_record(template_name, **kwargs):
    templates = get_templates()
    if template_name not in templates: raise ValueError(f"Unknown template: {template_name}")
    tpl = templates[template_name]
    record_id = str(uuid.uuid4())[:8]
    entry = {"id": record_id, "timestamp": datetime.now().isoformat(), **tpl["fields"], **kwargs}
    return entry

def create_decision(title="New Decision", context="", rationale="", consequences=""):
    return create_record("decision", title=title, context=context, rationale=rationale, consequences=consequences)

def create_record_entry(summary="", details="", references=[]):
    return create_record("record", summary=summary, details=details, references=references)
