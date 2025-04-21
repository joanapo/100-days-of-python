import requests
import datetime
import os

USERNAME = os.environ.get("PIXELA_USERNAME")
TOKEN = os.environ.get("PIXELA_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Water Drinking Graph",
    "unit": "ml",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1400"
}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)