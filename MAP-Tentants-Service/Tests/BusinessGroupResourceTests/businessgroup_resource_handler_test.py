from LogicLayer.ServiceAPIs.BusinessGroupResourceAPI.BusinessGroupResourceHandler import BusinessGroupResourceHandler
from Tests import mock_pytest_postgresql as mock
from flask import Flask

app = Flask(__name__)

# ------------------------------------ START OF API-HANDLER PERSIST BUSINESS GROUP TESTS ------------------------------------ #

# TEST IF A 201 STATUS CODE GETS RETURNED IF A BUSINESS GROUP IS PERSISTED WITH VALID PARAMETERS
def test_handle_persist_businessgroupresource(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "BusinessGroup")
        mock.clean_table(connection, "BusinessGroupResource")
        # ARRANGE
        request_body = {
            	"BusinessGroupId": '123',
	            "Type": "Sandbox",
	            "Assigned": 10,
	            "Consumed": 0,
	            "Available": 99,
	            "Reserved": 1,
	            "Recordtype": ""
        }
        commands = (
            mock.return_businessgroup_table(), 
            mock.return_businessgroup_resource_table(),
            "INSERT INTO BusinessGroup (Id, Name, ShortName) VALUES ('123', 'FL Smidth', 'FLS')",)
        mock.execute_commands(commands, connection)
        # ACT
        response_object = BusinessGroupResourceHandler.handle_persist_businessgroupresource(request_body, connection)
        
        connection.close()
        # ASSERT
        assert response_object.status_code == 201



# TEST IF A 400 STATUS CODE GETS RETURNED IF AN UNEXPECTED ERROR OCCURS
def test_handle_persist_businessgroupresource_invalid_params(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "BusinessGroup")
        mock.clean_table(connection, "BusinessGroupResource")
        # ARRANGE
        request_body = {
            	"BusinessGroupId": '123',
	            "Type": "Sanbox",
	            "Assigned": 10,
	            "Consumed": "THIS SHOULD BE NUMERIC",
	            "Available": 99,
	            "Reserved": 1,
	            "Recordtype": ""
        }
        commands = (mock.return_businessgroup_table(), mock.return_businessgroup_resource_table(),)
        mock.execute_commands(commands, connection)
        # ACT
        response_object = BusinessGroupResourceHandler.handle_persist_businessgroupresource(request_body, connection)
        
        connection.close()
        # ASSERT
        assert response_object.status_code == 400



# ------------------------------------ END OF API-HANDLER PERSIST BUSINESS GROUP TESTS ------------------------------------ #

# ------------------------------------ START OF API-HANDLER GET BUSINESS GROUP TESTS ------------------------------------ #


# TEST IF A 200 STATUS CODE IS RETURNED IF NO DATA IS SEND
def test_handle_get_all_businessgroupresource(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "BusinessGroup")
        mock.clean_table(connection, "BusinessGroupResource")
        # ARRANGE
        data = {}
        commands = (mock.return_businessgroup_table(), mock.return_businessgroup_resource_table(),)
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            BusinessGroupResourceHandler.handle_get_all_businessgroupsresources(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 200


# TEST IF A 200 STATUS CODE IS RETURNED IF A VALID PARAMETER IS SEND
def test_handle_get_all_businessgroupresource_on_valid_parameters(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "BusinessGroup")
        mock.clean_table(connection, "BusinessGroupResource")
        # ARRANGE
        data = {"Type":"GETFIELD"}
        commands = (mock.return_businessgroup_table(), 
                    mock.return_businessgroup_resource_table(),
                    "INSERT INTO BusinessGroupResource (Id, BusinessGroupId, Type, Assigned, Consumed, Available, Reserved, RecordDateTime, RecordType) VALUES ('765', null, 'GETFIELD', '10','10', '11','0', CURRENT_DATE, 'ORIGINAL')",)
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            BusinessGroupResourceHandler.handle_get_all_businessgroupsresources(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 200



# TEST IF A 400 STATUS CODE IS RETURNED IF A INVALID PARAMETER IS SEND
def test_handle_get_all_businessgroupresource_on__invalid_parameters(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "BusinessGroup")
        mock.clean_table(connection, "BusinessGroupResource")
        # ARRANGE
        data = {"rrgeg":"GweffffffffffffffffffffffffffffffffEewfffffffffffffffffTFIELD"}
        commands = (mock.return_businessgroup_table(), 
                    mock.return_businessgroup_resource_table(),
                    "INSERT INTO BusinessGroupResource (Id, BusinessGroupId, Type, Assigned, Consumed, Available, Reserved, RecordDateTime, RecordType) VALUES ('765', null, 'GETFIELD', '10','10', '11','0', CURRENT_DATE, 'ORIGINAL')",)
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            BusinessGroupResourceHandler.handle_get_all_businessgroupsresources(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 400


# ------------------------------------ END OF API-HANDLER GET BUSINESS GROUP TESTS ------------------------------------ #


# ------------------------------------ START OF API-HANDLER DELETE BUSINESS GROUP TESTS ------------------------------------ #

# TEST IF A 200 STATUS CODE IS RETURNED IF A VALID ID IS PROVIDED
def test_handle_delete_businessgroupresource_by_id(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "BusinessGroup")
        mock.clean_table(connection, "BusinessGroupResource")
        # ARRANGE
        commands = (mock.return_businessgroup_table(), 
                    mock.return_businessgroup_resource_table(),
                    "INSERT INTO BusinessGroupResource (Id, BusinessGroupId, Type, Assigned, Consumed, Available, Reserved, RecordDateTime, RecordType) VALUES ('765', null, 'GETFIELD', '10','10', '11','0', CURRENT_DATE, 'ORIGINAL')",)
        mock.execute_commands(commands, connection)
        data = {"Id": "765"}
        # ACT

        response_object = (
            BusinessGroupResourceHandler.handle_delete_businessgroupsresources_by_id(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 200


# ------------------------------------ END OF API-HANDLER DELETE BUSINESS GROUP TESTS ------------------------------------ #


# ------------------------------------ START OF API-HANDLER UPDATE BUSINESS GROUP TESTS ------------------------------------ #

# TEST IF A 200 STATUS CODE IS RETURNED IF A VALID ID AND OTHER PARAMETER IS PROVIDED
def test_handle_update_businessgroupresource(connection=mock.establish_connection()):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "BusinessGroup")
        mock.clean_table(connection, "BusinessGroupResource")
        # ARRANGE
        data = {"Id":"765", "Type":"NEWFIELD"}
        commands = (mock.return_businessgroup_table(), 
                    mock.return_businessgroup_resource_table(),
                    "INSERT INTO BusinessGroupResource (Id, BusinessGroupId, Type, Assigned, Consumed, Available, Reserved, RecordDateTime, RecordType) VALUES ('765', null, 'GETFIELD', '10','10', '11','0', CURRENT_DATE, 'ORIGINAL')",)
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            BusinessGroupResourceHandler.handle_update_businessgroupsresources(
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
        mock.clean_table(connection, "BusinessGroupResource")
        # ARRANGE
        data = {"Id":"765", "FIELD_THAT_DOESN'T_EXIST":"NEWFIELD"}
        commands = (mock.return_businessgroup_table(), 
                    mock.return_businessgroup_resource_table(),
                    "INSERT INTO BusinessGroupResource (Id, BusinessGroupId, Type, Assigned, Consumed, Available, Reserved, RecordDateTime, RecordType) VALUES ('765', '123', 'GETFIELD', '10','10', '11','0', CURRENT_DATE, 'ORIGINAL')",)
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            BusinessGroupResourceHandler.handle_update_businessgroupsresources(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 400

# ------------------------------------ END OF API-HANDLER UPDATE BUSINESS GROUP TESTS ------------------------------------ #
