from DatabaseLayer.Queries.misc import dict_keys_helper



# ------------------------------------ START OF MICS FUNCTIONS TESTS ------------------------------------ #

# TEST IF THE KEYS AND VALUES OF TWO LISTS ARE MERGED CORRECTLY - IS USED WHEN RETURNING DATA FROM POSTGRES
def test_if_keys_and_values_are_merged_correctly():
    keys = ["id", "name", "age"]
    values = [("1", "lasse", "23")]
    entity = dict_keys_helper.merge_keys_with_values(keys, values)
    assert entity[0].get("name")=="lasse"
    
    
# TESTS IF DICTIONARY IS EMPTY OR NOT  IS USED WHEN A GET-REQUEST IS MADE
def test_check_if_no_keys():
    assert dict_keys_helper.check_if_no_keys(data={}) == True
    
    
    
    
def test_lowercase_keys_to_dict():
    data = {"NAME":"Lasse"}
    new_dict = dict_keys_helper.lowercase_keys_to_dict(data)
    entry = list(new_dict.keys())[0]
    assert (entry == "name") and (type(new_dict) == dict)
    


def test_lowercase_keys_to_list():
    data = {"NAME":"Lasse"}
    new_list = dict_keys_helper.lowercase_keys_to_list(data)
    assert (new_list[0] == "name") and (type(new_list) == list)
    
    
    

# ------------------------------------ END OF MICS FUNCTIONS TESTS ------------------------------------ #