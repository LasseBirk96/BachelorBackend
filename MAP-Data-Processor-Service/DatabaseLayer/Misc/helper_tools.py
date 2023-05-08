 
def get_valid_regions():
    with open("valid_regions.txt") as f:
        data = f.read()
        valid_regions = data.split("\n")
        return valid_regions


# Rename this
def get_valid_costcenters():
    with open("valid_costcenters.txt") as f:
        data = f.read()
        valid_costcenters = data.split("\n")
        return valid_costcenters


def check_if_domain_is_valid(domain):
    businessgroup_id = domain.split("-")[0]
    if businessgroup_id in get_valid_costcenters():
        region = domain.split("-")[1]
        if region in get_valid_regions():
            return True
    return False





def seperate_valid_entities(_list):
    valid_names = []
    invalid_names = []
    for element in _list:
        domain = element.get("domain")
        if check_if_domain_is_valid(domain):
            appname = get_muleappname_from_domain(domain)
            valid_names.append(appname)
        else:
            invalid_names.append(element)
    return valid_names, invalid_names




def remove_duplicate_values(_list):
    unique_set = set(_list)
    unique_list = list(unique_set)
    return unique_list

    
def get_muleappname_from_domain(domain):
    muleappname_as_list = domain.split("-")[2:]
    muleappname = "-".join(muleappname_as_list)
    return muleappname



def determine_name_and_registration(muleapp_names, element):
    app_registration = "ORPHAN"
    mule_app_name = None
    domain = element.get("domain")
    if check_if_domain_is_valid(domain):
        appname = get_muleappname_from_domain(domain)
        if appname in muleapp_names:
            app_registration = "ATTACHED"
            mule_app_name = appname
            return mule_app_name, app_registration
    return mule_app_name, app_registration
    