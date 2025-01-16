import requests


BASE_UL = "https://icanhazdadjoke.com"
API_PAGE = "/api"

URL = BASE_UL + API_PAGE

response = requests.get(URL)
print(response.status_code)
print(response.text)

file_handler = open("jokes.html", "w")
file_handler.write(response.text)
file_handler.close()

