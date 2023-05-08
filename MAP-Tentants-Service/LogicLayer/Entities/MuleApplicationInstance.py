from dataclasses import dataclass


@dataclass
class MuleApplicationInstance:
    Id: str
    MuleAppName: str | None 
    Name: str 
    AppRegistration: str | None 
    BusinessGroup: str 
    EnvironmentName: str 
    DeploymentStatus: str 
    MuleVersion: str 
    WorkerWeight: str 
    Workers: str 
    Region: str 
    StaticIPEnabled: str | None 
    RecordDateTime: str 
    IsDeploymentWaiting: str | None 
    RecordType: str
