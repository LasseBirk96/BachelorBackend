from DatabaseLayer.Queries import businessgroup_queries
from LogicLayer.Entities.BusinessGroup import BusinessGroup
from nanoid import generate
from psycopg2 import errors
from psycopg2._psycopg import connection
from flask import Response
from Logger.logger_creator import create_logger as log
from dacite import from_dict
import json


class BusinessGroupHandler:
    def handle_persist_businessgroup(request_body: json, connection: connection = None) -> Response:
        request_body["Id"] = generate(size=10)
        try:
            businessgroup = from_dict(data_class=BusinessGroup, data=request_body)
            businessgroup_queries.persist_businessgroup(businessgroup, connection)
            return Response(
                response="Created BusinessGroup",
                status=201,
                headers={"Access-Control-Allow-Origin": "*"},
            )

        except errors.UniqueViolation as error:
            log().error(error)
            return Response(
                response="A BusinessGroup with that name already exists - Please change the name and try again, check the logs for more information",
                status=400,
            )

        except Exception as error:
            log().error(error)
            return Response(
                response="An error occured that the system did not expect, check logs for more information",
                status=400,
            )

    def handle_get_all_businessgroups(request_body: json, connection: connection = None) -> Response:
        try:
            businessgroups = businessgroup_queries.get_all_businessgroups(
                request_body, connection
            )
            return Response(
                response=json.dumps(businessgroups),
                status=200,
                headers={"Access-Control-Allow-Origin": "*"},
            )
        except Exception as error:
            log().error(error)
            return Response(
                response="An error occured that the system did not expect, check logs for more information",
                status=400,
            )

    def handle_delete_businessgroup_by_id(request_body: json, connection: connection = None) -> Response:
        try:
            id = request_body.get("Id")
            businessgroup_queries.delete_businessgroup_by_id(id, connection)
            return Response(
                response="Deleted BusinessGrouop",
                status=200,
                headers={"Access-Control-Allow-Origin": "*"},
            )
        except Exception as error:
            log().error(error)
            return Response(
                response="An error occured that the system did not expect, check logs for more information",
                status=400,
            )

    def handle_update_businessgroup(request_body: json, connection: connection = None) -> Response:
        try:
            businessgroup_queries.update_businessgroup(request_body, connection)
            return Response(
                response="Updated BusinessGrouop",
                status=200,
                headers={"Access-Control-Allow-Origin": "*"},
            )
        except Exception as error:
            log().error(error)
            return Response(
                response="An error occured that the system did not expect, check logs for more information",
                status=400,
            )
