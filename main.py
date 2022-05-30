import requests

BASE_URL = "http://recruit-qa.portnov.com/recruit/api/v1"

# Login to request token
data = {
  "email": "john@doe.com",
  "password": "12345"
}
token = {"Authorization": ""}

response = requests.post(BASE_URL + "/login", json=data)
if response.status_code != 200:
    print(f"{response.status_code}: Can't reach token")
    exit()
else:
    token["Authorization"] = "Bearer " + response.json()['token']

# Create a new candidate
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

response2 = requests.post(BASE_URL + "/candidates", json=candidate, headers=token)
if response2.status_code != 201:
    print(f"{response2.status_code}: Can't create a new candidate. Maybe it is exists")
else:
    lines2 = response2.json()
    candidate_id = lines2["id"]
    print(lines2)
    print(f"New id: {candidate_id}")

# Login as new candidate
new_candidate_data = {
  "email": "john@doe.com",
  "password": "12345"
}

response3 = requests.post(BASE_URL + "/login", json=new_candidate_data)
if response3.status_code != 200:
    print(f"{response3.status_code}: Can't reach token")
    exit()
else:
    token["Authorization"] = "Bearer " + response3.json()['token']

# Create a new position
position_data = {
    "title": "Python QA automation engineer",
    "address": "1st Main campus",
    "city": "San Jose",
    "state": "CA",
    "zip": "93145",
    "description": "SQA Automation engineer on python. Needs to automate all in the our company",
    "dateOpen": "2022-05-30",
    "company": "Space technologies"
}

response4 = requests.post(BASE_URL + "/positions", json=position_data,  headers=token)
if response4.status_code != 201:
    print(f"{response4.status_code}: Can't create a new position. Maybe it is exists")
else:
    lines4 = response4.json()
    company_id = lines4["id"]
    print(lines4)
    print(f"New id: {company_id}")


exit()
# Reach list of all candidates
response = requests.get(BASE_URL + "/candidates/", headers=token)
lines = response.json()
for line in range(len(lines)):
    print(lines[line])
