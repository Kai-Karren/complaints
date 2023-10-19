import uuid
from datetime import datetime
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List

@dataclass_json
@dataclass
class Location:
    street: str
    number: str
    city: str

@dataclass_json
@dataclass
class Complaint:
    summary: str
    category: str
    location: Location
    conversation_id: str

@dataclass_json
@dataclass
class Problem:
    creation_date: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    last_update: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    uuid: str = uuid.uuid4()
    users: List[str] = field(default_factory=list)
    conversations: List[str] = field(default_factory=list)
    status: str = ""
    summary: str  = ""
    category: str = ""
    location: Location = Location("", "", "")
    severity: str = ""
    reason: str = ""

