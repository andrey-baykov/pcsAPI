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

