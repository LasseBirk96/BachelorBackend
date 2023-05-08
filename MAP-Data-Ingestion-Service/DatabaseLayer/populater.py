from DatabaseLayer.connection import establish_connection
import json
from psycopg2._psycopg import connection
from nanoid import generate

def populate(_list: list, connection: connection = None):
    if connection == None:
        connection = establish_connection()
    cursor = connection.cursor()
    query = "INSERT INTO StageingTable (Id, AnyPointData) VALUES (%s, %s)"
    id = generate(size=10)
    try:
        cursor.execute(query, (id, json.dumps(_list),))
        connection.commit()
    except Exception:
        raise