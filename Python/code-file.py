import requests

def get_exchange_rate(api_url):
    response = requests.get(api_url)
    data = response.json() if response.status_code == 200 else None 
    return data
