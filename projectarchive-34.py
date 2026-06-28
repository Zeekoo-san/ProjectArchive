# === Stage 34: Add support for multiple local user profiles ===
# Project: ProjectArchive
import os, json, uuid
from pathlib import Path
PROFILE_DIR = Path(__file__).parent / ".profiles"
def init_profiles(): PROFILE_DIR.mkdir(exist_ok=True) if not PROFILE_DIR.exists() else None
def get_profile(name: str):
    path = PROFILE_DIR / f"{name}.json"
    return json.loads(path.read_text()) if path.exists() else {"id": uuid.uuid4().hex[:8], "name": name, "records": [], "tags": set(), "decisions": []}
def save_profile(name: str, data): (PROFILE_DIR / f"{name}.json").write_text(json.dumps(data, indent=2))
def add_record(profile_name: str, record): p = get_profile(profile_name); p["records"].append(record); save_profile(profile_name, p)
def tag_record(profile_name: str, record_id: str, tags): p = get_profile(profile_name); r = next((r for r in p["records"] if r.get("id") == record_id), None); [p["tags"].add(t) for t in tags]; save_profile(profile_name, p)
def add_decision(profile_name: str, decision): p = get_profile(profile_name); p["decisions"].append(decision); save_profile(profile_name, p)
