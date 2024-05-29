import requests, smtplib
from datetime import datetime as dt
import time

MYLAT = 38.710006
MYLNG = -90.312565
MYEMAIL = "XXXXXXXXXXX"
MYPW = "XXXXXXXXXX"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    isslat = float(data["iss_position"]["latitude"])
    isslng = float(data["iss_position"]["longitude"])

    if MYLAT - 5 <= isslat <= MYLAT + 5 and MYLNG - 5 <= isslng <= MYLNG + 5:
        return True


def is_night():
    param = {
        "lat": MYLAT,
        "lng": MYLNG,
        "formatted": 0,
    }
    res = requests.get("https://api.sunrise-sunset.org/json", params=param)
    res.raise_for_status()
    data = res.json()
    sunrisehour = int(data["results"]["sunrise"].split("T")[1][0:2])
    sunsethour = int(data["results"]["sunset"].split("T")[1][0:2])
    timenow = dt.now().hour
    if timenow >= sunsethour or timenow < sunrisehour:
        return True


def send_email():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MYEMAIL, MYPW)
    connection.sendmail(from_addr=MYEMAIL, to_addrs=MYEMAIL, msg="Subject:ISS \n\n Look up")


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        send_email()
