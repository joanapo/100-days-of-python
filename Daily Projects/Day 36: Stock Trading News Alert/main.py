import requests
import os
from twilio.rest import Client
from statistics import mean

STOCK_NAME = "NFLX"
COMPANY_NAME = "Netflix, Inc."

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()

stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

yesterday_closing_price = float(stock_data_list[0]["4. close"])
day_before_yesterday_closing_price = float(stock_data_list[1]["4. close"])

diff = yesterday_closing_price-day_before_yesterday_closing_price

up_down = None
if diff > 0:
    up_down = "🔺"
elif diff < 0:
    up_down = "🔻"

abs_diff = abs(diff)
percentage_diff = abs_diff/mean([yesterday_closing_price, day_before_yesterday_closing_price]) * 100

if percentage_diff > 5:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()

    news_data = news_response.json()["articles"]
    last_three_articles = news_data[:3]
    article_list = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in last_three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in article_list:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f"{STOCK_NAME}: {up_down}{round(percentage_diff)}% \n{article}",
            to='whatsapp:+37066146888'  # insert your whatsapp phone number here
        )


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

