from DatabaseLayer.Queries import muleapplicationinstance_queries
from LogicLayer.Entities.MuleApplicationInstance import MuleApplicationInstance
from nanoid import generate
from psycopg2 import errors
from psycopg2._psycopg import connection
from flask import Response
from Logger.logger_creator import create_logger as log
from datetime import datetime, timezone
from dacite import from_dict

import json


class MuleApplicationInstanceHandler:
    def handle_persist_muleapplication_instance(request_body:json, connection: connection = None) -> Response:
        request_body["Id"] = generate(size=10)
        request_body["RecordDateTime"] = str(datetime.now(timezone.utc))
        try:
            muleapplicationinstance = from_dict(
                data_class=MuleApplicationInstance, data=request_body
            )
            muleapplicationinstance_queries.persist_muleapplication_instance(
                muleapplicationinstance, connection
            )
            return Response(
                response=json.dumps("Created MuleApplicationInstance"),
                status=201,
                headers={"Access-Control-Allow-Origin": "*"},
            )

        # INSTANCES CAN HAVE THE SAME NAME SO THIS IS WRONG
        except errors.UniqueViolation as error:
            log().error(error)
            return Response(
                response=json.dumps("A MuleApplicationInstance with that name already exists - Please change the name and try again, check the logs for more information"),
                status=400,
            )

        except errors.ForeignKeyViolation as error:
            log().error(error)
            return Response(
                response=json.dumps("No Muleapplication with that id exists - You can create an instance without specifying an Id by using null, but you can't makeup your own, check the logs for more information"),
                status=400,
            )

        except Exception as error:
            log().error(error)
            return Response(
                response=json.dumps("An error occured that the system did not expect, check logs for more information"),
                status=400,
            )

    def handle_get_all_muleapplicationinstances(request_body: json, connection: connection = None) -> Response:
        try:
            instances = (
                muleapplicationinstance_queries.get_all_muleapplication_instances(
                    request_body, connection
                )
            )
            return Response(
                response=json.dumps(instances, default=str).encode("utf-8"),
                status=200,
                headers={"Access-Control-Allow-Origin": "*"},
            )
        except Exception as error:
            log().error(error)
            return Response(
                response=json.dumps("An error occured that the system did not expect, check logs for more information"),
                status=400,
            )

    def handle_update_muleapplicationinstance(request_body: json, connection: connection = None) -> Response:
        try:
            muleapplicationinstance_queries.update_muleapplicationinstance(
                request_body, connection
            )
            return Response(
                response=json.dumps("Updated MuleApplicationInstance"),
                status=200,
                headers={"Access-Control-Allow-Origin": "*"},
            )
        except errors.ForeignKeyViolation as error:
            log().error(error)
            return Response(
                response=json.dumps("No business group has the provided id, check the logs for more information"),
                status=400,
            )

        except Exception as error:
            log().error(error)
            return Response(
                response=json.dumps("An error occured that the system did not expect, check logs for more information"),
                status=400,
            )

    def handle_delete_muleapplicationinstance_by_id(request_body: json, connection: connection = None) -> Response:
        try:
            id = request_body.get("Id")
            muleapplicationinstance_queries.delete_muleapplicationinstance_by_id(
                id, connection
            )
            return Response(
                response=json.dumps("Deleted MuleApplicationInstance"),
                status=200,
                headers={"Access-Control-Allow-Origin": "*"},
            )
        except Exception as error:
            log().error(error)
            return Response(
                response=json.dumps("An error occured that the system did not expect, check logs for more information"),
                status=400,
            )
