from DatabaseLayer.Queries.businessgroup_queries import (
    persist_businessgroup,
    update_businessgroup,
    delete_businessgroup_by_id,
    get_all_businessgroups,
)
from Tests import mock_pytest_postgresql as mock
from LogicLayer.Entities.BusinessGroup import BusinessGroup


# ------------------------------------ START OF PERSIST BUSINESS GROUP TESTS ------------------------------------ #

# TEST IF A BUSINESS GROUP GETS PERSISTED CORRECTLY
def test_persist_businessgroup(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "BusinessGroup")
    # ARRANGE
    cursor = connection.cursor()
    commands = (mock.return_businessgroup_table(),)
    mock.execute_commands(commands, connection)
    instance = BusinessGroup(
        Id="1", Name="Novo Nordisk Information Technology", ShortName="NNIT"
    )
    # ACT
    persist_businessgroup(instance, connection)
    cursor.execute("SELECT * FROM BusinessGroup;")
    amount_of_muleapplication = len(cursor.fetchall())
    connection.close()
    # ASSERT
    assert amount_of_muleapplication == 1


# ------------------------------------ END OF PERSIST BUSINESS GROUP TESTS ------------------------------------ #

# ------------------------------------ START OF UPDATE BUSINESS GROUP TESTS ------------------------------------ #

# TEST IF A BUSINESS GROUP GETS UPDATED CORRECTLY
def test_update_businessgroup(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "BusinessGroup")
    # ARRANGE
    cursor = connection.cursor()
    commands = (
        mock.return_businessgroup_table(),
        "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('123', 'FL Smidth', 'FLS')",
    )
    mock.execute_commands(commands, connection)
    data = {"Id": "123", "Name": "Novo Nordisk"}
    # ACT
    update_businessgroup(data, connection)
    cursor.execute("SELECT name FROM BusinessGroup WHERE Id = '123'")
    name = cursor.fetchone()[0]
    connection.close()
    # ASSERT
    assert name == "Novo Nordisk"


# TEST IF A BUSINESS GROUP GETS UPDATED CORRECTLY ON MULTIPLE PARAMETERS
def test_update_businessgroup_multiple_params(
    connection=mock.establish_connection(),
):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "BusinessGroup")
    # ARRANGE
    cursor = connection.cursor()
    commands = (
        mock.return_businessgroup_table(),
        "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('123', 'FL Smidth', 'FLS')",
    )
    mock.execute_commands(commands, connection)
    data = {"Id": "123", "Name": "Novo Nordisk", "ShortName": "Novo"}
    # ACT
    update_businessgroup(data, connection)
    cursor.execute("SELECT name FROM BusinessGroup WHERE Id = '123'")
    name = cursor.fetchone()[0]
    cursor.execute("SELECT shortname FROM BusinessGroup WHERE Id = '123'")
    shortname = cursor.fetchone()[0]
    connection.close()
    # ASSERT
    assert (name == "Novo Nordisk") and (shortname == "Novo")


# ------------------------------------ END OF UPDATE BUSINESS GROUP TESTS ------------------------------------ #


# ------------------------------------ START OF DELETE BUSINESS GROUP TESTS ------------------------------------ #
# TEST IF A BUSINESS GROUP GETS DELETED CORRECTLY
def test_delete_businessgroup(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "BusinessGroup")
    # ARRANGE
    cursor = connection.cursor()
    commands = (
        mock.return_businessgroup_table(),
        "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('123', 'FL Smidth', 'FLS')",
        "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('134', 'Novo Nordisk', 'Novo')",
    )
    mock.execute_commands(commands, connection)
    id = "123"
    # ACT
    delete_businessgroup_by_id(id, connection)
    cursor.execute(
        "SELECT * FROM BusinessGroup",
    )
    amount_of_instances = len(cursor.fetchall())
    connection.close()
    # ASSERT
    assert amount_of_instances == 1


# ------------------------------------ END OF DELETE BUSINESS GROUP TESTS ------------------------------------ #


# ------------------------------------ START OF GET BUSINESS GROUP TESTS ------------------------------------ #
# TEST IF BUSINESS GROUP ARE RETURNED PROPERLY
def test_get_all_businessgroup(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "BusinessGroup")
    # ARRANGE
    commands = (
        mock.return_businessgroup_table(),
        "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('123', 'FL Smidth', 'FLS')",
        "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('134', 'Novo Nordisk', 'Novo')",
    )
    mock.execute_commands(commands, connection)
    data = {}
    # ACT
    amount_of_instances = len(get_all_businessgroups(data, connection))
    connection.close()
    # ASSERT
    assert amount_of_instances == 2


# TEST IF BUSINESS GROUPS ARE RETURNED PROPERLY ON MULTIPLE PARAMETERS (FILTERING)
def test_get_all_businessgroup_on_params(
    connection=mock.establish_connection(),
):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "BusinessGroup")
    # ARRANGE
    commands = (
        mock.return_businessgroup_table(),
        "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('123', 'FL Smidth', 'FLS')",
        "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('134', 'Novo Nordisk', 'Novo')",
        "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('341', 'Novo Sordisk', 'Novo')",
    )
    mock.execute_commands(commands, connection)
    data = {"ShortName": "Novo"}
    # ACT
    amount_of_instances = len(get_all_businessgroups(data, connection))
    connection.close()
    # ASSERT
    assert amount_of_instances == 2


# ------------------------------------ END OF GET BUSINESS GROUP TESTS ------------------------------------ #
