from psycopg2 import connect, OperationalError
import time


def establish_connection(tries=3, timeout=5):
    if tries == 0:
        raise Exception("Could not connect after multiple tries")

    try:
        return connect(dbname="postgres",user="postgres", password="123",port=5432, host="127.0.0.1")
    except OperationalError:
        time.sleep(timeout)
        return establish_connection(tries - 1, timeout)

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute(open("drop_tables.sql", "r").read())
    connection.commit()
    
def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute(open("create_tables.sql", "r").read())
    connection.commit()
    
    
def fill_tables(connection):
    cursor = connection.cursor()
    cursor.execute(open("fill_tables.sql", "r").read())
    connection.commit()
    
    
def set_environment(connection = establish_connection()):
    drop_tables(connection)
    create_tables(connection)
    fill_tables(connection)
    
