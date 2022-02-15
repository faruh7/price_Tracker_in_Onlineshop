import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
MY_EMAIL = "blah.blah@gmail.com"
MY_PASSWORD = "password"
header = {
    "Accept-Language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,lv;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71"
                  " Safari/537.36",
}
response = requests.get("https://www.amazon.com/dp/B091TTDRVP/ref=syn_sd_onsite_desktop_174?psc=1&pd_rd_plhdr=t&spLa"
                        "=ZW5jcnlwdGVkUXVhbGlmaWVyPUExOVdXWVNLM1BGV0Q3JmVuY3J5cHRlZElkPUEwMzUyMzI3MllGSTQ0UEFTMzJSWSZ"
                        "lbmNyeXB0ZWRBZElkPUEwMjE0MTg5MjZBSlJBQjdXRldGVSZ3aWRnZXROYW1lPXNkX29uc2l0ZV9kZXNrdG9wJmFjdGlv"
                        "bj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==", headers=header)
data = response.text
soup = BeautifulSoup(data, "lxml")
price = float(soup.find("span", class_="a-offscreen").getText().split("$")[1])

if price < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="some_email@inbox.ru",
            msg=f"Subject:Goods in sale\nPlease check"
        )
