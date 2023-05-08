from DatabaseLayer.Queries.businessgroupresource_queries import (
    persist_businessgroupresource,
    update_businessgroupresource,
    delete_businessgroupresource_by_id,
    get_all_businessgroupsresources
)

from Tests import mock_pytest_postgresql as mock
from LogicLayer.Entities.BusinessGroupResource import BusinessGroupResource
from datetime import datetime, timezone



# ------------------------------------ START OF PERSIST BUSINESS GROUP RESOURCE TESTS ------------------------------------ #

# TEST IF A BUSINESS GROUP RESOURCE GETS PERSISTED CORRECTLY
def test_persist_businessgroup_resource(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "BusinessGroup")
    mock.clean_table(connection, "BusinessGroupResource")
    # ARRANGE
    cursor = connection.cursor()
    commands = (
        mock.return_businessgroup_table(),
        mock.return_businessgroup_resource_table(),
        )
    mock.execute_commands(commands, connection)
    instance = BusinessGroupResource(
       Id="1",
       BusinessGroupId=None,
       Type="Supplier",
       Assigned=10.0,
       Consumed=0.0,
       Available=0.0,
       Reserved=5.0,
       RecordDateTime= datetime.now(timezone.utc),
       RecordType="ORIGINAL"
    )
    # ACT
    persist_businessgroupresource(instance, connection)
    cursor.execute("SELECT * FROM BusinessGroupResource;")
    amount_of_muleapplication = len(cursor.fetchall())
    connection.close()
    # ASSERT
    assert amount_of_muleapplication == 1


# ------------------------------------ END OF PERSIST BUSINESS GROUP RESOURCE TESTS ------------------------------------ #

# ------------------------------------ START OF UPDATE BUSINESS GROUP RESOURCE TESTS ------------------------------------ #

# TEST IF A BUSINESS GROUP RESOURCE GETS UPDATED CORRECTLY
def test_update_businessgroupresource(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "BusinessGroup")
    mock.clean_table(connection, "BusinessGroupResource")
    # ARRANGE
    cursor = connection.cursor()
    commands = (
        mock.return_businessgroup_table(),
        mock.return_businessgroup_resource_table(),
        "INSERT INTO BusinessGroupResource (Id, BusinessGroupId, Type, Assigned, Consumed, Available, Reserved, RecordDateTime, RecordType) VALUES ('765', null, 'thing', '10','10', '11','0', CURRENT_DATE, 'ORIGINAL')",
    )
    mock.execute_commands(commands, connection)
    data = {"Id": "765", "Type": "Education"}
    # ACT
    update_businessgroupresource(data, connection)
    cursor.execute("SELECT type FROM BusinessGroupResource WHERE Id = '765'")
    type = cursor.fetchone()[0]
    connection.close()
    # ASSERT
    assert type == "Education"


# TEST IF A BUSINESS GROUP RESOURCE GETS UPDATED CORRECTLY ON MULTIPLE PARAMETERS
def test_update_businessgroupresource_multiple_params(
    connection=mock.establish_connection(),
):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "BusinessGroup")
    mock.clean_table(connection, "BusinessGroupResource")
    # ARRANGE
    cursor = connection.cursor()
    commands = (
        mock.return_businessgroup_table(),
        mock.return_businessgroup_resource_table(),
        "INSERT INTO BusinessGroupResource (Id, BusinessGroupId, Type, Assigned, Consumed, Available, Reserved, RecordDateTime, RecordType) VALUES ('765', null, 'thing', '10','10', '11','0', CURRENT_DATE, 'ORIGINAL')",
    )
    mock.execute_commands(commands, connection)
    data = {"Id": "765", "Type": "Education", "RecordType":"ESTIMATED"}
    # ACT
    update_businessgroupresource(data, connection)
    cursor.execute("SELECT type, recordtype FROM BusinessGroupResource WHERE Id = '765'")
    type = cursor.fetchone()[0]
    cursor.execute("SELECT recordtype FROM BusinessGroupResource WHERE Id = '765'")
    recordtype = cursor.fetchone()[0]
    connection.close()
    # ASSERT
    assert (type == "Education") and (recordtype == "ESTIMATED")


# ------------------------------------ END OF UPDATE BUSINESS GROUP RESOURCE TESTS ------------------------------------ #


# ------------------------------------ START OF DELETE BUSINESS GROUP RESOURCE TESTS ------------------------------------ #
# TEST IF A BUSINESS GROUP RESOURCE GETS DELETED CORRECTLY
def test_delete_businessgroupresource(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "BusinessGroup")
    mock.clean_table(connection, "BusinessGroupResource")
    # ARRANGE
    cursor = connection.cursor()
    commands = (
        mock.return_businessgroup_table(),
        mock.return_businessgroup_resource_table(),
            "INSERT INTO BusinessGroupResource (Id, BusinessGroupId, Type, Assigned, Consumed, Available, Reserved, RecordDateTime, RecordType) VALUES ('765', null, 'thing', '10','10', '11','0', CURRENT_DATE, 'ORIGINAL')",
            "INSERT INTO BusinessGroupResource (Id, BusinessGroupId, Type, Assigned, Consumed, Available, Reserved, RecordDateTime, RecordType) VALUES ('766', null, 'thing', '10','10', '11','0', CURRENT_DATE, 'ORIGINAL')",
    )
    mock.execute_commands(commands, connection)
    id = "765"
    # ACT
    delete_businessgroupresource_by_id(id, connection)
    cursor.execute(
        "SELECT * FROM BusinessGroupResource",
    )
    amount_of_instances = len(cursor.fetchall())
    connection.close()
    # ASSERT
    assert amount_of_instances == 1


# ------------------------------------ END OF DELETE BUSINESS GROUP RESOURCE TESTS ------------------------------------ #


# ------------------------------------ START OF GET BUSINESS GROUP RESOURCE TESTS ------------------------------------ #
# TEST IF BUSINESS GROUP RESOURCE ARE RETURNED PROPERLY
def test_get_all_businessgroup(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "BusinessGroup")
    mock.clean_table(connection, "BusinessGroupResource")
    # ARRANGE
    commands = (
        mock.return_businessgroup_table(),
        mock.return_businessgroup_resource_table(),
            "INSERT INTO BusinessGroupResource (Id, BusinessGroupId, Type, Assigned, Consumed, Available, Reserved, RecordDateTime, RecordType) VALUES ('765', null, 'thing', '10','10', '11','0', CURRENT_DATE, 'ORIGINAL')",
            "INSERT INTO BusinessGroupResource (Id, BusinessGroupId, Type, Assigned, Consumed, Available, Reserved, RecordDateTime, RecordType) VALUES ('766', null, 'thing', '10','10', '11','0', CURRENT_DATE, 'ORIGINAL')",
    )
    mock.execute_commands(commands, connection)
    data = {}
    # ACT
    amount_of_instances = len(get_all_businessgroupsresources(data, connection))
    connection.close()
    # ASSERT
    assert amount_of_instances == 2


# TEST IF BUSINESS GROUP RESOURCE ARE RETURNED PROPERLY ON MULTIPLE PARAMETERS (FILTERING)
def test_get_all_businessgroup_on_params(
    connection=mock.establish_connection(),
):
    mock.clean_table(connection, "BusinessGroup")
    mock.clean_table(connection, "BusinessGroupResource")
    # ARRANGE
    commands = (
        mock.return_businessgroup_table(),
        mock.return_businessgroup_resource_table(),
            "INSERT INTO BusinessGroupResource (Id, BusinessGroupId, Type, Assigned, Consumed, Available, Reserved, RecordDateTime, RecordType) VALUES ('765', null, 'Education', '10','10', '11','0', CURRENT_DATE, 'ORIGINAL')",
            "INSERT INTO BusinessGroupResource (Id, BusinessGroupId, Type, Assigned, Consumed, Available, Reserved, RecordDateTime, RecordType) VALUES ('766', null, 'Sandbox', '10','10', '11','0', CURRENT_DATE, 'ORIGINAL')",
            "INSERT INTO BusinessGroupResource (Id, BusinessGroupId, Type, Assigned, Consumed, Available, Reserved, RecordDateTime, RecordType) VALUES ('767', null, 'Education', '10','10', '11','0', CURRENT_DATE, 'ORIGINAL')",

    )
    mock.execute_commands(commands, connection)
    data = {"Type":"Education"}
    # ACT
    amount_of_instances = len(get_all_businessgroupsresources(data, connection))
    connection.close()
    # ASSERT
    assert amount_of_instances == 2

# ------------------------------------ END OF GET BUSINESS GROUP RESOURCE TESTS ------------------------------------ #
