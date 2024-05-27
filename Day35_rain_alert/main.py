import requests
from twilio.rest import Client

endpoint = "https://api.openweathermap.org/data/2.5/forecast"
application_id = "check in env"
myparams = {
    "lat": 38.627003,
    "lon": -90.199402,
    "cnt": 4,
    "appid": application_id,
}
account_sid = "check in env"
auth_token = "check in env"

res = requests.get(endpoint, params=myparams)
res.raise_for_status()
weather_data = res.json()
weather_list = weather_data["list"]
will_rain = False
for x in weather_list:
    condition_code = x["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        print(condition_code)

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='+18339221992',
    body = 'use a umbrella 😊',
    to = '+16363872053'
    )
    print(message.sid)
    print("Bring an Umbrella")



