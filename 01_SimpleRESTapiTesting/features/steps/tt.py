import requests
import json

global_general_variables = {}
http_request_header = {}
http_request_body = {}

base_URL = "https://reqres.in"

payload = {
    "email": "sydney@fife",
    "password": "pistol"
}
global_general_variables['response_full'] = requests.post(base_URL + "/api/register", data=payload)
# resp = response.json()
# head=resp.header("Content-Type");
# print(resp)
current_json = global_general_variables.get('response_full').json()
actual_response_code = global_general_variables['response_full'].status_code
print(actual_response_code)
