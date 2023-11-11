import os

import requests

from dotenv import load_dotenv

load_dotenv()

url = "https://api.cryptorank.io/v1/currencies"
api_key = os.getenv('API_KEY')


params = {
    'api_key': api_key,
    'symbols': 'BTC',
    'convert': 'USD'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    # Обработка данных от API
    # Цена биткоина будет доступна в data['data'][0]['price']
    print(data['data'])
else:
    print(f"Ошибка при запросе к API: {response.status_code}")