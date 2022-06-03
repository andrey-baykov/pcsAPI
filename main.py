from portnovapi import PortnovAPI
import json

with open("package.json") as file:
    data = json.load(file)
    connection = PortnovAPI(data["base_url"])
    login_end_point = "/login"

    if connection.request_token(login_end_point, data["data"]):
        print("Step 1: Done")
    else:
        print("Step 1: False")
        exit()

    candidate_end_point = "/candidates"
    if connection.create_new_candidate(candidate_end_point, data["candidate"]):
        print("Step 2: Done")
    else:
        print("Step 2: False")
        exit()

    if connection.request_token(login_end_point, data["new_candidate_data"]):
        print("Step 3: Done")
    else:
        print("Step 3: False")
        exit()

    position_end_point = "/positions"

    if connection.create_new_position(position_end_point, data["position_data"]):
        print("Step 4: Done")
    else:
        print("Step 4: False")
        exit()

    position = connection.get_position_by_id(position_end_point, connection.company_id)
    if position is not None:
        print("Step 5: Done")
    else:
        print("Step 5: False")
        exit()

    position = connection.update_position_by_id(position_end_point, connection.company_id, data["position_new_data"])
    if position is not None:
        print("Step 6: Done")
    else:
        print("Step 6: False")
        exit()

    if connection.delete(position_end_point, connection.company_id):
        print("Step 7: Done")
    else:
        print("Step 7: False")
        exit()

    if connection.delete(candidate_end_point, connection.candidate_id):
        print("Step 8: Done")
    else:
        print("Step 8: False")
        exit()

    if input("Do you want to see all positions? > 'y/n'") == 'y':
        all_positions = connection.return_all(position_end_point)
        if all_positions is not None:
            for pos in all_positions:
                print(pos)

    if input("Do you want to see all candidates? > 'y/n'") == 'y':
        all_candidates = connection.return_all(candidate_end_point)
        if all_candidates is not None:
            for cand in all_candidates:
                print(cand)
