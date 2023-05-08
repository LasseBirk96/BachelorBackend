def merge_keys_with_values(keys, values):
    center_list = []
    for element in values:
        alist = list(element)
        center = dict(zip(keys, alist))
        center_list.append(center)
        if len(center_list) == 0:
            return center_list[0]
    return center_list


# This essentially checks if the request is empty, this is important to know due to how data is filtered
def check_if_no_keys(data):
    if len(data.keys()) == 0:
        return True
    return False

def lowercase_keys_to_list(data):
   return list({k.lower(): v for k, v in data.items()})
    
def lowercase_keys_to_dict(data):
    return dict((k.lower(), v) for k, v in data.items()) 