# from LogicLayer.anypoint_api_calls import get_access_token, get_organization_id, get_suborganizations, get_environments_by_organization_id, get_applications_by_ids
# from decouple import config


# # THESE TESTS NEED TO B
# client_id = config('client_id')
# client_secret = config('client_secret')
# access_token = get_access_token(client_id, client_secret).response

# # THERE IS A DIFFERNECE BETWEEN STATUS AND STATUS CODE -  FIX THIS LATER
# def test_get_access_tokes_returns_200():
#     response_code = get_access_token(client_id, client_secret).status
#     assert response_code == 200
    
    
# def test_get_organization_id_returns_200():
#     response_code = get_organization_id(access_token).status
#     assert response_code == 200

# def test_get_suborganizations_returns_200():
#     organization_id  = get_organization_id(access_token).response
#     response_code = get_suborganizations(organization_id, access_token).status
#     assert response_code == 200
    
# def test_get_environments_by_organization_id_returns_200():
#     organization_id  = get_organization_id(access_token).response
#     orgs = get_suborganizations(organization_id, access_token).response
#     response_code = get_environments_by_organization_id(orgs, access_token).status
#     assert response_code == 200
    
    
# def test_get_applications_by_ids_returns_200():
#     organization_id  = get_organization_id(access_token).response
#     orgs = get_suborganizations(organization_id, access_token).response
#     envs = get_environments_by_organization_id(orgs, access_token).response
#     response_code = get_applications_by_ids(envs, access_token).status
#     assert response_code == 200
    
    


