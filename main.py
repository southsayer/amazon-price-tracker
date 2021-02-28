from bs4 import BeautifulSoup
from pprint import pprint
from re import sub
from decimal import Decimal
import requests
import smtplib

my_email = "akshitgaur.sky21@gmail.com"
my_password = "**********"
your_email = "akshit.gaur1214@gmail.com"
min_price = 16000
URL = "https://www.amazon.in/Test-Exclusive-558/dp/B077PWJRFH/ref=sr_1_3?crid=3B8MXPYS0HK9I&dchild=1&keywords=xiaomi+redmi+note+9+pro&qid=1610969038&sprefix=xi%2Caps%2C381&sr=8-3"

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}

response = requests.get(url=URL, headers=headers)
amazon_wpg = response.text

soup = BeautifulSoup(amazon_wpg, "html.parser")
product_price_tag = soup.find(name="span", class_="a-size-medium a-color-price priceBlockDealPriceString")
# print(product_price_tag)
product_price = product_price_tag.getText()
print(product_price)

money = product_price
value = float(Decimal(sub(r'[^\d.]', '', money)))
print(value)

#***************************TO SEND MAIL IF PRICE IS LOWER THAN SELLING PRICE***************************
if value < min_price:
    print("so cheap")
    difference= min_price - value
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    message = f"subject:Price Alert!\n\nThe price of your product"
    f" is less than the selling price {product_price}.\n"
    f"Order now to get profit!"
    connection.sendmail(from_addr=my_email, to_addrs=your_email, msg=f"subject:Price Alert!\n\nThe price of your product"
                                                                     f" is less than the selling price {product_price}.\n"
                                                                     f"Order now to get profit!".encode('utf-8'))

    connection.close()
