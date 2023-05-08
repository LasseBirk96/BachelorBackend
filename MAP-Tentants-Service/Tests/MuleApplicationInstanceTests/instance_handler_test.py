from LogicLayer.ServiceAPIs.MuleApplicationInstanceAPI.MuleApplicationInstanceHandler import (
    MuleApplicationInstanceHandler,
)
from Tests import mock_pytest_postgresql as mock
from flask import Flask

app = Flask(__name__)

# ------------------------------------ START OF API-HANDLER PERSIST MULEAPPLICATION-INSTANCE TESTS ------------------------------------ #

# TEST IF A 200 STATUS CODE GETS RETURNED IF A MULEAPPLICATION-INSTANCE IS PERSISTED WITH VALID PARAMETERS
def test_handle_persist_muleapplication_instance(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        mock.clean_table(connection, "MuleApplicationInstance")
        # ARRANGE
        data = {
            "MuleApplicationId": "QWERTY",
            "LinkStatus": "on",
            "Name": "AppName",
            "BusinessGroupShortName": "FLS",
            "Environment": "Sandbox",
            "TargetName": "blah",
            "TargetType": "bluh",
            "DeploymentStatus": "Deployed",
            "RuntimeVersion": "1.0",
            "WorkerSize": "0.1",
            "Workers": "2",
            "Region": "NA",
            "StaticIPCount": "1",
            "RecordType": "ORIGINAL",
        }
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            mock.return_muleapplication_instance_table(),
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('QWERTY', 'qqq-aaa-123', 'Anakin Skywalker', 'ANSK', 'Deathstar', '1', 'Deployed', 'Standard', null)",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            MuleApplicationInstanceHandler.handle_persist_muleapplication_instance(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 201


# TEST IF A 400 STATUS CODE GETS RETURNED IF A MULEAPPLICATION-INSTANCE IS PERSISTED WITH A DUPLICATE NAME
def test_handle_persist_muleapplication_instance_unique_violation(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        mock.clean_table(connection, "MuleApplicationInstance")
        # ARRANGE
        data = {
            "MuleApplicationId": None,
            "LinkStatus": "on",
            "Name": "Test",
            "BusinessGroupShortName": "FLS",
            "Environment": "Sandbox",
            "TargetName": "blah",
            "TargetType": "bluh",
            "DeploymentStatus": "Deployed",
            "RuntimeVersion": "1.0",
            "WorkerSize": "0.1",
            "Workers": "2",
            "Region": "NA",
            "StaticIPCount": "1",
            "RecordType": "ORIGINAL",
        }
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            mock.return_muleapplication_instance_table(),
            "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, TargetName, TargetType, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('1', null, 'None', 'Test', 'FLS', 'Sandbox', 'Cloud Hub', 'Good', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
        )
        mock.execute_commands(commands, connection)
        # ACT

        response_object = (
            MuleApplicationInstanceHandler.handle_persist_muleapplication_instance(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 400


# TEST IF A 400 STATUS CODE GETS RETURNED IF A MULEAPPLICATION-INSTANCE IS PERSISTED WITH A MULEAPPLICATION ID THAT DOESN'T EXIST
def test_handle_persist_muleapplication_instance_foreign_key_violation(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        mock.clean_table(connection, "MuleApplicationInstance")
        # ARRANGE
        data = {
            "MuleApplicationId": "ID_THAT_IS_NOT_IN_DB",
            "LinkStatus": "on",
            "Name": "Test",
            "BusinessGroupShortName": "FLS",
            "Environment": "Sandbox",
            "TargetName": "blah",
            "TargetType": "bluh",
            "DeploymentStatus": "Deployed",
            "RuntimeVersion": "1.0",
            "WorkerSize": "0.1",
            "Workers": "2",
            "Region": "NA",
            "StaticIPCount": "1",
            "RecordType": "ORIGINAL",
        }
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            mock.return_muleapplication_instance_table(),
        )
        mock.execute_commands(commands, connection)
        # ACT

        response_object = (
            MuleApplicationInstanceHandler.handle_persist_muleapplication_instance(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 400


# TEST IF A 400 STATUS CODE GETS RETURNED IF AN UNEXPECTED ERROR OCCURS
def test_handle_persist_muleapplication_instance_invalid_params(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        mock.clean_table(connection, "MuleApplicationInstance")
        # ARRANGE
        data = {
            "MuleApplicationId": "ID_THAT_IS_NOT_IN_DB",
            "LinkStatus": "on",
            "Name": "Test",
            "BusinessGroupShortName": "FLS",
            "Environment": "Sandbox",
            "TargetName": "blah",
            "TargetType": "bluh",
            "DeploymentStatus": "REALLYLONGANDNOTREALSTATUSCODE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
            "RuntimeVersion": "1.0",
            "WorkerSize": "0.1",
            "Workers": "2",
            "Region": "NA",
            "StaticIPCount": "1",
            "RecordType": "ORIGINAL",
        }
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            mock.return_muleapplication_instance_table(),
        )
        mock.execute_commands(commands, connection)
        # ACT

        response_object = (
            MuleApplicationInstanceHandler.handle_persist_muleapplication_instance(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 400


# TEST IF A 201 STATUS CODE GETS RETURNED IF THE MULEAPPLICATIONID IS NONE
def test_handle_persist_muleapplication_instance_no_id(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        mock.clean_table(connection, "MuleApplicationInstance")
        # ARRANGE
        data = {
            "MuleApplicationId": None,
            "LinkStatus": "on",
            "Name": "Test",
            "BusinessGroupShortName": "FLS",
            "Environment": "Sandbox",
            "TargetName": "blah",
            "TargetType": "bluh",
            "DeploymentStatus": "Deployed",
            "RuntimeVersion": "1.0",
            "WorkerSize": "0.1",
            "Workers": "2",
            "Region": "NA",
            "StaticIPCount": "1",
            "RecordType": "ORIGINAL",
        }
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            mock.return_muleapplication_instance_table(),
        )
        mock.execute_commands(commands, connection)
        # ACT

        response_object = (
            MuleApplicationInstanceHandler.handle_persist_muleapplication_instance(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 201


# ------------------------------------ END OF API-HANDLER PERSIST MULEAPPLICATION-INSTANCE TESTS ------------------------------------ #

# ------------------------------------ START OF API-HANDLER GET MULEAPPLICATION-INSTANCE TESTS ------------------------------------ #


# TEST IF A 200 STATUS CODE IS RETURNED IF NO DATA IS SEND
def test_handle_get_all_muleapplication_instances(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        mock.clean_table(connection, "MuleApplicationInstance")
        # ARRANGE
        data = {}
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            mock.return_muleapplication_instance_table(),
            "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, TargetName, TargetType, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('1', null, 'ON', 'Test', 'FLS', 'Sandbox', 'Cloud Hub', 'Good', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            MuleApplicationInstanceHandler.handle_get_all_muleapplicationinstances(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 200


# TEST IF A 200 STATUS CODE IS RETURNED IF A VALID PARAMETER IS SEND
def test_handle_get_all_muleapplication_instances_on_valid_parameters(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        mock.clean_table(connection, "MuleApplicationInstance")
        # ARRANGE
        data = {"Id": "1"}
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            mock.return_muleapplication_instance_table(),
            "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, TargetName, TargetType, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('1', null, 'None', 'werwer', 'FLS', 'Sandbox', 'Cloud Hub', 'goofd', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
            "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, TargetName, TargetType, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('2', null, 'None', 'THwerwerwing', 'FLS', 'Sandbox', 'Cloud Hub', 'goofd', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
            "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, TargetName, TargetType, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('3', null, 'None', 'THiewerwerng', 'FLS', 'Sandbox', 'Cloud Hub', 'goofd', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            MuleApplicationInstanceHandler.handle_get_all_muleapplicationinstances(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 200


# TEST IF A 400 STATUS CODE IS RETURNED IF A INVALID PARAMETER IS SEND
def test_handle_get_all_muleapplication_instances_on__invalid_parameters(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        mock.clean_table(connection, "MuleApplicationInstance")
        # ARRANGE
        data = {"sdfsdfsdf": "1"}
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            mock.return_muleapplication_instance_table(),
            "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, TargetName, TargetType, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('1', null, 'None', 'werwer', 'FLS', 'Sandbox', 'Cloud Hub', 'goofd', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
            "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, TargetName, TargetType, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('2', null, 'None', 'THwerwerwing', 'FLS', 'Sandbox', 'Cloud Hub', 'goofd', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
            "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, TargetName, TargetType, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('3', null, 'None', 'THiewerwerng', 'FLS', 'Sandbox', 'Cloud Hub', 'goofd', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            MuleApplicationInstanceHandler.handle_persist_muleapplication_instance(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 400


# ------------------------------------ END OF API-HANDLER GET MULEAPPLICATION-INSTANCE TESTS ------------------------------------ #


# ------------------------------------ START OF API-HANDLER DELETE MULEAPPLICATION-INSTANCE TESTS ------------------------------------ #

# TEST IF A 200 STATUS CODE IS RETURNED IF A VALID ID IS PROVIDED
def test_handle_delete_muleapplication_instance_by_id(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        mock.clean_table(connection, "MuleApplicationInstance")
        # ARRANGE
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            mock.return_muleapplication_instance_table(),
            "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, TargetName, TargetType, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('1', null, 'None', 'Test', 'FLS', 'Sandbox', 'Cloud Hub', 'goofd', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
        )
        mock.execute_commands(commands, connection)
        data = {"Id": "1"}
        # ACT

        response_object = (
            MuleApplicationInstanceHandler.handle_delete_muleapplicationinstance_by_id(
                data, connection
            )
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 200


# ------------------------------------ END OF API-HANDLER DELETE MULEAPPLICATION-INSTANCE TESTS ------------------------------------ #


# ------------------------------------ START OF API-HANDLER UPDATE MULEAPPLICATION-INSTANCE TESTS ------------------------------------ #

# TEST IF A 200 STATUS CODE IS RETURNED IF A VALID ID AND OTHER PARAMETER IS PROVIDED
def test_handle_update_muleapplication_instance(connection=mock.establish_connection()):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        mock.clean_table(connection, "MuleApplicationInstance")
        # ARRANGE
        data = {"Id": "1", "Environment": "NEW", "TargetType": "OTHER"}
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            mock.return_muleapplication_instance_table(),
            "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, TargetName, TargetType, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('1', null, 'None', 'Test', 'FLS', 'Sandbox', 'Cloud Hub', 'goofd', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            MuleApplicationInstanceHandler.handle_update_muleapplicationinstance(
                data, connection
            )
        )
        connection.close()
        assert response_object.status_code == 200


# TEST IF A 400 STATUS CODE IS RETURNED IF INVALID PARAMETERS ARE PROVIDED
def test_handle_update_muleapplication_instance_invalid_params(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        mock.clean_table(connection, "MuleApplicationInstance")
        # ARRANGE
        data = {"Id": "1", "rgergreg": "NEW", "TargetType": "OTHER"}
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            mock.return_muleapplication_instance_table(),
            "INSERT INTO MuleApplicationInstance (Id, MuleApplicationId, LinkStatus, Name, BusinessGroupShortName, Environment, TargetName, TargetType, DeploymentStatus, RunTimeVersion, WorkerSize, Workers, Region, StaticIpCount, RecordDateTime, RecordType) VALUES ('1', null, 'None', 'Test', 'FLS', 'Sandbox', 'Cloud Hub', 'goofd', 'Deployed', '132', '2.1', '1', 'Frank', 131, CURRENT_DATE, 'ESTIMATED')",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = (
            MuleApplicationInstanceHandler.handle_update_muleapplicationinstance(
                data, connection
            )
        )
        connection.close()
        assert response_object.status_code == 400


# ------------------------------------ END OF API-HANDLER UPDATE MULEAPPLICATION-INSTANCE TESTS ------------------------------------ #
