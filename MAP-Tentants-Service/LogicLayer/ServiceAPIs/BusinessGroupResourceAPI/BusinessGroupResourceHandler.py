from DatabaseLayer.Queries import businessgroupresource_queries
from LogicLayer.Entities.BusinessGroupResource import BusinessGroupResource
from nanoid import generate
from psycopg2 import errors
from psycopg2._psycopg import connection
from flask import Response
from Logger.logger_creator import create_logger as log
from datetime import datetime, timezone
from dacite import from_dict
import json
from flask import Response

class BusinessGroupResourceHandler:
    def handle_persist_businessgroupresource(request_body: json, connection: connection = None) -> Response:
        request_body["RecordDateTime"] = str(datetime.now(timezone.utc))
        request_body["Id"] = generate(size=10)
        try:
            print(BusinessGroupResource.__annotations__)
            businessgroupresource = from_dict(
                data_class=BusinessGroupResource, data=request_body
            )
            businessgroupresource_queries.persist_businessgroupresource(
                businessgroupresource, connection
            )
            return Response(
                response="Created BusinessGroupResource",
                status=201,
                headers={"Access-Control-Allow-Origin": "*"},
            )

        except errors.UniqueViolation as error:
            log().error(error)
            return Response(
                response="A BusinessGroupResource with that name already exists - Please change the name and try again, check the logs for more information",
                status=400,
            )

        except Exception as error:
            log().error(error)
            return Response(
                response="An error occured that the system did not expect, check logs for more information",
                status=400,
            )

    def handle_get_all_businessgroupsresources(request_body: json, connection: connection = None) -> Response:
        try:
            businessgroupresources = (
                businessgroupresource_queries.get_all_businessgroupsresources(
                    request_body, connection
                )
            )
            return Response(
                response=json.dumps(businessgroupresources, default=str).encode("utf-8"),
                status=200,
                headers={"Access-Control-Allow-Origin": "*"},
            )
        except Exception as error:
            log().error(error)
            return Response(
                response="An error occured that the system did not expect, check logs for more information",
                status=400,
            )

    def handle_delete_businessgroupsresources_by_id(request_body: json, connection: connection = None) -> Response:
        try:
            id = request_body.get("Id")
            businessgroupresource_queries.delete_businessgroupresource_by_id(
                id, connection
            )
            return Response(
                response="Deleted BusinessGroupResource",
                status=200,
                headers={"Access-Control-Allow-Origin": "*"},
            )
        except Exception as error:
            log().error(error)
            return Response(
                response="An error occured that the system did not expect, check logs for more information",
                status=400,
            )

    def handle_update_businessgroupsresources(request_body: json, connection: connection = None) -> Response:
        try:
            businessgroupresource_queries.update_businessgroupresource(
                request_body, connection
            )
            return Response(
                response="Updated BusinessGroupResource",
                status=200,
                headers={"Access-Control-Allow-Origin": "*"},
            )

        except errors.ForeignKeyViolation as error:
            log().error(error)
            return Response(
                response="No business group has the provided id, check the logs for more information",
                status=400,
            )

        except Exception as error:
            log().error(error)
            return Response(
                response="An error occured that the system did not expect, check logs for more information",
                status=400,
            )
