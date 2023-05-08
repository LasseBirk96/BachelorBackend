import json
from DatabaseLayer.connection import establish_connection
from psycopg2 import errors, sql
from psycopg2._psycopg import connection
from LogicLayer.Entities.CostCenter import CostCenter
from dataclasses import astuple
from DatabaseLayer.Queries.misc.dict_keys_helper import (
    merge_keys_with_values,
    check_if_no_keys,
    lowercase_keys_to_dict,
    lowercase_keys_to_list
)

# MAYBE MAKE THIS MORE DYNAMIC
# Takes a CostCenter object and persists it, the reason for the connection being none is so that the function can be tested with a different connection
def persist_costcenter(CostCenter: CostCenter,connection: connection = None):
    if connection == None:
        connection = establish_connection()
    cursor = connection.cursor()
    query = "INSERT INTO CostCenter (Id, Label, ApproverName, ApproverInitials) VALUES (%s, %s, %s, %s)"
    try:
        # Note the "," at the end, this is how the psycopg API understands that is a tuple that is being executed with the query
        cursor.execute(query, astuple(CostCenter),)
        connection.commit()
    except (errors.UniqueViolation, errors.NotNullViolation, Exception):
        raise


def get_all_costcenters(data: json,connection: connection = None) -> list:
    if connection == None:
        connection = establish_connection()
    cursor = connection.cursor()
    if check_if_no_keys(data):
        query = "SELECT * FROM CostCenter"
    else:
        update_fields = lowercase_keys_to_list(data)
        query = sql.SQL("SELECT * FROM CostCenter WHERE ({}) = ({})").format(
            sql.SQL(", ").join(map(sql.Identifier, update_fields)),
            sql.SQL(", ").join(map(sql.Placeholder, update_fields)),
        )
    try:
        cursor.execute(query, lowercase_keys_to_dict(data))
        value = cursor.fetchall()
        keys = [desc[0] for desc in cursor.description]
        return merge_keys_with_values(keys, value)
    except (Exception, IndexError):
        raise


def delete_costcenter_by_id(id: str,connection: connection = None):
    if connection == None:
        connection = establish_connection()
    cursor = connection.cursor()
    query = "DELETE FROM CostCenter WHERE id = %s"
    try:
        cursor.execute(query, (id,))
        connection.commit()
    except Exception:
        raise


def update_costcenter(data: json,connection: connection = None):
    if connection == None:
        connection = establish_connection()
    cursor = connection.cursor()
    update_fields = lowercase_keys_to_list(data) 
    update_sql = sql.SQL(
        """UPDATE CostCenter SET ({}) = ({}) WHERE id = %(id)s """
    ).format(
        sql.SQL(", ").join(map(sql.Identifier, update_fields)),
        sql.SQL(", ").join(map(sql.Placeholder, update_fields)),
    )
    try:
        cursor.execute(update_sql, lowercase_keys_to_dict(data))
        connection.commit()
    except (Exception):
        raise
