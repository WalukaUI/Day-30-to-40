import requests
from datetime import datetime
import os

APP_ID = "8"
API_KEY = "e"
SHEET_ENDPOINT = "https:"
TOKEN = "aa"

urls = "https://trackapi.nutritionix.com/v2/natural/exercise"
question = input("Which exe you did ?  ")
head = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
    }
json_data = {
    "query": question,
    "gender": "male",
    "weight_kg": 60,
    "height_cm": 166,
    "age": 33
}
res = requests.post(url=urls, json=json_data, headers=head)
processed_data = res.json()
print(processed_data)
today = datetime.now().date()
today_time = datetime.now().time()

sheet_data = {
    "workout": {
        "date": today.strftime("%Y/%m/%d"),
        "time": today_time.strftime("%H:%M:%S"),
        "exercise": processed_data["exercises"][0]["user_input"].title(),
        "duration": processed_data["exercises"][0]["duration_min"],
        "calories": processed_data["exercises"][0]["nf_calories"]
    }
}
sheet_head = {
    "Authorization": TOKEN
    }
sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_data, headers=sheet_head)
print(sheet_response.text)
