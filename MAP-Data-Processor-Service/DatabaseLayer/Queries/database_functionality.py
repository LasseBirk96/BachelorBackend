from DatabaseLayer.connector import establish_connection
from DatabaseLayer.Misc import helper_tools as tools
from psycopg2._psycopg import connection
from Logger.logger_creator import create_logger as log
from nanoid import generate



def update_row(id: str, error = None, connection: connection = None):
    if connection == None:
        connection = establish_connection()
    cursor = connection.cursor()
    #THIS IS BAD
    status = "FAILED"
    if error == None:
        status = "PROCESSED"
    query = "UPDATE StageingTable SET Status = %s, dateProcessed = timezone('utc', now()) WHERE Id = %s"
    log().info("UPDATING STATUS ON ROW WHERE ID IS: {}".format(id))
    try:
        cursor.execute(query, (status, id,))
        connection.commit()
        log().info("UPDATED STATUS ON ROW WHERE ID IS: {}".format(id))
    except Exception as error:
        log().error("THE FOLLOWING ERROR OCCURRED WHEN TRYING TO UPDATE ROW {}: {}".format(id, error))
        raise 


def get_oldest_not_processed_batch(connection: connection = None) -> tuple[str, dict]:
    if connection == None:
        connection = establish_connection()
    cursor = connection.cursor()
    query = """SELECT Id, AnyPointData FROM StageingTable WHERE Status = 'Not Processed' ORDER BY DateAdded LIMIT 1"""
    log().info("GETTING OLDEST VALID BATCH")
    try:
        cursor.execute(query)
        fetched = cursor.fetchone()
        id_of_row = fetched[0]
        data = fetched[1]
        if id_of_row is None:
            raise TypeError
        log().info("GOT OLDEST VALID BATCH")
        return id_of_row, data
    except TypeError:
        raise
    except Exception as error:
        log().error("THE FOLLOWING ERROR OCCURRED WHEN TRYING TO GET OLDEST BATCH: {}".format(error))
        raise 


def get_names_of_all_muleapps(connection: connection = None) -> list:
    if connection == None:
        connection = establish_connection()
    cursor = connection.cursor()
    query = "SELECT Name FROM MuleApplication;"
    log().info("TRYING TO GET NAMES OF ALL MULEAPPLICATIONS")
    try:
        cursor.execute(query)
        result = [r[0] for r in cursor.fetchall()]
        log().info("GOT THE NAMES OF ALL MULEAPPLICATIONS")
        return result
    except Exception as error:
        log().error("THE FOLLOWING ERROR OCCURRED WHEN TRYING TO GET THE NAMES OF ALL MULEAPPLICATIONS: {}".format(error))
        raise
    
def prepare_batch(id: str, list_of_instances: list, list_of_muleapp_names: list) -> list:
    log().info("TRYING TO PREPARE BATCH WITH ID: {}".format(id))
    try:
        list_of_objects = []
        for element in list_of_instances:
            mule_app_name, app_registration = tools.determine_name_and_registration(list_of_muleapp_names, element)
            updated_object = (
                generate(size=20),
                mule_app_name,
                element.get("domain"),
                app_registration,
                element.get("businessGroup"),
                element.get("environmentName"),
                element.get("status"),
                element.get("muleVersion"),
                element.get("workerWeight"),
                element.get("workers"),
                element.get("region"),
                element.get("staticIPsEnabled"),
                element.get("recordDateTime"),
                element.get("isDeploymentWaiting"),
            )
            list_of_objects.append(updated_object)
        log().info("PREPARED BATCH WITH ID: {}".format(id))
        return list_of_objects
    except Exception as error:
            log().error("THE FOLLOWING ERROR OCCURED WHEN TRYING TO PREPARE BATCH WITH ID {}: {}".format(id, error))
            raise

def persist_instance(id: str, batch: list, connection: connection = None):
    if connection == None:
        connection = establish_connection()
    cursor = connection.cursor()
    log().info("TRYING TO PERSIST BATCH WITH ID: {}".format(id))
    query = "INSERT INTO MuleApplicationInstance (Id, MuleAppName, Name, AppRegistration, BusinessGroup, EnvironmentName, DeploymentStatus, MuleVersion, WorkerWeight, Workers, Region, staticIPsEnabled, RecordDateTime, isDeploymentWaiting) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"    
    try:
        for element in batch:
            cursor.execute(query, (element),)
        connection.commit()
        log().info("PERSISTED BATCH WITH ID: {}".format(id))
    except Exception as error:
            log().error("THE FOLLOWING ERROR OCCURED WHEN TRYING TO PERSIST BATCH WITH ID {}: {}".format(id, error))
            raise
        

    
