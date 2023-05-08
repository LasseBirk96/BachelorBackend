from DatabaseLayer.Queries import costcenter_queries
from Logger.logger_creator import create_logger as log
from psycopg2 import errors
from psycopg2._psycopg import connection
from flask import Response
from LogicLayer.ServiceAPIs.CostCenterAPI.costcenter_util import validate_body
import json


class CostCenterHandler:
    
    def handle_persist_costcenter(request_body: json, connection: connection = None) -> Response:
        try:
            
            costcenter_queries.persist_costcenter(validate_body(request_body), connection)
            return Response(
                response=json.dumps({"msg":"Created Costcenter"}),
                status=201,
                headers={"Access-Control-Allow-Origin": "*"},
            )

        except errors.UniqueViolation as error:
            log().error(error)
            return Response(
                response=json.dumps({"msg":"A costcenter with that label already exists - Please change the label and try again, check the logs for more information"}),
                status=400,
            )

        except errors.NotNullViolation as error:
            log().error(error)
            return Response(
                response=json.dumps({"msg":"A field that is not allowed to be left empty was - Please change this and try again, check the logs for more information"}),
                status=400,
            )

        except TypeError as error:
            log().error(error)
            return Response(
                response=json.dumps({"msg":error.args[0]}),
                status=400,
            )
            
        except Exception as error:
            log().error(error)
            return Response(
                response=json.dumps({"msg":"An error occured that the system did not expect, check logs for more information"}),
                status=400,
            )

    def handle_get_all_costcenters(request_body: json, connection: connection = None) -> Response:
        try:
            costcenters = costcenter_queries.get_all_costcenters(request_body, connection)
            return Response(
                response=json.dumps(costcenters),
                status=200,
                headers={"Access-Control-Allow-Origin": "*"},
            )
        except Exception as error:
            log().error(error)
            return Response(
                response=json.dumps({"msg":"An error occured that the system did not expect, check logs for more information"}),
                status=400,
            )

    def handle_delete_costcenter_by_id(request_body: json, connection: connection = None) -> Response:
        try:
            costcenter_queries.delete_costcenter_by_id(id = request_body.get("Id"), connection=connection)
            return (
                Response(response= "Deleted Costcenter", status=200, headers={"Access-Control-Allow-Origin": "*"})
            )
        except Exception as error:
            log().error(error)
            return Response(
                response=json.dumps({"msg":"An error occured that the system did not expect, check logs for more information"}),
                status=400,
            )

    def handle_update_costcenter(request_body: json, connection: connection = None) -> Response:
        try:
            costcenter_queries.update_costcenter(validate_body(request_body), connection)
            return Response(
                response=json.dumps("Updated Costcenter"),
                status=200,
                headers={"Access-Control-Allow-Origin": "*"},
            )
            
            
        except TypeError as error:
            log().error(error)
            return Response(
                response=json.dumps({"msg":error.args[0]}),
                status=400,
            )
            

        except Exception as error:
            log().error(error)
            return Response(
                response=json.dumps({"msg":"An error occured that the system did not expect, check logs for more information"}),
                status=400,
            )
