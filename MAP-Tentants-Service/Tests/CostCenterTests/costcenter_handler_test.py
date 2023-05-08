from LogicLayer.ServiceAPIs.CostCenterAPI.CostCenterHandler import CostCenterHandler
from Tests import mock_pytest_postgresql as mock
from flask import Flask

app = Flask(__name__)


# ------------------------------------ START OF API-HANDLER PERSIST COSTCENTER TESTS ------------------------------------ #

# TEST IF A 200 STATUS CODE GETS RETURNED IF A COSTCENTER IS PERSISTED WITH VALID PARAMETERS
def test_handle_persist_costcenter(connection=mock.establish_connection()):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        # ARRANGE
        data = {
            "Label": "PP",
            "ApproverName": "Mads Mikkelsen",
            "ApproverInitials": "MDMK",
        }

        mock.execute_commands((mock.return_costcenter_table(),), connection)
        # ACT

        response_object = CostCenterHandler.handle_persist_costcenter(data, connection)
        connection.close()
        # ASSERT
        assert response_object.status_code == 201


# TEST IF A 400 STATUS CODE IS RETURNED IF A DUPLICATE LABEL IS PERSISTED
def test_handle_persist_costcenter_unique_violation(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        # ARRANGE
        data = {
            "Label": "RS",
            "ApproverName": "Mads Mikkelsen",
            "ApproverInitials": "MDMK",
        }

        commands = (
            mock.return_costcenter_table(),
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')""",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = CostCenterHandler.handle_persist_costcenter(data, connection)
        connection.close()
        # ASSERT
        assert response_object.status_code == 400


# TEST IF A 400 STATUS CODE IS RETURNED IF A FIELD THAT IS NOT ALLOWED TO BE NULL IS
def test_handle_persist_costcenter_notnull_violation(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        # ARRANGE
        data = {
            "Label": None,
            "ApproverName": "Mads Mikkelsen",
            "ApproverInitials": "MDMK",
        }


        mock.execute_commands(mock.return_costcenter_table(), connection)
        # ACT
        response_object = CostCenterHandler.handle_persist_costcenter(data, connection)
        connection.close()
        # ASSERT
        assert response_object.status_code == 400


# TEST IF A 400 STATUS CODE IS RETURNED IF AN UNEXPECTED ERROR OCCURS
def test_handle_persist_costcenter_execption(connection=mock.establish_connection()):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        # ARRANGE
        data = {
            "Label": None,
            "ApproverName": "Mads Mikkelsen",
            "ApproverInitials": "MDMK",
        }

        mock.execute_commands(mock.return_costcenter_table(), connection)
        # ACT
        response_object = CostCenterHandler.handle_persist_costcenter(data, connection)
        connection.close()
        # ASSERT
        assert response_object.status_code == 400


# ------------------------------------ END OF API-HANDLER PERSIST COSTCENTER TESTS ------------------------------------ #


# ------------------------------------ START OF API-HANDLER GET COSTCENTER TESTS ------------------------------------ #

# TEST IF A 200 STATUS CODE IS RETURNED IF NO DATA IS SEND
def test_handle_get_all_costcenters(connection=mock.establish_connection()):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        # ARRANGE
        data = {}

        commands = (
            mock.return_costcenter_table(),
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')""",
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('234', 'GF', 'Albus Dumbledore', 'ABEW')""",
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('885', 'PO', 'Albus Dumbledore', 'ABEW')""",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = CostCenterHandler.handle_get_all_costcenters(data, connection)
        connection.close()
        assert response_object.status_code == 200


# TEST IF A 200 STATUS CODE IS RETURNED IF A VALID PARAMETER IS SEND
def test_handle_get_all_costcenters_on_valid_parameters(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        # ARRANGE
        data = {"Id": "123"}
        commands = (
            mock.return_costcenter_table(),
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')""",
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('234', 'GF', 'Albus Dumbledore', 'ABEW')""",
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('885', 'PO', 'Albus Dumbledore', 'ABEW')""",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = CostCenterHandler.handle_get_all_costcenters(data, connection)
        connection.close()
        assert response_object.status_code == 200


# TEST IF A 400 STATUS CODE IS RETURNED IF A INVALID PARAMETER IS SEND
def test_handle_get_all_costcenters_on__invalid_parameters(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        # ARRANGE
        data = {"rigregnrejng": "123"}
        commands = (
            mock.return_costcenter_table(),
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')""",
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('234', 'GF', 'Albus Dumbledore', 'ABEW')""",
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('885', 'PO', 'Albus Dumbledore', 'ABEW')""",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = CostCenterHandler.handle_get_all_costcenters(data, connection)
        connection.close()
        assert response_object.status_code == 400


# ------------------------------------ END OF API-HANDLER GET COSTCENTER TESTS ------------------------------------ #


# ------------------------------------ START OF API-HANDLER DELETE COSTCENTER TESTS ------------------------------------ #

# TEST IF A 200 STATUS CODE IS RETURNED IF A VALID ID IS PROVIDED
def test_handle_delete_costcenter_by_id(connection=mock.establish_connection()):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        # ARRANGE
        data = {"Id": "123"}
        commands = (
            mock.return_costcenter_table(),
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')""",
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('234', 'GF', 'Albus Dumbledore', 'ABEW')""",
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('885', 'PO', 'Albus Dumbledore', 'ABEW')""",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = CostCenterHandler.handle_delete_costcenter_by_id(
            data, connection
        )
        connection.close()
        assert response_object.status_code == 200


# ------------------------------------ END OF API-HANDLER DELETE TESTS ------------------------------------ #


# ------------------------------------ START OF API-HANDLER UPDATE TESTS ------------------------------------ #

# TEST IF A 200 STATUS CODE IS RETURNED IF A VALID ID AND OTHER PARAMETER IS PROVIDED
def test_handle_update_costcenter(connection=mock.establish_connection()):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        # ARRANGE
        data = {"Id": "123", "Label": "DD"}
        commands = (
            mock.return_costcenter_table(),
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')""",
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('234', 'GF', 'Albus Dumbledore', 'ABEW')""",
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('885', 'PO', 'Albus Dumbledore', 'ABEW')""",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = CostCenterHandler.handle_update_costcenter(data, connection)
        connection.close()
        assert response_object.status_code == 200


# TEST IF A 400 STATUS CODE IS RETURNED IF INVALID PARAMETERS ARE PROVIDED
def test_handle_update_costcenter_invalid_params(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        # ARRANGE
        data = {"sdfsdffsesfe": "123", "aasdasasdas": "DD"}
        commands = (
            mock.return_costcenter_table(),
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')""",
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('234', 'GF', 'Albus Dumbledore', 'ABEW')""",
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('885', 'PO', 'Albus Dumbledore', 'ABEW')""",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = CostCenterHandler.handle_update_costcenter(data, connection)
        connection.close()
        assert response_object.status_code == 400


# ------------------------------------ END OF API-HANDLER UPDATE TESTS ------------------------------------ #
