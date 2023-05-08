from LogicLayer.ServiceAPIs.MuleApplicationAPI.MuleApplicationHandler import MuleApplicationHandler
from Tests import mock_pytest_postgresql as mock
from flask import Flask
app = Flask(__name__)

# ------------------------------------ START OF API-HANDLER PERSIST MULEAPPLICATION TESTS ------------------------------------ #

# TEST IF A 200 STATUS CODE GETS RETURNED IF A MULEAPPLICATION IS PERSISTED WITH VALID PARAMETERS
def test_handle_persist_muleapplication(connection=mock.establish_connection()):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        # ARRANGE
        data = {
            "Name": "awp-12-d-aqsab-xp",
            "ContactPerson": "Lasse Birk",
            "ContactPersonInitials": "OBIK",
            "ProjectName": "Muletest",
            "OnboardingAgreementID": "2",
            "Status": "deployed",
            "Category": "Dev",
            "CostCenterLabel": "RS",
        }
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = MuleApplicationHandler.handle_persist_muleapplication(
            data, connection
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 201


# TEST IF A 400 STATUS CODE GETS RETURNED IF A MULEAPPLICATION IS PERSISTED WITH A DUPLICATE NAME
def test_handle_persist_muleapplication_unique_violation(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        # ARRANGE
        data = {
            "Name": "TESTNAME",
            "ContactPerson": "Lasse Birk",
            "ContactPersonInitials": "OBIK",
            "ProjectName": "Muletest",
            "OnboardingAgreementID": "2",
            "Status": "deployed",
            "Category": "Dev",
            "CostCenterLabel": "RS",
        }
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')""",
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('QWERTY', 'TESTNAME', 'Anakin Skywalker', 'ANSK', 'Deathstar', '1', 'Deployed', 'Standard', null)",
        )
        mock.execute_commands(commands, connection)
        # ACT

        response_object = MuleApplicationHandler.handle_persist_muleapplication(
            data, connection
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 400


# TEST IF A 400 STATUS CODE GETS RETURNED IF A MULEAPPLICATION IS PERSISTED WITH A LABEL THAT DOESN'T EXIST
def test_handle_persist_muleapplication_foreign_key_violation(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        # ARRANGE
        data = {
            "Name": "awp-12-d-aqsab-xp",
            "ContactPerson": "Lasse Birk",
            "ContactPersonInitials": "OBIK",
            "ProjectName": "Muletest",
            "OnboardingAgreementID": "2",
            "Status": "deployed",
            "Category": "Dev",
            "CostCenterLabel": "THISLABELISNOTREAL",
        }
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')""",
        )
        mock.execute_commands(commands, connection)
        # ACT

        response_object = MuleApplicationHandler.handle_persist_muleapplication(
            data, connection
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 400


# TEST IF A 400 STATUS CODE GETS RETURNED IF AN UNEXPECTED ERROR OCCURS
def test_handle_persist_muleapplication_invalid_params(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        # ARRANGE
        data = {
            "Name": "awp-12-d-aqsab-xp",
            "ContactPerson": "Lasse Birk",
            "ContactPersonInitials": "OBIK",
            "ProjectName": "Muletest",
            "OnboardingAgreementID": "2",
            "Status": "THISSTATUSCODEISWAYTOOLONGTOBEREALANDTHEFUNCTIONSHOULDFAIL",
            "Category": "Dev",
            "CostCenterLabel": "RS",
        }
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')""",
        )
        mock.execute_commands(commands, connection)
        # ACT

        response_object = MuleApplicationHandler.handle_persist_muleapplication(
            data, connection
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 400

# TEST IF A 201 STATUS CODE GETS RETURNED IF THE LABEL IS NONE
def test_handle_persist_muleapplication_no_label(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        # ARRANGE
        data = {
            "Name": "awp-12-d-aqsab-xp",
            "ContactPerson": "Lasse Birk",
            "ContactPersonInitials": "OBIK",
            "ProjectName": "Muletest",
            "OnboardingAgreementID": "2",
            "Status": "deployed",
            "Category": "Dev",
            "CostCenterLabel": None,
        }
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')""",
        )
        mock.execute_commands(commands, connection)
        # ACT

        response_object = MuleApplicationHandler.handle_persist_muleapplication(
            data, connection
        )
        connection.close()
        # ASSERT
        assert response_object.status_code == 201


# ------------------------------------ END OF API-HANDLER PERSIST MULEAPPLICATION TESTS ------------------------------------ #

# ------------------------------------ START OF API-HANDLER GET MULEAPPLICATION TESTS ------------------------------------ #


# TEST IF A 200 STATUS CODE IS RETURNED IF NO DATA IS SEND
def test_handle_get_all_muleapplications(connection=mock.establish_connection()):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        # ARRANGE
        data = {}
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            """INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES ('123', 'RS', 'Albus Dumbledore', 'ABEW')""",
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('QWERTY', 'qqq-aaa-123', 'Anakin Skywalker', 'ANSK', 'Deathstar', '1', 'Deployed', 'Standard', null)",
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('POIUYT', 'www-bbb-987', 'Barack Obama', 'BAOM', 'Healthcare', '2', 'Deployed', 'Proxy', null)",
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('FFFHHJ', 'sss-ccc-427', 'James Hetfield', 'JAHF', '72 Seasons', '3', 'Undeployed', 'Proxy', null)",
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('AZQWSX', 'xxx-xpa-627', 'Trey Parker', 'TRPK', 'South Park', '4', 'Undeployed', 'Proxy', 'RS')",
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('VFRTGB', 'nnn-ppp-888', 'Winston Churchill', 'WNCH', 'Win the war', '5', 'Failed', 'Proxy', 'RS')",
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('BGTYHN', 'vcx-xcv-413', 'Christopher Nolan', 'CHNO', 'Oppenheimer', '6', 'Deployed', 'Standard', null)",
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('NHYUJM', 'vsr-vsw-321', 'Tester Testerson', 'TEST', 'Test', '7', 'Failed', 'Standard', null)",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = MuleApplicationHandler.handle_get_all_muleapplications(
            data, connection
        )
        connection.close()
        assert response_object.status_code == 200


# TEST IF A 200 STATUS CODE IS RETURNED IF A VALID PARAMETER IS SEND
def test_handle_get_all_muleapplications_on_valid_parameters(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        # ARRANGE
        data = {"Id": "QWERTY"}
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('QWERTY', 'qqq-aaa-123', 'Anakin Skywalker', 'ANSK', 'Deathstar', '1', 'Deployed', 'Standard', null)",
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('POIUYT', 'www-bbb-987', 'Barack Obama', 'BAOM', 'Healthcare', '2', 'Deployed', 'Proxy', null)",
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('FFFHHJ', 'sss-ccc-427', 'James Hetfield', 'JAHF', '72 Seasons', '3', 'Undeployed', 'Proxy', null)",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = MuleApplicationHandler.handle_get_all_muleapplications(
            data, connection
        )
        connection.close()
        assert response_object.status_code == 200


# TEST IF A 400 STATUS CODE IS RETURNED IF A INVALID PARAMETER IS SEND
def test_handle_get_all_muleapplications_on__invalid_parameters(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        # ARRANGE
        data = {"THISFIELDISNOTREAL": "123"}
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('QWERTY', 'qqq-aaa-123', 'Anakin Skywalker', 'ANSK', 'Deathstar', '1', 'Deployed', 'Standard', null)",
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('POIUYT', 'www-bbb-987', 'Barack Obama', 'BAOM', 'Healthcare', '2', 'Deployed', 'Proxy', null)",
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('FFFHHJ', 'sss-ccc-427', 'James Hetfield', 'JAHF', '72 Seasons', '3', 'Undeployed', 'Proxy', null)",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = MuleApplicationHandler.handle_get_all_muleapplications(
            data, connection
        )
        connection.close()
        assert response_object.status_code == 400


# ------------------------------------ END OF API-HANDLER GET MULEAPPLICATION TESTS ------------------------------------ #


# ------------------------------------ START OF API-HANDLER DELETE MULEAPPLICATION TESTS ------------------------------------ #

# TEST IF A 200 STATUS CODE IS RETURNED IF A VALID ID IS PROVIDED
def test_handle_delete_muleapplication_by_id(connection=mock.establish_connection()):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        # ARRANGE
        data = {"Id": "THISIDISNOTAREALID"}
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('FFFHHJ', 'sss-ccc-427', 'James Hetfield', 'JAHF', '72 Seasons', '3', 'Undeployed', 'Proxy', null)",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = MuleApplicationHandler.handle_delete_muleapplication_by_id(
            data, connection
        )
        connection.close()
        assert response_object.status_code == 200


# ------------------------------------ END OF API-HANDLER DELETE MULEAPPLICATION TESTS ------------------------------------ #


# ------------------------------------ START OF API-HANDLER UPDATE MULEAPPLICATION TESTS ------------------------------------ #

# TEST IF A 200 STATUS CODE IS RETURNED IF A VALID ID AND OTHER PARAMETER IS PROVIDED
def test_handle_update_muleapplication(connection=mock.establish_connection()):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        # ARRANGE
        data = {"Id": "FFFHHJ", "ContactPersonInitials": "PPPP"}
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('FFFHHJ', 'sss-ccc-427', 'James Hetfield', 'JAHF', '72 Seasons', '3', 'Undeployed', 'Proxy', null)",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = MuleApplicationHandler.handle_update_muleapplication(
            data, connection
        )
        connection.close()
        assert response_object.status_code == 200


# TEST IF A 400 STATUS CODE IS RETURNED IF INVALID PARAMETERS ARE PROVIDED
def test_handle_update_muleapplication_invalid_params(
    connection=mock.establish_connection(),
):
    with app.app_context():
        # ENSURE CLEAN ENVIRONMENT
        mock.clean_table(connection, "CostCenter")
        mock.clean_table(connection, "MuleApplication")
        # ARRANGE
        data = {"NOTREAL": "123", "NOTREAL": "DD"}
        commands = (
            mock.return_costcenter_table(),
            mock.return_muleapplication_table(),
            "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('FFFHHJ', 'sss-ccc-427', 'James Hetfield', 'JAHF', '72 Seasons', '3', 'Undeployed', 'Proxy', null)",
        )
        mock.execute_commands(commands, connection)
        # ACT
        response_object = MuleApplicationHandler.handle_update_muleapplication(
            data, connection
        )
        connection.close()
        assert response_object.status_code == 400


# ------------------------------------ END OF API-HANDLER UPDATE MULEAPPLICATION TESTS ------------------------------------ #
