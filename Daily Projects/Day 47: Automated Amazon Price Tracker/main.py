import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from email_manager import EmailManager

load_dotenv() #environment variables

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
TARGET_PRICE = 100

email_manager = EmailManager()
recipient = os.environ["TO_EMAIL"]

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.3.1 Safari/605.1.15",
                         "Accept-Language": "en-GB,en;q=0.9"}

response = requests.get(URL, headers=headers)
amazon_data = response.text

soup = BeautifulSoup(amazon_data, "html.parser")
# find the current price on the amazon website
current_price = soup.find(name="span", class_="a-offscreen").getText().strip()
# remove the dollar sign from the price and convert the value into a float
number_only_price = float(current_price.split("$")[1])

# find the name of the product and strip it of whitespace
name = soup.find(name="span", id="productTitle").getText().strip()

# compare the target price and current price
if number_only_price < float(TARGET_PRICE):
    email_body = f"{name} is now only {current_price}."
    email_manager.send_email(recipient=recipient, email_body=email_body)