from bs4 import BeautifulSoup
import requests
import smtplib

# ------------------------------------ CONSTANTS ------------------------------------ #

# Go to https://myhttpheader.com/ and pass in the following headers
HEADERS = {
    "User-Agent": "",
    "Accept-Language": "",
    "Accept-Encoding": "",
}
URL = ""  # Your amazon product url

YOUR_EMAIL = ""
YOUR_PASSWORD = ""
SMTP_SERVER_NAME = "smtp.gmail.com"  # update based on your email account
DESIRED_PRICE = 0

response = requests.get(url=URL, headers=HEADERS)
webpage = response.content
soup = BeautifulSoup(webpage, "lxml")
price = soup.find(name="span", class_="a-price-whole").get_text()
title = soup.find(name="span", id="productTitle").get_text().strip()

if float(price) < DESIRED_PRICE:
    with smtplib.SMTP(SMTP_SERVER_NAME) as connection:
        connection.starttls()
        connection.login(user=YOUR_EMAIL, password=YOUR_PASSWORD)
        connection.sendmail(from_addr=YOUR_EMAIL,
                            to_addrs=YOUR_EMAIL,
                            msg=f"Subject:Amazon price alert!\n\n{title} is now available for Rs.{price}.\n{URL}")
