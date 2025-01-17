import requests

URL = "https://dontpad.com/csvmichelin"

response = requests.get(URL)
print(response.text)