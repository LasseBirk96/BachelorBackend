from __main__ import app
import json
from flask import request
from LogicLayer.ServiceAPIs.MuleApplicationAPI.MuleApplicationHandler import (
    MuleApplicationHandler,
)


BASE_ROUTE = "/muleapplications"








@app.route(BASE_ROUTE, methods=["POST"])
def persist_muleapplication():
    return MuleApplicationHandler.handle_persist_muleapplication(request_body=request.get_json())


@app.route(BASE_ROUTE, methods=["GET"])
def get_all_muleapplications():
    return MuleApplicationHandler.handle_get_all_muleapplications(request_body=dict(request.args))


@app.route(BASE_ROUTE, methods=["PATCH"])
def update_muleapplication():
    return MuleApplicationHandler.handle_update_muleapplication(request_body=request.get_json())


@app.route(BASE_ROUTE, methods=["DELETE"])
def delete_muleapplication_by_id():
    return MuleApplicationHandler.handle_delete_muleapplication_by_id(request_body=request.get_json())
