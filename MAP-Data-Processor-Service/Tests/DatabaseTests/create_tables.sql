    CREATE TABLE IF NOT EXISTS CostCenter (
        Id VARCHAR(100) primary KEY,
        Label VARCHAR(50) NOT NULL UNIQUE,
        ApproverName VARCHAR(100) NOT NULL,
        ApproverInitials VARCHAR(10) NOT NULL
    );
    CREATE TABLE IF NOT EXISTS MuleApplication (
        Id VARCHAR(100) primary KEY,
	    Name VARCHAR(100) UNIQUE,
        ContactPerson VARCHAR(100),
        ContactPersonInitials VARCHAR(100),
        ProjectName VARCHAR(100),
        OnboardingAgreementID VARCHAR(50),
        Status VARCHAR(50),
        Category VARCHAR(50),
        CostCenterLabel VARCHAR(50) references CostCenter(Label) on update cascade ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS MuleApplicationInstance (
        MuleAppName VARCHAR(100) references MuleApplication(Name) on update cascade ON DELETE CASCADE,
        Name VARCHAR(100),
        AppRegistration VARCHAR(100),
        BusinessGroup VARCHAR(100),
        EnvironmentName VARCHAR(50), 
        DeploymentStatus VARCHAR(50),
        MuleVersion VARCHAR(50),
        WorkerWeight numeric,
        Workers SMALLINT,
        Region VARCHAR(50),
        staticIPsEnabled BOOL,
        RecordDateTime timestamp default current_timestamp,
        isDeploymentWaiting BOOL,
        RecordType VARCHAR(50) default null
    );



    CREATE TABLE IF NOT EXISTS StageingTable (
        Id VARCHAR(100) primary KEY,
        AnyPointData jsonb,
        DateAdded timestamp default timezone('utc', now()),
        Status VARCHAR(30) default 'Not Processed',
        dateProcessed timestamp default null
        )