import requests


class PortnovAPI:
    company_id = None
    candidate_id = None
    token = {"Authorization": ""}
    base_url = None

    def __init__(self, base_url):
        self.base_url = base_url

    def request_token(self, end_point, json_data):
        response = requests.post(self.base_url + end_point, json=json_data)
        if response.status_code != 200:
            return False
        else:
            self.token["Authorization"] = "Bearer " + response.json()['token']
            return True

    def create_new_candidate(self, end_point, candidate_data):
        response = requests.post(self.base_url + end_point, json=candidate_data, headers=self.token)
        if response.status_code != 201:
            return False
        else:
            body = response.json()
            self.candidate_id = body["id"]
            return True

    def create_new_position(self, end_point, position_data):
        response = requests.post(self.base_url + end_point, json=position_data, headers=self.token)
        if response.status_code != 201:
            return False
        else:
            body = response.json()
            self.company_id = body["id"]
            return True

    def get_position_by_id(self, end_point, position_id):
        response = requests.get(self.base_url + end_point + "/" + str(position_id), headers=self.token)
        if response.status_code != 200:
            return None
        else:
            return response.json()

    def update_position_by_id(self, end_point, position_id, new_data):
        response = requests.put(self.base_url + end_point + "/" + str(position_id), json=new_data, headers=self.token)
        if response.status_code != 200:
            return None
        else:
            return response.json()

    def delete(self, end_point, data_id):
        response = requests.delete(self.base_url + end_point + "/" + str(data_id), headers=self.token)
        if response.status_code != 204:
            return False
        else:
            return True

    def return_all(self, end_point):
        response = requests.get(self.base_url + end_point + "/", headers=self.token)
        if response.status_code != 200:
            return None
        else:
            return response.json()


BASE_URL = "http://recruit-qa.portnov.com/recruit/api/v1"

connection = PortnovAPI(BASE_URL)

data = {
  "email": "john@doe.com",
  "password": "12345"
}
login_end_point = "/login"

if connection.request_token(login_end_point, data):
    print("Step 1: Done")
else:
    print("Step 1: False")
    exit()

candidate = {
  "firstName": "Bumble",
  "middleName": "Jr",
  "lastName": "Bee",
  "email": "bmbl@bee.com",
  "password": "789456",
  "address": "2704 El Dorado Hills",
  "city": "Sacramento",
  "state": "California",
  "zip": "95680",
  "summary": "Account for the perfect person"
}
candidate_end_point = "/candidates"

if connection.create_new_candidate(candidate_end_point, candidate):
    print("Step 2: Done")
else:
    print("Step 2: False")
    exit()

new_candidate_data = {
  "email": "bmbl@bee.com",
  "password": "789456"
}

if connection.request_token(login_end_point, new_candidate_data):
    print("Step 3: Done")
else:
    print("Step 3: False")
    exit()

position_data = {
    "title": "Manual tester",
    "address": "1st Main campus",
    "city": "San Jose",
    "state": "CA",
    "zip": "93145",
    "description": "SQA Automation engineer on python. Needs to automate all in the our company",
    "dateOpen": "2022-05-30",
    "company": "Space technologies"
}

position_end_point = "/positions"

if connection.create_new_position(position_end_point, position_data):
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

position_new_data = {
    "title": "Python SQA automation engineer",
    "address": "1st Main campus",
    "city": "San Jose",
    "state": "CA",
    "zip": "93145",
    "description": "SQA Automation engineer on python. Needs to automate all in the our company",
    "dateOpen": "2022-05-30",
    "company": "Space technologies inc"
}
position = connection.update_position_by_id(position_end_point, connection.company_id, position_new_data)
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
