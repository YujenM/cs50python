import sys
import requests
import json
if len(sys.argv)==1:
    sys.exit("Missing command-line argument")
else:
    input = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    data= input.json()
    price= data["bpi"]["USD"]["rate"]
    new_price =price.replace(",","")
    new_price=(float(new_price)* float(sys.argv[1]))
    print(f"${new_price:,.4f}")
