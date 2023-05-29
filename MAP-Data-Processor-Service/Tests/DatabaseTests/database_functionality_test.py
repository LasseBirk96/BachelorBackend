# import mock_pytest_postgresql as mock
# from DatabaseLayer.Queries import database_functionality as db




# # --------- TESTS ON UPDATE ROW --------- #

# # THE STATUS ROW SHOULD BE "PROCESSED"
# def test_update_row_no_error():
#     # ARRANGE
#     mock.set_environment()
#     connection = mock.establish_connection()
#     cursor = connection.cursor()
#     cursor.execute(open("data.sql", "r").read())
#     connection.commit()
#     # ACT
#     db.update_row('gjs24GyDOh', connection=connection)
#     cursor.execute("SELECT status FROM StageingTable WHERE Id = 'gjs24GyDOh'")
#     status = cursor.fetchone()[0]
#     # ASSERT
#     assert status == "PROCESSED"
    
    
# # SHOULD AN ERROR BE PASSED ALONG TO THE FUNCTION, THE ROW SHOULD BE "FAILED"
# def test_update_row_service_error():
#     # ARRANGE
#     mock.set_environment()
#     connection = mock.establish_connection()
#     cursor = connection.cursor()
#     cursor.execute(open("data.sql", "r").read())
#     connection.commit()
#     # ACT
#     db.update_row('gjs24GyDOh', Exception, connection=connection)
#     cursor.execute("SELECT status FROM StageingTable WHERE Id = 'gjs24GyDOh'")
#     status = cursor.fetchone()[0]
#     # ASSERT
#     assert status == "FAILED"


# # --------- TESTS ON GET OLDEST BATCH --------- #

# # THE OLDEST RECORD SHOULD BE SELECTED
# def test_oldest_not_processed_batch():
#     # ARRANGE 
#     mock.set_environment()    
#     connection = mock.establish_connection()
#     cursor = connection.cursor()
#     cursor.execute(open("data.sql", "r").read())
#     connection.commit()
#     # ACT
#     id, data = db.get_oldest_not_processed_batch(connection=connection)
    
#     # ASSERT
#     assert id == 'gjs24GyDOh'
    

# # SHOULD AN OLDER RECORD HAVE A STATUS OF "FAILED", A NEWER VALID RECORD SHOULD BE SELECTED
# def test_oldest_not_processed_batch_avoid_invalid_record():
#     # ARRANGE
#     mock.set_environment()    
#     connection = mock.establish_connection()
#     cursor = connection.cursor()
#     cursor.execute(open("data.sql", "r").read())
#     connection.commit()
#     # ACT
#     db.update_row('gjs24GyDOh', Exception, connection=connection)
#     id, data = db.get_oldest_not_processed_batch(connection=connection)
#     # ASSERT
#     assert id == 'QWERYEASDG'
    
    
    
# def test_oldest_not_processed_batch_no_records():
#     # ARRANGE
#     mock.set_environment()    
#     connection = mock.establish_connection()
#     # ACT - # ASSERT
#     try:
#         db.get_oldest_not_processed_batch(connection=connection)
#     except TypeError:
#         assert True
    
    
    
    
    

# # --------- TESTS ON GET NAME OF ALL MULE APPS --------- #
# # SHOULD RETURN A NOT EMPTY LIST 
# def test_get_names_of_all_muleapps():
#     # ARRANGE
#     mock.set_environment()
#     connection = mock.establish_connection()
#     # ACT
#     names = db.get_names_of_all_muleapps(connection)
#     # ASSERT
#     assert len(names) > 1
    
    

# # --------- TESTS ON PREPARE BATCH --------- #
# # SHOULD RETURN A NON EMPTY LIST
# def test_prepare_batch():
    
#     # ARRANGE
#     mock.set_environment()
#     connection = mock.establish_connection()
#     cursor = connection.cursor()
#     cursor.execute(open("data.sql", "r").read())
#     id, data = db.get_oldest_not_processed_batch(connection=connection)
#     names = db.get_names_of_all_muleapps(connection)

#     # ACT
#     prepared_batch = db.prepare_batch(id, data, names)
    
#     # Assert
#     assert len(prepared_batch) > 1
    
    
    
    

# # --------- TESTS ON PERSIST INSTANCE --------- #
# # SHOULD RETURN A NON EMPTY LIST
# def test_persist_instance():
#     # ARRANGE
#     mock.set_environment()
#     connection = mock.establish_connection()
#     cursor = connection.cursor()
#     cursor.execute(open("data.sql", "r").read())
#     id, data = db.get_oldest_not_processed_batch(connection=connection)
#     names = db.get_names_of_all_muleapps(connection)
#     prepared_batch = db.prepare_batch(id, data, names)
#     length_of_batch = len(prepared_batch)
#     # ACT
    
#     db.persist_instance(id, prepared_batch, connection)
#     cursor.execute("SELECT Name From MuleApplicationInstance")
#     amount = len(cursor.fetchall())
    
#     # Assert
#     assert length_of_batch == amount