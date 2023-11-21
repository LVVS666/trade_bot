import os
from dotenv import load_dotenv
import requests

import data_coin

load_dotenv()

def get_price_coin_in_coinsbit(coin):
    '''Получение цены монеты на coinsbit'''
    url_api_coinsbit = requests.get(' https://coinsbit.io/api/v1/public/tickers')
    price_coin_coinsbit = url_api_coinsbit.json()['result'][f'{coin.name}_{coin.currency}']['ticker']['last']
    return price_coin_coinsbit




def get_price_coin_in_kucoin(coin):
    '''Получение цены монеты на Kucoin'''
    response = requests.get(f'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={coin.name}-{coin.currency}')
    return response.json()['data']['price']


def get_price_coin_in_bitget(coin):
    '''Получение цены монеты на Bitget'''
    response = requests.get(f'https://api.bitget.com/api/v2/spot/market/tickers?symbol={coin.name}{coin.currency}')
    return response.json()['data'][0]['lastPr']

import datetime
import json
import hmac
import base64
def get_time():
    now = datetime.datetime.utcnow()
    t = now.isoformat("T", "milliseconds")
    return t + "Z"


def signature(timestamp, request_type, endpoint, body, secret):
    if body != '':
        body = json.dumps(body)
    message = str(timestamp) + str.upper(request_type) + endpoint + body
    print(message)
    mac = hmac.new(bytes(secret, encoding='utf-8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d)


def get_header(request_type, endpoint, body):
    time = get_time()
    header = dict()
    header['CONTENT-TYPE'] = 'application/json'
    header['OK-ACCESS-KEY'] = os.getenv('API_KEY_OKX')
    header['OK-ACCESS-SIGN'] = signature(time, request_type, endpoint, body, os.getenv('SECRET_KEY_OKX'))
    header['OK-ACCESS-TIMESTAMP'] = str(time)
    header['OK-ACCESS-PASSPHRASE'] = os.getenv('PASSPHRASE_OKX')
    return header


def get(endpoint, body=''):
    ROOT_URL = 'https://www.okx.com'
    url = ROOT_URL + endpoint
    header = get_header('GET', endpoint, body)
    return requests.get(url, headers=header)


response = get('/api/v5/account/balance')
print(response)