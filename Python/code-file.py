import requests

def get_exchange_rate(api_url):
    response = requests.get(api_url)
    data = response.json() if response.status_code == 200 else None 
    return data

#Define API URL
fixer_api_key = 'YOUR_FIXER_API_KEY'
fixer_url = f'http://data.fixer.io/api/latest?access_key={fixer_api_key}'

# Get exchange rate data from Fixer
exchange_data = get_exchange_rate(fixer_url)
print(exchange_data)

def compare_exchange_rates(currency_1, currency_2):
    # Construct API URLs for different currencies
    fixer_api_key = 'YOUR_FIXER_API_KEY'
    fixer_url = f'http://data.fixer.io/api/latest?access_key={fixer_api_key}&symbols={currency_1},{currency_2}'

    currency_beacon_api_key = 'YOUR_CURRENCY_BEACON_API_KEY'
    currency_beacon_url = f'https://api.currencybeacon.com/v1/latest?api_key={currency_beacon_api_key}&base={currency_1}&symbols={currency_2}'
 # Get exchange rate data from Fixer and Currency Beacon APIs
    fixer_data = get_exchange_rate(fixer_url)
    currency_beacon_data = get_exchange_rate(currency_beacon_url)