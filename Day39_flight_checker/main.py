#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from datetime import datetime

APP_ID = "8"
API_KEY = "e"
SHEET_ENDPOINT = "https:"
TOKEN = "aa"

head = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
    }

sheet_data = {
    "workout": {
        "date": "dfg",
        "time":"dfg",
        "exercise": "dfgd",
        "duration": "df",
        "calories": "dfdg"
    }
}
sheet_head = {
    "Authorization": TOKEN
    }
sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_data, headers=sheet_head)
print(sheet_response.text)