import os
import time
from psycopg2 import connect, OperationalError


# The reason for the tries/timeout is that forever reason, postgres sometimes takes forever to start, so this allows the system to try to connect a few times
def establish_connection(tries=3, timeout=5):
    if tries == 0:
        raise Exception("Could not connect after multiple tries")

    try:
        return connect(
            dbname=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD"),
            host=os.environ.get("POSTGRES_HOST"),
            port=os.environ.get("POSTGRES_PORT"),
        )
    except OperationalError:
        time.sleep(timeout)
        return establish_connection(tries - 1, timeout)


# This is purely for local testing whilst developing, remove if unwanted
def establish_connection_to_local_postgres():
    return connect(
        dbname="postgres", user="postgres", password="123", port=5432, host="127.0.0.1"
    )
