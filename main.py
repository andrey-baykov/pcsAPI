import requests

BASE_URL = "http://recruit-qa.portnov.com/recruit/api/v1"

# Login to request token
data = {
  "email": "john@doe.com",
  "password": "12345"
}
token = {"Authorization": ""}
new_candidate_token = {"Authorization": ""}

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

response = requests.post(BASE_URL + "/candidates", json=candidate, headers=token)
if response.status_code != 201:
    print(f"{response.status_code}: Can't create a new candidate. Maybe it is exists")
else:
    lines = response.json()
    candidate_id = lines["id"]
    print(lines)
    print(f"New id: {candidate_id}")

# Login as new candidate
new_candidate_data = {
  "email": "john@doe.com",
  "password": "12345"
}

new_candidate_token = {"Authorization": ""}
response = requests.post(BASE_URL + "/login", json=new_candidate_data)
if response.status_code != 200:
    print(f"{response.status_code}: Can't reach token")
    exit()
else:
    new_candidate_token["Authorization"] = "Bearer " + response.json()['token']
print(token)
print(new_candidate_token)

exit()
# Reach list of all candidates
response = requests.get(BASE_URL + "/candidates/", headers=token)
lines = response.json()
for line in range(len(lines)):
    print(lines[line])
