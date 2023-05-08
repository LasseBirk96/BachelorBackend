from LogicLayer.Entities.CostCenter import CostCenter
from dacite import from_dict
from nanoid import generate

import re

# FIX THE REGEX ISSUE WITH LENGTH
def sanitize_entry(entry):
        if entry == None:
            return False
        regex = r"\b^[a-åA-Å_]+$\b"
        if re.match(regex, entry):
           return True
        return False
    

def sanitize_approver_name(name):
        if name == None:
            return False
        regex = r"\b^[a-åA-Å_ ]*$\b"
        if re.match(regex, name):
            return True
        return False
    
def capitalize_entry(entry):
    return entry.upper()
    
def capitalize_approver_name(approver_name):
    approver_name_as_list = approver_name.split()
    name_capitalized = str()
    for element in approver_name_as_list:
            name_capitalized = name_capitalized + ' ' + element.title()
    return name_capitalized[1:]


def validate_body(request_body):
    
    if sanitize_entry(request_body.get("Label")) is not True:
        raise TypeError("Input for Label is invalid - Please check the guide")
    if sanitize_approver_name(request_body.get("ApproverName")) is not True:
        raise TypeError("Input for Approver Name is invalid - Please check the guide")
    if sanitize_entry(request_body.get("ApproverInitials")) is not True:
        raise TypeError("Input for Approver Inititals is invalid - Please check the guide")

    
    id = generate(size=10)
    request_body["Id"] = id
    request_body["Label"] = capitalize_entry(request_body.get("Label"))
    request_body["ApproverName"] = capitalize_approver_name(request_body.get("ApproverName"))
    request_body["ApproverInitials"] = capitalize_entry(request_body.get("ApproverInitials"))
    costcenter = from_dict(data_class=CostCenter, data=request_body)
    
    return costcenter


