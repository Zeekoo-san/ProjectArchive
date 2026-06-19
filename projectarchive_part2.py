# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: ProjectArchive
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional, Dict, Any

@dataclass
class Record:
    id: str
    title: str
    content: str
    created_at: date = field(default_factory=date.today)
    tags: List[str] = field(default_factory=list)
    attachments: Dict[str, str] = field(default_factory=dict)

@dataclass
class Decision(Record):
    decision_type: str
    rationale: Optional[str] = None
    stakeholders: List[str] = field(default_factory=list)

@dataclass
class TimelineEvent:
    date: date
    event_type: str
    description: str
    record_id: Optional[str] = None
