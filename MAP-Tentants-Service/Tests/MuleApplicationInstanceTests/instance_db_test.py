from DatabaseLayer.Queries.muleapplicationinstance_queries import (
    persist_muleapplication_instance,
    update_muleapplicationinstance,
    delete_muleapplicationinstance_by_id,
    get_all_muleapplication_instances,
)
from Tests import mock_pytest_postgresql as mock
from LogicLayer.Entities.MuleApplicationInstance import MuleApplicationInstance
from datetime import datetime, timezone

# ------------------------------------ START OF PERSIST MULEAPPLICATION-INSTANCE TESTS ------------------------------------ #

# TEST IF A MULEAPPLICATION-INSTANCE GETS PERSISTED CORRECTLY
def test_persist_muleapplication_instance():
    connection=mock.establish_connection()
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    mock.clean_table(connection, "MuleApplication")
    mock.clean_table(connection, "MuleApplicationInstance")
    # ARRANGE
    cursor = connection.cursor()
    commands = (
        mock.return_costcenter_table(),
        mock.return_muleapplication_table(),
        mock.return_muleapplication_instance_table(),
    )
    mock.execute_commands(commands, connection)
    instance = MuleApplicationInstance(
        Id="1",
        MuleApplicationId=None,
        LinkStatus="TEST",
        Name="TEST",
        BusinessGroupShortName="TEST",
        Environment="TEST",
        DeploymentStatus="TEST",
        RuntimeVersion="TEST",
        WorkerSize=0.2,
        Workers=1,
        Region="TEST",
        StaticIPCount=2,
        RecordDateTime=datetime.now(timezone.utc),
        RecordType="TEST",
    )
    instance1 = MuleApplicationInstance(
        Id="2",
        MuleApplicationId=None,
        LinkStatus="TEST",
        Name="TEST2",
        BusinessGroupShortName="TEST",
        Environment="TEST",
        DeploymentStatus="TEST",
        RuntimeVersion="TEST",
        WorkerSize=0.2,
        Workers=1,
        Region="TEST",
        StaticIPCount=2,
        RecordDateTime=datetime.now(timezone.utc),
        RecordType="TEST",
    )
    # ACT
    persist_muleapplication_instance(instance, connection)
    persist_muleapplication_instance(instance1, connection)
    cursor.execute("SELECT * FROM MuleApplicationInstance;")
    amount_of_muleapplication = len(cursor.fetchall())
    connection.close()
    # ASSERT
    assert amount_of_muleapplication == 2


# ------------------------------------ END OF PERSIST MULEAPPLICATION-INSTANCE TESTS ------------------------------------ #

# ------------------------------------ START OF UPDATE MULEAPPLICATION-INSTANCE TESTS ------------------------------------ #

# TEST IF A MULEAPPLICATION-INSTANCE GETS UPDATED CORRECTLY
def test_update_muleapplication_instance():
    connection=mock.establish_connection()
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    mock.clean_table(connection, "MuleApplication")
    mock.clean_table(connection, "MuleApplicationInstance")
    # ARRANGE
    cursor = connection.cursor()
    commands = (
        mock.return_costcenter_table(),
        mock.return_muleapplication_table(),
        mock.return_muleapplication_instance_table(),
        "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('1', null, 'None', 'AppName1', 'FLS', 'Good', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
    )
    mock.execute_commands(commands, connection)
    data = {"Id": "1", "RecordType": "NOTORIGINAL"}
    # ACT
    update_muleapplicationinstance(data, connection)
    cursor.execute("SELECT recordtype FROM MuleApplicationInstance WHERE Id = '1'")
    recordtype = cursor.fetchone()[0]
    connection.close()
    # ASSERT
    assert recordtype == "NOTORIGINAL"


# TEST IF A MULEAPPLICATION-INSTANCE GETS UPDATED CORRECTLY ON MULTIPLE PARAMETERS
def test_update_muleapplication_instance_multiple_params():
    connection=mock.establish_connection()
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    mock.clean_table(connection, "MuleApplication")
    mock.clean_table(connection, "MuleApplicationInstance")
    # ARRANGE
    cursor = connection.cursor()
    commands = (
        mock.return_costcenter_table(),
        mock.return_muleapplication_table(),
        mock.return_muleapplication_instance_table(),
        "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('1', null, 'None', 'AppName2', 'FLS', 'Good', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
    )
    mock.execute_commands(commands, connection)

    data = {"Id": "1", "RecordType": "NOTORIGINAL", "DeploymentStatus": "FAILED"}
    # ACT
    update_muleapplicationinstance(data, connection)
    cursor.execute("SELECT RecordType FROM MuleApplicationInstance WHERE Id = '1'")
    recordtype = cursor.fetchone()[0]
    cursor.execute(
        "SELECT DeploymentStatus FROM MuleApplicationInstance WHERE Id = '1'"
    )
    deploymentstatus = cursor.fetchone()[0]
    connection.close()
    # ASSERT
    assert (recordtype == "NOTORIGINAL") and (deploymentstatus == "FAILED")


# ------------------------------------ END OF UPDATE MULEAPPLICATION-INSTANCE TESTS ------------------------------------ #


# ------------------------------------ START OF DELETE MULEAPPLICATION-INSTANCE TESTS ------------------------------------ #
# TEST IF A MULEAPPLICATION-INSTANCE GETS DELETED CORRECTLY
def test_delete_muleapplication_instance():
    connection=mock.establish_connection()
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    mock.clean_table(connection, "MuleApplication")
    mock.clean_table(connection, "MuleApplicationInstance")
    # ARRANGE
    cursor = connection.cursor()
    commands = (
        mock.return_costcenter_table(),
        mock.return_muleapplication_table(),
        mock.return_muleapplication_instance_table(),
        "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('1', null, 'None', 'AppName3', 'FLS', 'Good', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
        "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('2', null, 'None', 'AppName4', 'FLS', 'Good', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
    )
    mock.execute_commands(commands, connection)
    id = "1"
    # ACT
    delete_muleapplicationinstance_by_id(id, connection)
    cursor.execute(
        "SELECT * FROM MuleApplicationInstance",
    )
    amount_of_instances = len(cursor.fetchall())
    connection.close()
    # ASSERT
    assert amount_of_instances == 1


# ------------------------------------ END OF DELETE MULEAPPLICATION-INSTANCE TESTS ------------------------------------ #


# ------------------------------------ START OF GET MULEAPPLICATION-INSTANCE TESTS ------------------------------------ #
# TEST IF MULEAPPLICATION-INSTANCES ARE RETURNED PROPERLY
def test_get_all_muleapplication_instances():
    connection=mock.establish_connection()
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    mock.clean_table(connection, "MuleApplication")
    mock.clean_table(connection, "MuleApplicationInstance")
    # ARRANGE
    commands = (
        mock.return_costcenter_table(),
        mock.return_muleapplication_table(),
        mock.return_muleapplication_instance_table(),
        "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('1', null, 'None', 'AppName5', 'FLS', 'Good', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
        "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('2', null, 'None', 'AppName6', 'FLS', 'Good', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
    )
    mock.execute_commands(commands, connection)
    data = {}
    # ACT
    amount_of_instances = len(get_all_muleapplication_instances(data, connection))
    connection.close()
    # ASSERT
    assert amount_of_instances == 2


# TEST IF MULEAPPLICATIONS ARE RETURNED PROPERLY ON MULTIPLE PARAMETERS (FILTERING)
def test_get_all_muleapplication_instances_on_params():
    connection=mock.establish_connection()
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    mock.clean_table(connection, "MuleApplication")
    mock.clean_table(connection, "MuleApplicationInstance")
    # ARRANGE
    commands = (
        mock.return_costcenter_table(),
        mock.return_muleapplication_table(),
        mock.return_muleapplication_instance_table(),
        "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('1', null, 'None', 'AppName7', 'FLS', 'Good', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
        "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('2', null, 'None', 'AppName8', 'FLS', 'Good', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
        "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('3', null, 'None', 'AppName9', 'NOVO', 'Good', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
    )
    mock.execute_commands(commands, connection)
    data = {"BusinessGroupShortName": "FLS"}
    # ACT
    amount_of_instances = len(get_all_muleapplication_instances(data, connection))
    connection.close()
    # ASSERT
    assert amount_of_instances == 2


# ------------------------------------ END OF GET MULEAPPLICATION-INSTANCE TESTS ------------------------------------ #
