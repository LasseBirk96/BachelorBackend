from DatabaseLayer.Queries import muleapplication_queries
from LogicLayer.Entities.MuleApplication import MuleApplication
from nanoid import generate
from psycopg2 import errors
from psycopg2._psycopg import connection
from flask import Response
from Logger.logger_creator import create_logger as log
from dacite import from_dict
import json

class MuleApplicationHandler:
    def handle_persist_muleapplication(request_body: json, connection: connection = None) -> Response:
        request_body["Id"] = generate(size=10)
        try:
            muleapplication = from_dict(data_class=MuleApplication, data=request_body)
            muleapplication_queries.persist_muleapplication(muleapplication, connection)
            return Response(
                response=json.dumps("Created MuleApplication"),
                status=201,
                headers={"Access-Control-Allow-Origin": "*"},
            )

        except errors.UniqueViolation as error:
            log().error(error)
            return Response(
                response=json.dumps("A muleapplication with that name already exists - Please change the name and try again, check the logs for more information"),
                status=400,
            )
            
    

        except errors.ForeignKeyViolation as error:
            log().error(error)
            return Response(
                response=json.dumps("No costcenter has the provided label - You can create an application without specifying a label by using null, but you can't makeup your own, check the logs for more information"),
                status=400,
            )
            

        except Exception as error:
            log().error(error)
            return Response(
                response=json.dumps("An error occured that the system did not expect, check logs for more information"),
                status=400,
            )

    def handle_get_all_muleapplications(request_body: json, connection: connection = None) -> Response:
        try:
            muleapplications = muleapplication_queries.get_all_muleapplications(request_body, connection)
            return Response(
                response=json.dumps(muleapplications),
                status=200,
                headers={"Access-Control-Allow-Origin": "*"},
            )

        except Exception as error:
            log().error(error)
            return Response(
                response=json.dumps("An error occured that the system did not expect, check logs for more information"),
                status=400,
            )

    def handle_delete_muleapplication_by_id(request_body: json, connection: connection = None) -> Response:
        try:
            muleapplication_queries.delete_muleapplication_by_id(id = request_body.get("Id"), connection=connection)
            return (
                Response(response= "Deleted MuleApplication", status=200, headers={"Access-Control-Allow-Origin": "*"})
            )
        except Exception as error:
            log().error(error)
            return Response(
                response="An error occured that the system did not expect, check logs for more information",
                status=400,
            )

    def handle_update_muleapplication(request_body:json, connection: connection = None) -> Response:
        try:
            muleapplication_queries.update_muleapplication(request_body, connection)
            return Response(
                response=json.dumps("Updated MuleApplication"),
                status=200,
                headers={"Access-Control-Allow-Origin": "*"},
            )
        except errors.ForeignKeyViolation as error:
            log().error(error)
            return Response(response =json.dumps("No costcenter has the id you are trying to attach to the muleapplication, check the logs for more information"), status = 400, )
    

        except Exception as error:
            log().error(error)
            return Response(
                response=json.dumps("An error occured that the system did not expect, check logs for more information"),
                status=400,
            )

