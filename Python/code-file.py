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