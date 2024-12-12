#submit50 cs50/problems/2022/python/bitcoin

import requests
import sys

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit()

try:
    # Convert the command-line argument to a float
    bitcoin = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit()

try:
    # Fetch the current Bitcoin price from an API
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()
    data = response.json()
    price = float(data["bpi"]["USD"]["rate"].replace(",", ""))

    # Calculate the dollar value
    amount = bitcoin * price
    print(f"${amount:,.4f}")
except requests.RequestException as e:
    print(f"Error fetching Bitcoin price: {e}")
    sys.exit()
