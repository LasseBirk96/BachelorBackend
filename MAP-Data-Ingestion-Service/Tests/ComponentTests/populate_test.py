# from Tests import mock_pytest_postgresql as mock
# from DatabaseLayer.populater import populate

# def test_data(connection = mock.establish_connection()):
#     mock.clean_table(connection, "StagingTable")
#     cursor = connection.cursor()
#     mock.execute_commands((mock.return_noname_table(),), connection)
#     _list = [{"data":"erfregr"}, {"data":"rgn"}]
#     populate(_list ,connection)

#     cursor.execute("SELECT * FROM StagingTable;")
#     data = len(cursor.fetchall())
#     connection.close()
#     # ASSERT
#     assert data == 1