from psycopg2 import connect


def establish_connection():
    return connect(dbname="postgres",user="postgres", password="123",port=5432, host="127.0.0.1")

def execute_commands(commands, connection):
    cursor = connection.cursor()
    try:
        for command in commands:
            cursor.execute(command)
        connection.commit()
    except (Exception) as error:
        print(error)
        
        
        
def clean_table(connection, table_name):
    query = "DROP TABLE IF EXISTS {} CASCADE;".format(table_name)
    cursor = connection.cursor()
    cursor.execute(query, (table_name,))
    connection.commit()
    


def return_costcenter_table():
    return str("""
            CREATE TABLE IF NOT EXISTS CostCenter (
                Id VARCHAR(100) primary KEY,
                Label VARCHAR(50) NOT NULL UNIQUE,         
                ApproverName VARCHAR(100) NOT NULL,
                ApproverInitials VARCHAR(10) NOT NULL)
            """,)
     

 
def return_muleapplication_table():
    return str("""
            CREATE TABLE IF NOT EXISTS MuleApplication (
                Id VARCHAR(100) primary KEY,
                Name VARCHAR(100) UNIQUE,
                ContactPerson VARCHAR(100),
                ContactPersonInitials VARCHAR(100),
                ProjectName VARCHAR(100),
                OnboardingAgreementID VARCHAR(50),
                Status VARCHAR(50),
                Category VARCHAR(50),
                CostCenterLabel VARCHAR(50) references CostCenter(Label) on update cascade ON DELETE CASCADE)
        """,)



def return_muleapplication_instance_table():
    return str("""
    CREATE TABLE IF NOT EXISTS MuleApplicationInstance (
        Id VARCHAR(100) primary KEY, 
        MuleApplicationId VARCHAR(100) references MuleApplication(Id) ON DELETE CASCADE ,
        LinkStatus VARCHAR(100),
        Name VARCHAR(100) UNIQUE,
        BusinessGroupShortName VARCHAR(10),
        Environment VARCHAR(50), 
        DeploymentStatus VARCHAR(50),
        RuntimeVersion VARCHAR(50),
        WorkerSize numeric,
        Workers SMALLINT,
        Region VARCHAR(50),
        StaticIPCount Integer,
        RecordDateTime DATE,
        RecordType VARCHAR(50)
    )
    
    """,)
    


def return_businessgroup_table():
    return str("""
    CREATE TABLE IF NOT EXISTS BusinessGroup (
        Id VARCHAR(100) primary KEY,
        Name VARCHAR(100) UNIQUE NOT NULL,
        ShortName VARCHAR(50) NOT NULL 
    )     
    """,)
    
    
def return_businessgroup_resource_table():
    return str("""
    CREATE TABLE IF NOT EXISTS BusinessGroupResource (
        Id VARCHAR(100) primary KEY,
        BusinessGroupId VARCHAR(100),
        Type VARCHAR(100),
        Assigned  numeric,
        Consumed  numeric,
        Available  numeric,
        Reserved  numeric,
        RecordDateTime DATE,
        RecordType VARCHAR(50),
        CONSTRAINT fk_BGID FOREIGN KEY(BusinessGroupId) REFERENCES BusinessGroup(Id) ON DELETE CASCADE
    )
    """,)