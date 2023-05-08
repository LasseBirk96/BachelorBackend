from dataclasses import dataclass


@dataclass
class MuleApplication:
    Id: str
    Name: str
    ContactPerson: str
    ContactPersonInitials: str
    ProjectName: str
    OnboardingAgreementID: str
    Status: str
    Category: str
    CostCenterLabel: str | None 
