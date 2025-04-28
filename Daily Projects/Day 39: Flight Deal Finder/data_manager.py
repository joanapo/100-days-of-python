import requests
import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/455af28989f6a31a97fded89b45046c8/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.sheety_username = os.environ["SHEETY_USERNAME"]
        self.sheety_password = os.environ["SHEETY_PASSWORD"]
        self.authorization = HTTPBasicAuth(self.sheety_username, self.sheety_password)

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, auth=self.authorization)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_iata_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}",
                                    json=new_data,
                                    auth=self.authorization)

            print(response.text)


