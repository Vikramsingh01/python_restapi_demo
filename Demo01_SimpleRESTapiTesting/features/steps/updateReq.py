import requests
import json

base_URL = "https://www.reqres.in"

payload = {
    "name": "morpheus",
    "job": "zion resident"
}
response = requests.put(base_URL + "/api/users/2", data=payload)
# print(json.dumps(response.json(), indent=4))
print(response.status_code)
