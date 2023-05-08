from LogicLayer.ServiceAPIs.BusinessGroupAPI.BusinessGroupHandler import BusinessGroupHandler
from Tests import mock_pytest_postgresql as mock
from flask import Flask

app = Flask(__name__)

# ------------------------------------ START OF API-HANDLER PERSIST BUSINESS GROUP TESTS ------------------------------------ #

# TEST IF A 200 STATUS CODE GETS RETURNED IF A BUSINESS GROUP IS PERSISTED WITH VALID PARAMETERS
def test_handle_persist_businessgroup(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "BusinessGroup")
        # ARRANGE
        data = {
            "Name":"Novo Nordisk",
            "ShortName":"Novo"
        }
        commands = (mock.return_businessgroup_table(),)
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            BusinessGroupHandler.handle_persist_businessgroup(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 201


# TEST IF A 400 STATUS CODE GETS RETURNED IF A BUSINESS GROUP IS PERSISTED WITH A DUPLICATE NAME
def test_handle_persist_businessgroup_unique_violation(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "BusinessGroup")
        # ARRANGE
        data = {
            "Name":"Novo Nordisk",
            "ShortName":"Novo"
        }
        commands = (mock.return_businessgroup_table(),
                    "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('345', 'Novo Nordisk', 'NOVO')",
                )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            BusinessGroupHandler.handle_persist_businessgroup(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 400


# TEST IF A 400 STATUS CODE GETS RETURNED IF AN UNEXPECTED ERROR OCCURS
def test_handle_persist_businessgroup_invalid_params(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "BusinessGroup")
        # ARRANGE
        data = {
            "Name":"Novo Nordiskerrrrrrrrrrrrrrrrrrrrg",
            "ShortName":"Novobgeeeeeeeeeeeeeeeeeedffffffffffffffffffffffffeeeeeeeeeergergerger"
        }
        commands = (mock.return_businessgroup_table(),)
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            BusinessGroupHandler.handle_persist_businessgroup(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 400



# ------------------------------------ END OF API-HANDLER PERSIST BUSINESS GROUP TESTS ------------------------------------ #

# ------------------------------------ START OF API-HANDLER GET BUSINESS GROUP TESTS ------------------------------------ #


# TEST IF A 200 STATUS CODE IS RETURNED IF NO DATA IS SEND
def test_handle_get_all_businessgroup(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "BusinessGroup")
        # ARRANGE
        data = {}
        commands = (mock.return_businessgroup_table(),)
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            BusinessGroupHandler.handle_get_all_businessgroups(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 200


# TEST IF A 200 STATUS CODE IS RETURNED IF A VALID PARAMETER IS SEND
def test_handle_get_all_businessgroup_on_valid_parameters(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "BusinessGroup")
        # ARRANGE
        data = {"shortname":"Novo"}
        commands = (
            mock.return_businessgroup_table(),
            "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('123', 'FL Smidth', 'FLS')",
            "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('134', 'Novo Nordisk', 'Novo')",
            "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('341', 'Novo Sordisk', 'Novo')",
            )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            BusinessGroupHandler.handle_get_all_businessgroups(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 200



# TEST IF A 400 STATUS CODE IS RETURNED IF A INVALID PARAMETER IS SEND
def test_handle_get_all_businessgroup_on__invalid_parameters(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "BusinessGroup")
        # ARRANGE
        data = {"ewfwefsfew":"Novo"}
        commands = (
            mock.return_businessgroup_table(),
            "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('123', 'FL Smidth', 'FLS')",
            "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('134', 'Novo Nordisk', 'Novo')",
            "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('341', 'Novo Sordisk', 'Novo')",
            )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            BusinessGroupHandler.handle_get_all_businessgroups(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 400


# ------------------------------------ END OF API-HANDLER GET BUSINESS GROUP TESTS ------------------------------------ #


# ------------------------------------ START OF API-HANDLER DELETE BUSINESS GROUP TESTS ------------------------------------ #

# TEST IF A 200 STATUS CODE IS RETURNED IF A VALID ID IS PROVIDED
def test_handle_delete_businessgroup_by_id(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "BusinessGroup")
        # ARRANGE
        commands = (
            mock.return_businessgroup_table(),
            "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('341', 'Novo Sordisk', 'Novo')", )
        mock.execute_commands(commands, connection)
        data = {"Id": "341"}
        # ACT

        response_object = (
            BusinessGroupHandler.handle_delete_businessgroup_by_id(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 200


# ------------------------------------ END OF API-HANDLER DELETE BUSINESS GROUP TESTS ------------------------------------ #


# ------------------------------------ START OF API-HANDLER UPDATE BUSINESS GROUP TESTS ------------------------------------ #

# TEST IF A 200 STATUS CODE IS RETURNED IF A VALID ID AND OTHER PARAMETER IS PROVIDED
def test_handle_update_businessgroup(connection=mock.establish_connection()):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "BusinessGroup")
        # ARRANGE
        data = {"Id":"134", "ShortName":"FLS"}
        commands = (
            mock.return_businessgroup_table(),
            "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('123', 'FL Smidth', 'FLS')",
            "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('134', 'Novo Nordisk', 'Novo')",
            "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('341', 'Novo Sordisk', 'Novo')",
            )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            BusinessGroupHandler.handle_update_businessgroup(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 200


# TEST IF A 400 STATUS CODE IS RETURNED IF INVALID PARAMETERS ARE PROVIDED
def test_handle_update_businessgroup_invalid_params(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "BusinessGroup")
        # ARRANGE
        data = {"Id":"134", "wegewgegw":"FLS"}
        commands = (
            mock.return_businessgroup_table(),
            "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('123', 'FL Smidth', 'FLS')",
            "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('134', 'Novo Nordisk', 'Novo')",
            "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('341', 'Novo Sordisk', 'Novo')",
            )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            BusinessGroupHandler.handle_update_businessgroup(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 400

# ------------------------------------ END OF API-HANDLER UPDATE BUSINESS GROUP TESTS ------------------------------------ #
