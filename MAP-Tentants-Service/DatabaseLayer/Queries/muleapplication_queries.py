import json
from DatabaseLayer.connection import establish_connection, establish_connection_local
from psycopg2 import errors, sql
from psycopg2._psycopg import connection
from LogicLayer.Entities.MuleApplication import MuleApplication
from dataclasses import astuple
from DatabaseLayer.Queries.misc.dict_keys_helper import (
    merge_keys_with_values,
    check_if_no_keys,
    lowercase_keys_to_dict,
    lowercase_keys_to_list
)


def persist_muleapplication(MuleApplication: MuleApplication, connection: connection = None):
    if connection == None:
        connection = establish_connection()
    cursor = connection.cursor()
    query = "INSERT INTO MuleApplication (Id, Name, ContactPerson, ContactPersonInitials, ProjectName, OnboardingAgreementID, Status, Category, CostCenterLabel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        cursor.execute(query, astuple(MuleApplication),)
        connection.commit()
    except (errors.UniqueViolation, errors.ForeignKeyViolation, Exception):
        raise


def get_all_muleapplications(data: json, connection: connection = None) -> list:
    if connection == None:
        connection = establish_connection()
    cursor = connection.cursor()
    if check_if_no_keys(data):
        query = "SELECT * FROM MuleApplication"
    else:
        update_fields = lowercase_keys_to_list(data)
        query = sql.SQL("SELECT * FROM MuleApplication WHERE ({}) = ({})").format(
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


def delete_muleapplication_by_id(id: str, connection: connection = None):
    if connection == None:
        connection = establish_connection()
    cursor = connection.cursor()
    query = "DELETE FROM MuleApplication WHERE id = %s"
    try:
        cursor.execute(query, (id,))
        connection.commit()
    except Exception:
        raise


def update_muleapplication(data: json, connection: connection = None):
    if connection == None:
        connection = establish_connection()
    cursor = connection.cursor()
    update_fields = lowercase_keys_to_list(data)
    update_sql = sql.SQL(
        """UPDATE MuleApplication SET ({}) = ({}) WHERE id = %(id)s """
    ).format(
        sql.SQL(", ").join(map(sql.Identifier, update_fields)),
        sql.SQL(", ").join(map(sql.Placeholder, update_fields)),
    )
    try:
        cursor.execute(update_sql, lowercase_keys_to_dict(data))
        connection.commit()
    except (errors.ForeignKeyViolation, Exception):
        raise
