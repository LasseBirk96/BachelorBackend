from __main__ import app
from flask import request
from LogicLayer.ServiceAPIs.BusinessGroupResourceAPI.BusinessGroupResourceHandler import (
    BusinessGroupResourceHandler,
)


BASE_ROUTE = "/businessgroupresource"


@app.route(BASE_ROUTE, methods=["POST"])
def persist_businessgroupresource():
    return BusinessGroupResourceHandler.handle_persist_businessgroupresource(request_body=request.get_json())


@app.route(BASE_ROUTE, methods=["GET"])
def get_all_businessgroupresources():
    return BusinessGroupResourceHandler.handle_get_all_businessgroupsresources(request_body=request.get_json())


@app.route(BASE_ROUTE, methods=["DELETE"])
def delete_businessgroupresource_by_id():
    return BusinessGroupResourceHandler.handle_delete_businessgroupsresources_by_id(request_body=request.get_json()
)


@app.route(BASE_ROUTE, methods=["PATCH"])
def update_businessgroupresource():
    return BusinessGroupResourceHandler.handle_update_businessgroupsresources(request_body=request.get_json())
