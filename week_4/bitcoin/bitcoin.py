import requests
import sys

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
except ValueError:
    sys.exit("Command-line argument is not a number")

dol = float(sys.argv[1])

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
data = response.json()
price = float(data["bpi"]["USD"]["rate"].replace(",", ""))

amount = dol * price
print(f"${amount:,.4f}")

