import requests
from decouple import config
from Logger.logger_creator import create_logger as log
from LogicLayer.Entities.CustomResponseObject import CustomResponseObject

def get_access_token(client_id: str, client_secret: str) -> CustomResponseObject:
    log().info("TRYING TO GET ACCESS TOKEN")
    body = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }
    try:
        request_response = requests.post(url=config("auth_url"), json=body)
        log().info("GOT ACCESS TOKEN")
        return CustomResponseObject(response = request_response.json().get("access_token") , status = request_response.status_code)
    except Exception as error:
        log().error(error)
        raise


def get_organization_id(access_token: str) -> CustomResponseObject:
    log().info("TRYING TO GET ORGANIZATION ID")
    try:
        request_response = requests.get(
            url=config("organization_id_url"),
            headers={"Authorization": "Bearer {}".format(access_token)},
        )
        client = request_response.json().get("client")
        log().info("GOT ORGANIZATION ID")
        return CustomResponseObject(response = client.get("org_id"), status = request_response.status_code)
    except Exception as error:
        log().error(error)
        raise


def get_suborganizations(organization_id: str, access_token: str) -> CustomResponseObject:
    log().info("TRYING TO GET SUBORGANIZATIONS")
    try:
        request_response = requests.get(
            url=config("suborganization_url").format(organization_id),
            headers={"Authorization": "Bearer {}".format(access_token)},
        )
        log().info("GOT SUBORGANIZATIONS")
        return CustomResponseObject(response = request_response.json().get("subOrganizations"), status = request_response.status_code)
    except requests.exceptions.HTTPError:
        raise
    except Exception as error:
        log().error(error)
        raise


def get_environments_by_organization_id(organizations: list, access_token) -> CustomResponseObject:
    log().info("TRYING TO GET ENVIRONMENTS")
    try:
        _list = []
        for organization in organizations:
            request_response = requests.get(
                url=config("environment_url").format(organization.get("id")),
                headers={"Authorization": "Bearer {}".format(access_token)},
            )
            for element in request_response.json().get("data"):
                element["businessGroup"] = organization.get("name")
                _list.append(element)
        log().info("GOT ENVIRONMENTS")
        return CustomResponseObject(response = _list, status = request_response.status_code)
    except Exception as error:
        log().error(error)
        raise


def get_applications_by_ids(list_of_environments: list, access_token: str) -> CustomResponseObject:
    log().info("TRYING TO GET APPLICATIONS")
    try:
        _list = []
        for element in list_of_environments:
            request_response = requests.get(
                url=config("applications_url"),
                headers={
                    "Authorization": "Bearer {}".format(access_token),
                    "X-ANYPNT-ORG-ID": element.get("organizationId"),
                    "X-ANYPNT-ENV-ID": element.get("id"),
                },
            )
            for entry in request_response.json():
                entry["businessGroup"] = element.get("businessGroup")
                entry["environmentName"] = element.get("name")
                _list.append(entry)
        log().info("GOT APPLICATIONS")
        return CustomResponseObject(response = _list, status = request_response.status_code)
    except Exception as error:
        log().error(error)
        raise
