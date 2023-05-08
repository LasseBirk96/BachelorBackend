from dataclasses import dataclass


@dataclass
class BusinessGroupResource:
    Id: str 
    BusinessGroupId: str | None
    Type: str 
    Assigned: float 
    Consumed: float 
    Available: float
    Reserved: float 
    RecordDateTime: str
    RecordType: str 