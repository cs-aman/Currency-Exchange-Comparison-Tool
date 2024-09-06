import requests

# API keys
FIXER_API_KEY = 'e97fb0b3595af6cb6b3fc68ab7ea2f18'
CURRENCYBEACON_API_KEY = '2hfC6b0eeEKhyBg4onxif4o9HGTWNQUD'

# Base URLs
FIXER_API_URL = 'http://data.fixer.io/api/latest'
CURRENCYBEACON_API_URL = 'https://api.currencybeacon.com/v1/latest'

# Function to get rates from Fixer API
def get_fixer_rate(base_currency, target_currency):
    url = f"{FIXER_API_URL}?access_key={FIXER_API_KEY}&base={base_currency}&symbols={target_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['rates'][target_currency]
    else:
        print(f"Error with Fixer API: {response.status_code}")
        return None

# Function to get rates from CurrencyBeacon API
def get_currencybeacon_rate(base_currency, target_currency):
    url = f"{CURRENCYBEACON_API_URL}?api_key={CURRENCYBEACON_API_KEY}&base={base_currency}&symbols={target_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['response']['rates'][target_currency]
    else:
        print(f"Error with CurrencyBeacon API: {response.status_code}")
        return None

# Function to compare rates from both APIs
def compare_rates(base_currency, target_currency):
    fixer_rate = get_fixer_rate(base_currency, target_currency)
    currencybeacon_rate = get_currencybeacon_rate(base_currency, target_currency)
    
    if fixer_rate and currencybeacon_rate:
        print(f"Fixer Rate: {fixer_rate}")
        print(f"CurrencyBeacon Rate: {currencybeacon_rate}")
        
        if fixer_rate > currencybeacon_rate:
            print(f"Best Rate: {fixer_rate} (Fixer API)")
        else:
            print(f"Best Rate: {currencybeacon_rate} (CurrencyBeacon API)")
    else:
        print("Could not fetch rates from both APIs.")

# Example usage
base_currency = 'EUR'
target_currency = 'USD'
compare_rates(base_currency, target_currency)
