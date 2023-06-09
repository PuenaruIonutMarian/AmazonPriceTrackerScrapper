import smtplib
import requests
from bs4 import BeautifulSoup
import lxml

my_email = "YOUR GMAIL"
password_email = "PSSW ID"

url = "AMAZON LINK OF YOUR FAVOURITE PRODUCT"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,ro-RO;q=0.6,ro;q=0.5"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = float((soup.find(name='span', class_='a-price-whole').get_text())[:3])
price_fraction = float(soup.find(name='span', class_='a-price-fraction').get_text())/100
final_price = price+price_fraction
print(final_price)


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password_email)
    if final_price > 270:
        connection.sendmail(from_addr=my_email,
                        to_addrs="DESTINATION EMAIL",
                        msg=f"Subject:Best price! \n\n It's time to buy the product because it's just {final_price} EURO."
                        )

