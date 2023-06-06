import requests
import time

api_key = "057c8c1739e24e69b1ccbc13a215392f"
url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"

response = requests.get(url)
data = response.json()

exchange_rates = data["rates"]

print("Top ten currencies: \n\tUSD \n\tEUR \n\tJPY \n\tGBP \n\tAUD \n\tCAD \n\tCHF \n\tCNY \n\tSEK \n\tNZD")

from_currency = input("\n\nEnter the base currency(USD for example): ").upper()
to_currency = input("Enter the target currency(EUR for example): ").upper()
try:
    amount = float(input("Enter the amount to convert(10 for example): "))
    original_amount = amount / exchange_rates[from_currency]
    converted_amount = round(original_amount * exchange_rates[to_currency], 2)

    print(f"{amount} {from_currency} = {converted_amount} {to_currency}")

    output = input("\nPress ENTER to leave...")
except Exception:
    print("An error ocured...")
    time.sleep(5)
    exit()
