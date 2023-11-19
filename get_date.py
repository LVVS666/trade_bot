import os
import requests

from coinbase.wallet.client import Client
from dotenv import load_dotenv

import data_coin

load_dotenv()

API_KEY_MEXC = os.getenv('API_KEY_MEXC')
SECRET_KEY_MEXC = os.getenv('SECRET_KEY_MEXC')


def get_price_coin_in_mexc(coin):
    '''Получение цены монеты на mexc'''
    url_api_mexc = "https://api.mexc.com/api/v3/ticker/price"
    params = {
        'symbol': f'{coin.name}{coin.currency}',
        'interval': '1m',
        'limit': 10
    }
    price_coin_mexc = requests.get(url_api_mexc, params=params).json()['price']
    return price_coin_mexc


def get_price_coinsbit(coin):
    '''Получение цены монеты на coinsbit'''
    url_api_coinsbit = requests.get(' https://coinsbit.io/api/v1/public/tickers')
    price_coin_coinsbit = url_api_coinsbit.json()['result'][f'{coin.name}_{coin.currency}']['ticker']['last']
    return price_coin_coinsbit


def get_proce_coin_in_coinbase(coin):
    '''Получение цены монеты на coinbase'''
    client = Client(api_key='КЛЮЧ АПИ', api_secret='СЕКРЕТНЫЙ КЛЮЧ')
    price_coin_coin_base = client.get_spot_price(currency_pair=f'{coin.name}-{coin.currency}')
    return price_coin_coin_base


def get_comparison_price(coin, network, market):
    '''Сравнение цен на разных биржах'''
    pass



