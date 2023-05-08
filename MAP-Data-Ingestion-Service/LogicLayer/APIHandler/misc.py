import datetime

def get_name_and_id_from_elements(elements: list) -> list:
    _list = []
    for element in elements:
        name = element.get("name")
        id = element.get("id")
        _list.append({"name": name, "id": id})
    return _list


def add_main_organization_id(_list: list, organization_id: str) -> list:
    _list.append({"name": "Novo Nordisk", "id": organization_id})
    return _list


def get_relevant_data_from_applications(_list: list) -> list:
    new_list = []
    utc_time = datetime.datetime.utcnow() 
    timestamp = utc_time.strftime('%Y-%d-%m %H:%M:%S')
    for element in _list:
        my_temp_object = {
            "businessGroup": element.get("businessGroup"),
            "environmentName": element.get("environmentName"),
            "status": element.get("status"),
            "domain": element.get("domain"),
            "workerWeight": element.get("workers").get("type").get("weight"),
            "workers": element.get("workers").get("amount"),
            "muleVersion": element.get("muleVersion").get("version"),
            "region": element.get("region"),
            "staticIPsEnabled": element.get("staticIPsEnabled"),
            "recordDateTime" : timestamp,
            "isDeploymentWaiting": element.get("isDeploymentWaiting")
        }
        new_list.append(my_temp_object)
    return new_list
    


    
    