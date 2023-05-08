from DatabaseLayer.Queries.costcenter_queries import (
    persist_costcenter,
    update_costcenter,
    delete_costcenter_by_id,
    get_all_costcenters,
)
from LogicLayer.Entities.CostCenter import CostCenter
from Tests import mock_pytest_postgresql as mock


# ------------------------------------ START OF PERSIST COSTCENTER TESTS ------------------------------------ #

# TEST IF A COSTCENTER GETS PERSISTED
def test_persist_costcenter(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    # ARRANGE
    cursor = connection.cursor()

    mock.execute_commands((mock.return_costcenter_table(),), connection)
    costcenter = CostCenter(
        Id="1", Label="RS", ApproverName="Person McPerson", ApproverInitials="PM"
    )
    costcenter1 = CostCenter(
        Id="2", Label="DD", ApproverName="Test McTest", ApproverInitials="TM"
    )
    # ACT
    persist_costcenter(costcenter, connection)
    persist_costcenter(costcenter1, connection)
    cursor.execute("SELECT * FROM CostCenter;")
    amount_of_costcenters = len(cursor.fetchall())
    connection.close()
    # ASSERT
    assert amount_of_costcenters == 2


# ------------------------------------ END OF PERSIST COSTCENTER TESTS ------------------------------------ #


# ------------------------------------ START OF UPDATE COSTCENTER TESTS ------------------------------------ #

# TEST IF A COSTCENTER GETS UPDATED CORRECTLY
def test_update_center(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    # ARRANGE
    cursor = connection.cursor()
    queries = (
        mock.return_costcenter_table(),
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')",
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('654', 'AD', 'Severus Snape', 'SSPM')",
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('444', 'CS', 'Minerva McGonagol', 'MMCG')",
    )
    mock.execute_commands(queries, connection)
    data = {"Id": "123", "ApproverName": "Test Name"}
    # ACT
    update_costcenter(data, connection)
    cursor.execute("SELECT approvername FROM CostCenter WHERE Id = '123'")
    name = cursor.fetchone()[0]
    connection.close()
    # ASSERT
    assert name == "Test Name"


# TEST IF A COSTCENTER GETS UPDATED CORRECTLY - In this case we are testing multiple fields at a time
def test_update_costcenter_multiple_params(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    # ARRANGE
    cursor = connection.cursor()
    queries = (
        mock.return_costcenter_table(),
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')",
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('654', 'AD', 'Severus Snape', 'SSPM')",
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('444', 'CS', 'Minerva McGonagol', 'MMCG')",
    )
    mock.execute_commands(queries, connection)
    data = {"Id": "123", "ApproverName": "Test Name", "ApproverInitials": "TSNM"}
    # ACT
    update_costcenter(data, connection)
    cursor.execute("SELECT approverinitials FROM CostCenter WHERE Id = '123'")
    initials = cursor.fetchone()[0]
    cursor.execute("SELECT approvername FROM CostCenter WHERE Id = '123'")
    name = cursor.fetchone()[0]
    connection.close()
    # ASSERT
    assert (initials == "TSNM") and (name == "Test Name")


# # ------------------------------------ END OF UPDATE COSTCENTER TESTS ------------------------------------ #


# # ------------------------------------ START OF DELETE COSTCENTER TESTS ------------------------------------ #
# TEST IF A COSTCENTER GETS DELETED CORRECTLY
def test_delete_costcenter(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    # ARRANGE
    cursor = connection.cursor()
    queries = (
        mock.return_costcenter_table(),
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')",
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('654', 'AD', 'Severus Snape', 'SSPM')",
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('444', 'CS', 'Minerva McGonagol', 'MMCG')",
    )
    mock.execute_commands(queries, connection)
    id = "123"
    # ACT
    delete_costcenter_by_id(id, connection)
    cursor.execute(
        "SELECT * FROM CostCenter",
    )
    amount_of_costcenters = len(cursor.fetchall())
    connection.close()
    # ASSERT
    assert amount_of_costcenters == 2


# # ------------------------------------ END OF DELETE COSTCENTER TESTS ------------------------------------ #


# # ------------------------------------ START OF GET COSTCENTER TESTS ------------------------------------ #
# # TEST IF COSTCENTERS ARE RETURNED PROPERLY
def test_get_all_costcenter(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    # ARRANGE
    queries = (
        mock.return_costcenter_table(),
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')",
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('654', 'AD', 'Severus Snape', 'SSPM')",
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('444', 'CS', 'Minerva McGonagol', 'MMCG')",
    )
    mock.execute_commands(queries, connection)
    data = {}
    # ACT
    amount_of_costcenters = len(get_all_costcenters(data, connection))
    connection.close()
    # ASSERT
    assert amount_of_costcenters == 3


# TEST IF FILTERING WORKS
def test_get_all_costcenter_on_parameters(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    # ARRANGE
    queries = (
        mock.return_costcenter_table(),
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')",
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('654', 'AD', 'Severus Snape', 'SSPM')",
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('444', 'CS', 'Minerva McGonagol', 'MMCG')",
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('744', 'FD', 'Albus Dumbledore', 'ABEW')",
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('777', 'BV', 'Albus Dumbledore', 'DSAS')",
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('345', 'KK', 'Albus Dumbledore', 'ASDS')",
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('999', 'IU', 'Albus Dumbledore', 'FSSA')",
        "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('315', 'LP', 'Albus Dumbledore', 'AAAS')",
    )
    mock.execute_commands(queries, connection)
    data = {"ApproverInitials": "ABEW", "ApproverName": "Albus Dumbledore"}
    # ACT
    amount_of_costcenters = len(get_all_costcenters(data, connection))
    connection.close()
    # ASSERT
    assert amount_of_costcenters == 2


# # ------------------------------------ END OF GET COSTCENTER TESTS ------------------------------------ #
