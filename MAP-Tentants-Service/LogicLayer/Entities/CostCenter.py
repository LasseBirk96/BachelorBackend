from dataclasses import dataclass


@dataclass
class CostCenter:
    Id: str 
    Label: str
    ApproverName: str
    ApproverInitials: str
