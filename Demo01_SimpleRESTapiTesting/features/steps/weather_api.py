import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=London&APPID=."

rsp = requests.get(url)
print(rsp)