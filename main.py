import requests
import subprocess
import sys
sys.setrecursionlimit(15000)

your_value = float(input("What is your expected value for Bitcoin ?(e.g 20000.0000): "))
print(f"Your expected value is {your_value}. We will let you know when the price of Bitcoin is less than {your_value}.")

def alert():
    subprocess.call(["afplay","alert.mp3"])

def bitcoin(currency = "USD"):
    currency = currency
    api = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(api)
    value = response.json()["bpi"][currency]["rate_float"]

    if value < your_value:
        alert()
    else:
        bitcoin()
bitcoin()
 





