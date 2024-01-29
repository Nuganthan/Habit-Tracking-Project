import requests
import os
from datetime import datetime

TOKEN = os.environ["TOKEN"]
USERNAME = os.environ["USERNAME"]
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_config = {
    "id": "graph1",
    "name": "Cycling",
    "unit": "kilometer",
    "type": "float",
    "color": "sora"
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.today().strftime('%Y%m%d')
pixel_data = {
    "date": today,
    "quantity": input("How many Kilometer Did you cycled today: ")
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# Update pixela data
update_endpoint = (f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/"
                   f"{datetime(day=27, month=1, year=2024).strftime('%Y%m%d')}")
update_data = {
    "quantity": "3"
}
# response = requests.put(url=update_endpoint, json=update_data, headers=headers)
# print(response.text)

# Delete the pixel
delete_endpoint = (f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/"
                   f"{datetime(day=29, month=1, year=2024).strftime('%Y%m%d')}")
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
