# === Stage 35: Add active user switching and user-specific records ===
# Project: ProjectArchive
from dataclasses import dataclass, field
from typing import Dict, List, Optional
import json
from pathlib import Path

@dataclass
class UserRecord:
    user_id: str
    record_type: str  # 'decision', 'file', 'report'
    content: dict
    created_at: float = field(default_factory=time.time)
    
    def to_dict(self):
        return {k: v for k, v in self.__dict__.items() if not callable(v)}

class ProjectArchive:
    _users: Dict[str, List[UserRecord]] = {}
    _current_user: Optional[str] = None
    
    @classmethod
    def set_current_user(cls, user_id: str):
        cls._current_user = user_id
        
    @classmethod
    def get_current_user(cls) -> Optional[str]:
        return cls._current_user
        
    @classmethod
    def add_record(cls, record_type: str, content: dict):
        if not cls._current_user:
            raise RuntimeError("No active user set. Call set_current_user first.")
        
        record = UserRecord(
            user_id=cls._current_user,
            record_type=record_type,
            content=content
        )
        
        if cls._current_user not in cls._users:
            cls._users[cls._current_user] = []
            
        cls._users[cls._current_user].append(record)
        
    @classmethod
    def get_user_records(cls, user_id: str) -> List[UserRecord]:
        return cls._users.get(user_id, [])
        
    @classmethod
    def export_all(cls):
        output = {user: [r.to_dict() for r in records] for user, records in cls._users.items()}
        with open("archive_export.json", "w") as f:
            json.dump(output, f, indent=2)
