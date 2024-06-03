import requests
from flight_search import FlightSearch

SHEET_ENDPOINT = "https://ap"
TOKEN = "B"


class DataManager:
    def __init__(self):
        self.sheet_head = {
            "Authorization": TOKEN
        }

    def get_sheet_data(self):
        sheet_response = requests.get(url=SHEET_ENDPOINT, headers=self.sheet_head)
        sheet_response.raise_for_status()
        return sheet_response.json()["prices"]

    def update_sheet(self, code, idnum):
        new_data = {
            "price": {
                "iataCode": code
            }
        }
        sheet_response = requests.put(url=f"{SHEET_ENDPOINT}/{idnum}", json=new_data,  headers=self.sheet_head)
        sheet_response.raise_for_status()
        print(sheet_response.text)

