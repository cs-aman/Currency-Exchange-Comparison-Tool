import requests
import json

# Welcoming In Application
print("Welcome to the currency exchange.The Base Currency is EUR")

# Adding a function for error handling.
def get_exchange_rate(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Failed to fetch data from the API.")
            return None
    except requests.RequestException as e:
        print("Request Exception:", e)
        return None

# Declaring the base Currency and Getting Input for Second Currency
basecurrency = "EUR"
currency = input("Enter currency: ")

# Adding API of Both Exchange Providers
fixer = (f"http://data.fixer.io/api/latest?access_key=0d08fdee18bfba444988679a06fa7a02&symbols={basecurrency},{currency}")
beacon= (f"https://api.currencybeacon.com/v1/latest?api_key=vGhiQ81fq6RxhT79HCSNz8nzMCrIvn6R&base={basecurrency}&symbols={currency}")

# Getting data from API
reqfixer = requests.get(fixer)
reqbeacon = requests.get(beacon)

# Adding Data to a Specific Dictionary for Different Providers
fixerdictionary = json.loads(reqfixer.text)
beacondictionary = json.loads(reqbeacon.text)

rate_fixer = {fixerdictionary["rates"][currency]}
rate_beacon = {beacondictionary["rates"][currency]}
print(rate_fixer)
print(rate_beacon)

# compare and Find the Best Provider
def compare_rates(rate_fixer,rate_beacon):
    if rate_fixer > rate_beacon:
        return ("The Fixer Currency Exchange Providing Best Rates")
    elif rate_fixer < rate_beacon  :
        return ("The Beacon Currency Exchange Providing Best Rates")
    else:
        return ("Both Fixer and Beacon Providing Same Rates")

result = compare_rates(fixer,beacon)
print(result)
# # Printing the Exchange Prices
# print(f"The exchange rate in Fixer.io is 1 {basecurrency} = {fixerdictionary['rates'][currency]}:")
# print(f"The exchange rate in Beacon is 1 {basecurrency} = {beacondictionary['rates'][currency]}")
#
