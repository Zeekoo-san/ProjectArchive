# === Stage 4: Implement create operations for the primary records ===
# Project: ProjectArchive
from datetime import datetime
def create_record(record_id: str, title: str, content: str, tags: list[str] = None) -> dict:
    if record_id in records_db: raise ValueError(f"Record {record_id} already exists")
    now = datetime.now().isoformat()
    new_record = {"id": record_id, "title": title, "content": content, "created_at": now, "tags": tags or []}
    records_db[record_id] = new_record
    return new_record

def create_decision(decision_id: str, context: str, decision: str, rationale: str) -> dict:
    if decision_id in decisions_db: raise ValueError(f"Decision {decision_id} already exists")
    now = datetime.now().isoformat()
    new_decision = {"id": decision_id, "context": context, "decision": decision, "rationale": rationale, "created_at": now}
    decisions_db[decision_id] = new_decision
    return new_decision

def create_file(file_id: str, filename: str, content_type: str, data: bytes) -> dict:
    if file_id in files_db: raise ValueError(f"File {file_id} already exists")
    now = datetime.now().isoformat()
    new_file = {"id": file_id, "filename": filename, "content_type": content_type, "data": data.hex(), "created_at": now}
    files_db[file_id] = new_file
    return new_file

def create_timeline_event(event_id: str, record_id: str, event_type: str, description: str) -> dict:
    if event_id in timeline_events_db: raise ValueError(f"Event {event_id} already exists")
    now = datetime.now().isoformat()
    new_event = {"id": event_id, "record_id": record_id, "type": event_type, "description": description, "timestamp": now}
    timeline_events_db[event_id] = new_event
    return new_event

def create_report(report_id: str, title: str, summary: str, metrics: dict) -> dict:
    if report_id in reports_db: raise ValueError(f"Report {report_id} already exists")
    now = datetime.now().isoformat()
    new_report = {"id": report_id, "title": title, "summary": summary, "metrics": metrics, "created_at": now}
    reports_db[report_id] = new_report
    return new_report
