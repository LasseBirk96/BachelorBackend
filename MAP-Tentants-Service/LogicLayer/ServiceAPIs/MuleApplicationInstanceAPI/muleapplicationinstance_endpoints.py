from __main__ import app
from flask import request
from LogicLayer.ServiceAPIs.MuleApplicationInstanceAPI.MuleApplicationInstanceHandler import (
    MuleApplicationInstanceHandler,
)


BASE_ROUTE = "/muleapplicationinstance"


@app.route(BASE_ROUTE, methods=["POST"])
def persist_muleapplicationinstance():
    return MuleApplicationInstanceHandler.handle_persist_muleapplication_instance(request_body=request.get_json())


@app.route(BASE_ROUTE, methods=["GET"])
def get_all_muleapplicationinstances():
    return MuleApplicationInstanceHandler.handle_get_all_muleapplicationinstances(request_body=dict(request.args))


@app.route(BASE_ROUTE, methods=["PATCH"])
def update_muleapplicationinstance():
    return MuleApplicationInstanceHandler.handle_update_muleapplicationinstance(request_body=request.get_json())


@app.route(BASE_ROUTE, methods=["DELETE"])
def delete_muleapplicationinstance_by_id():
    return MuleApplicationInstanceHandler.handle_delete_muleapplicationinstance_by_id(request_body=request.get_json())
