from __main__ import app
from flask import request
from LogicLayer.ServiceAPIs.CostCenterAPI.CostCenterHandler import CostCenterHandler


BASE_ROUTE = "/costcenter"


@app.route(BASE_ROUTE, methods=["POST"])
def persist_costcenter():
    return CostCenterHandler.handle_persist_costcenter(request_body=request.get_json())


@app.route(BASE_ROUTE, methods=["GET"])
def get_costcenters():
    return CostCenterHandler.handle_get_all_costcenters(request_body=dict(request.args))


@app.route(BASE_ROUTE, methods=["DELETE"])
def delete_costcenter_by_id():
    return CostCenterHandler.handle_delete_costcenter_by_id(request_body=request.get_json())


@app.route(BASE_ROUTE, methods=["PATCH"])
def update_costcenter():
    return CostCenterHandler.handle_update_costcenter(request_body=request.get_json())
