import requests
import json

base_URL = "https://www.reqres.in"

payload = {
    "email": "sydney@fife",
    "password": "pistol"
}
response = requests.post(base_URL + "/api/register", data=payload)
print(json.dumps(response.json(), indent=4))
print(response.status_code)
