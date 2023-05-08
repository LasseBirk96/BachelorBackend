from psycopg2 import connect


def establish_connection():
    return connect(dbname="postgres",user="postgres", password="123",port=5432, host="127.0.0.1")

def execute_commands(commands, connection):
    cursor = connection.cursor()
    try:
        for command in commands:
            cursor.execute(command)
        connection.commit()
    except (Exception) as error:
        print(error)
        
        
        
def clean_table(connection, table_name):
    query = "DROP TABLE IF EXISTS {} CASCADE;".format(table_name)
    cursor = connection.cursor()
    cursor.execute(query, (table_name,))
    connection.commit()
    


def return_noname_table():
    return str(    """
    CREATE TABLE IF NOT EXISTS StagingTable (
        AnyPointData jsonb,
        DateAdded timestamp default current_timestamp,
        LastAccessed timestamp default current_timestamp
        )
    """,)