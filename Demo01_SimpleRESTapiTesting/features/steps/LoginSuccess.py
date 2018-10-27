import requests
import json
from Demo01_SimpleRESTapiTesting.features.steps.keys import *

base_URL = "https://www.reqres.in"

payload = {
    "email": "USERNAME",
    "password": "PASSWORD"
}
response = requests.post(base_URL + "/api/login", data=payload)
print(json.dumps(response.json(), indent=4))
print(response.status_code)
