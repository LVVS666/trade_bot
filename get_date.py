import os
import requests

from coinbase.wallet.client import Client
from okx.MarketData import MarketAPI
from dotenv import load_dotenv

import data

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


def get_price_coin_in_okx(coin):
    '''Получение цены монеты на okx '''
    api = MarketAPI(flag='1', domain='https://www.okx.cab', debug=False)
    price_coin_okx = api.get_ticker(f'{coin.name}-{coin.currency}')['data'][0]['last']
    return price_coin_okx

def get_proce_coin_in_coinbase(coin):
    client = Client(api_key='КЛЮЧ АПИ', api_secret='СЕКРЕТНЫЙ КЛЮЧ')
    price_coin_coin_base = client.get_spot_price(currency_pair=f'{coin.name}-{coin.currency}')
    return price_coin_coin_base


def get_comparison_price(coin, network, market):
    '''Сравнение цен на разных биржах'''
    pass


