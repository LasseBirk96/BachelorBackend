from __main__ import app
from flask import request
from LogicLayer.ServiceAPIs.BusinessGroupAPI.BusinessGroupHandler import (
    BusinessGroupHandler,
)


BASE_ROUTE = "/businessgroup"


@app.route(BASE_ROUTE, methods=["POST"])
def persist_businessgroup():
    return BusinessGroupHandler.handle_persist_businessgroup(request_body=request.get_json())


@app.route(BASE_ROUTE, methods=["GET"])
def get_all_businessgroups():
    return BusinessGroupHandler.handle_get_all_businessgroups(request_body=request.get_json())


@app.route(BASE_ROUTE, methods=["DELETE"])
def delete_businessgroup_by_id():
    return BusinessGroupHandler.handle_delete_businessgroup_by_id(request_body=request.get_json())


@app.route(BASE_ROUTE, methods=["PATCH"])
def update_businessgroup():
    return BusinessGroupHandler.handle_update_businessgroup(request_body=request.get_json())
