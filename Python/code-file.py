import requests

# API keys
FIXER_API_KEY = 'e97fb0b3595af6cb6b3fc68ab7ea2f18'
CURRENCYLAYER_API_KEY = 'e627f8621da14745a34fd34b4eab46f2'

# Base URLs
FIXER_API_URL = 'http://data.fixer.io/api/latest'
CURRENCYLAYER_API_URL = 'http://apilayer.net/api/live'

def get_fixer_rate(base_currency, target_currency):
    url = f"{FIXER_API_URL}?access_key={FIXER_API_KEY}&base={base_currency}&symbols={target_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['rates'][target_currency]
    else:
        print(f"Error with Fixer API: {response.status_code}")
        return None

def get_currencylayer_rate(source_currency, target_currency):
    url = f"{CURRENCYLAYER_API_URL}?access_key={CURRENCYLAYER_API_KEY}&currencies={target_currency}&source={source_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['quotes'][f"{source_currency}{target_currency}"]
    else:
        print(f"Error with CurrencyLayer API: {response.status_code}")
        return None

def compare_rates(base_currency, target_currency):
    fixer_rate = get_fixer_rate(base_currency, target_currency)
    currencylayer_rate = get_currencylayer_rate(base_currency, target_currency)
    
    if fixer_rate and currencylayer_rate:
        print(f"Fixer Rate: {fixer_rate}")
        print(f"CurrencyLayer Rate: {currencylayer_rate}")
        
        if fixer_rate > currencylayer_rate:
            print(f"Best Rate: {fixer_rate} (Fixer API)")
        else:
            print(f"Best Rate: {currencylayer_rate} (CurrencyLayer API)")
    else:
        print("Could not fetch rates from both APIs.")

# Example usage
base_currency = 'EUR'
target_currency = 'USD'
compare_rates(base_currency, target_currency)
