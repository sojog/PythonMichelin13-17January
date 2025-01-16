import requests
from pprint import pp, pprint
import json

BASE_UL = "https://icanhazdadjoke.com"
API_PAGE = ""

URL = BASE_UL + API_PAGE

header_dict = {
    "Accept" : "application/json"
}

response = requests.get(URL,headers=header_dict)
print(response.status_code)
print(type(response.text))

json_response = json.loads(response.text)
print(type(json_response))
pprint(json_response)



pp(response.text)

with open("jokes.json", "w") as file_handler:
    file_handler.write(response.text)


