import smtplib
import datetime as dt
import random

PP = "xxxxxxxxxx"
mailer = "xxxxxxxxxxxx"

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
if day_of_week == 0:
    with open("quotes.txt", encoding="utf8")as files:
        quotes = files.readlines()
        quote = random.choice(quotes)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=mailer, password=PP)
            connection.sendmail(from_addr=mailer, to_addrs="cwaluka@yahoo.com", msg=f"Subject: Hello \n\n {quote}")


