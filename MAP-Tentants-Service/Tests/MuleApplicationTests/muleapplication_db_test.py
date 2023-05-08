from DatabaseLayer.Queries.muleapplication_queries import (
    persist_muleapplication,
    update_muleapplication,
    delete_muleapplication_by_id,
    get_all_muleapplications,
)
from Tests import mock_pytest_postgresql as mock
from LogicLayer.Entities.MuleApplication import MuleApplication


# ------------------------------------ START OF PERSIST MULEAPPLICATION TESTS ------------------------------------ #

# TEST IF A MULEAPPLICATION GETS PERSISTED CORRECTLY
def test_persist_muleapplication(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    mock.clean_table(connection, "MuleApplication")
    # ARRANGE
    cursor = connection.cursor()
    commands = (
        mock.return_costcenter_table(),
        mock.return_muleapplication_table(),
    )
    mock.execute_commands(commands, connection)
    muleapplication = MuleApplication(
        Id="1",
        Name="Muleapp-aqwe-123-aa",
        ContactPerson="Mads Mikkelsen",
        ContactPersonInitials="MKDK",
        ProjectName="Sultans Of Swing",
        OnboardingAgreementID="1",
        Status="Deployed",
        Category="Sandbox",
        CostCenterLabel=None,
    )
    muleapplication1 = MuleApplication(
        Id="2",
        Name="Muleapp-twer-144-fg",
        ContactPerson="Mads Mikklsen",
        ContactPersonInitials="FDAS",
        ProjectName="Sultans of Dance",
        OnboardingAgreementID="11",
        Status="Undeployed",
        Category="Education",
        CostCenterLabel=None,
    )
    # ACT
    persist_muleapplication(muleapplication, connection)
    persist_muleapplication(muleapplication1, connection)
    cursor.execute("SELECT * FROM MuleApplication;")
    amount_of_muleapplication = len(cursor.fetchall())
    connection.close()
    # ASSERT
    assert amount_of_muleapplication == 2


# ------------------------------------ END OF PERSIST MULEAPPLICATION TESTS ------------------------------------ #

# ------------------------------------ START OF UPDATE MULEAPPLICATION TESTS ------------------------------------ #

# TEST IF A MULEAPPLICATION GETS UPDATED CORRECTLY
def test_update_muleapplication(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    mock.clean_table(connection, "MuleApplication")
    # ARRANGE
    cursor = connection.cursor()
    commands = (
        mock.return_costcenter_table(),
        mock.return_muleapplication_table(),
        "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('QWERTY', 'awp-12-d-aqsab-xp', 'Anakin Skywalker', 'ANSK', 'Deathstar', '1', 'Deployed', 'Standard', null)",
    )
    mock.execute_commands(commands, connection)
    data = {"Id": "QWERTY", "ContactPerson": "superlegittestname"}
    # ACT
    update_muleapplication(data, connection)
    cursor.execute("SELECT contactperson FROM MuleApplication WHERE Id = 'QWERTY'")
    name = cursor.fetchone()[0]
    connection.close()
    # ASSERT
    assert name == "superlegittestname"


# TEST IF A MULEAPPLICATION GETS UPDATED CORRECTLY ON MULTIPLE PARAMETERS
def test_update_muleapplication_multiple_params(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    mock.clean_table(connection, "MuleApplication")
    # ARRANGE
    cursor = connection.cursor()
    commands = (
        mock.return_costcenter_table(),
        mock.return_muleapplication_table(),
        "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('QWERTY', 'awp-12-d-aqsab-xp', 'Anakin Skywalker', 'ANSK', 'Deathstar', '1', 'Deployed', 'Standard', null)",
    )
    mock.execute_commands(commands, connection)
    data = {"Id": "QWERTY", "ContactPerson": "superlegittestname", "Status": "done"}
    # ACT
    update_muleapplication(data, connection)
    cursor.execute("SELECT contactperson FROM MuleApplication WHERE Id = 'QWERTY'")
    contactperson = cursor.fetchone()[0]
    cursor.execute("SELECT status FROM MuleApplication WHERE Id = 'QWERTY'")
    status = cursor.fetchone()[0]
    connection.close()
    # ASSERT
    assert (contactperson == "superlegittestname") and (status == "done")


# ------------------------------------ END OF UPDATE MULEAPPLICATION TESTS ------------------------------------ #


# ------------------------------------ START OF DELETE MULEAPPLICATION TESTS ------------------------------------ #
# TEST IF A MULEAPPLICATION GETS DELETED CORRECTLY
def test_delete_muleapplication(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    mock.clean_table(connection, "MuleApplication")
    # ARRANGE
    cursor = connection.cursor()
    commands = (
        mock.return_costcenter_table(),
        mock.return_muleapplication_table(),
        "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('QWERTY', 'awp-12-d-aqsab-xp', 'Anakin Skywalker', 'ANSK', 'Deathstar', '1', 'Deployed', 'Standard', null)",
        "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('IHSEBF', 'awp-12-d-aqssssab-xp', 'Anakin Skywalker', 'ANSK', 'Deathstar', '1', 'Deployed', 'Standard', null)",
    )
    mock.execute_commands(commands, connection)
    id = "QWERTY"
    # ACT
    delete_muleapplication_by_id(id, connection)
    cursor.execute(
        "SELECT * FROM MuleApplication",
    )
    amount_of_muleapplication = len(cursor.fetchall())
    connection.close()
    # ASSERT
    assert amount_of_muleapplication == 1


# ------------------------------------ END OF DELETE MULEAPPLICATION TESTS ------------------------------------ #


# ------------------------------------ START OF GET MULEAPPLICATION TESTS ------------------------------------ #
# TEST IF MULEAPPLICATIONS ARE RETURNED PROPERLY
def test_get_all_muleapplication(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    mock.clean_table(connection, "MuleApplication")
    # ARRANGE
    commands = (
        mock.return_costcenter_table(),
        mock.return_muleapplication_table(),
        "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('QWERTY', 'awp-12-d-aqsab-xp', 'Anakin Skywalker', 'ANSK', 'Deathstar', '1', 'Deployed', 'Standard', null)",
        "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('IHSEBF', 'awp-12-d-aqssssab-xp', 'Anakin Skywalker', 'ANSK', 'Deathstar', '1', 'Deployed', 'Standard', null)",
    )
    mock.execute_commands(commands, connection)
    data = {}
    # ACT
    amount_of_muleapplication = len(get_all_muleapplications(data, connection))
    connection.close()
    # ASSERT
    assert amount_of_muleapplication == 2


# TEST IF MULEAPPLICATIONS ARE RETURNED PROPERLY ON MULTIPLE PARAMETERS (FILTERING)
def test_get_all_muleapplication_on_parameters(connection=mock.establish_connection()):
    # ENSURE CLEAN ENVIRONMENT
    mock.clean_table(connection, "CostCenter")
    mock.clean_table(connection, "MuleApplication")
    # ARRANGE
    commands = (
        mock.return_costcenter_table(),
        mock.return_muleapplication_table(),
        "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('QWERTY', 'awp-12-d-aqsab-xp', 'Anakin Skywalker', 'ANSK', 'Deathstar', '1', 'Deployed', 'Standard', null)",
        "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES ('IHSEBF', 'awp-12-d-aqssssab-xp', 'Luke Skywalker', 'ANSK', 'Deathstar', '1', 'Deployed', 'Standard', null)",
    )
    mock.execute_commands(commands, connection)
    data = {"ContactPerson": "Anakin Skywalker", "Status": "Deployed"}
    # ACT
    amount_of_muleapplication = len(get_all_muleapplications(data, connection))
    connection.close()
    # ASSERT
    assert amount_of_muleapplication == 1


# ------------------------------------ END OF GET MULEAPPLICATION TESTS ------------------------------------ #
