import requests

import data_coin


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
