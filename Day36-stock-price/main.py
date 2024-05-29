import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid= 'ACac88cxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token='4ff26bxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
stock_url = 'https://www.alphavantage.co/query?'
stock_api_key = "SCAxxxxxxxxxxxxxxxxxxxxxx"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}

news_api = "245ddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
news_url = "https://newsapi.org/v2/everything?"
news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": news_api
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_res = requests.get(url=stock_url, params=stock_params)
stock_res.raise_for_status()
stock_data = stock_res.json()
dbf_yesterday_rate = float(stock_data['Time Series (Daily)']['2024-05-23']['4. close'])
yesterday_rate = float(stock_data['Time Series (Daily)']['2024-05-24']['4. close'])


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_res = requests.get(url=news_url, params=news_params)
news_res.raise_for_status()
news_data = news_res.json()
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
the_difference = yesterday_rate -dbf_yesterday_rate
trend = None
if the_difference > 0:
    trend = "😊"
else:
    trend = "😒"
# abs() , get the value of the answer without + or -
print(the_difference)

diff_percentage = round((the_difference / yesterday_rate) * 100)
print(diff_percentage)

if abs(diff_percentage) > 2:
    articles = news_data['articles'][0:3]
    articles_list = [f"{STOCK}: {trend} {diff_percentage}%\n Headline: {key['title']}, \n Brief: {key['description']}" for key in articles]
    print(articles_list)
    client = Client(account_sid, auth_token)
    for msg in articles_list:
        message = client.messages.create(
        from_='+18339xxxxx',
        body = msg,
        to = '+16363xxxxx'
        )
        print(message.sid)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

