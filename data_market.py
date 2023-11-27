import time
from datetime import datetime
import os
import requests
import get_date

import data_coin
from models import Market
from okx.MarketData import MarketAPI
from dotenv import load_dotenv
from coinbase.wallet.client import Client
from okx.Account import AccountAPI


load_dotenv()


class BitgetModel(Market):

    def get_price_coin(self, coin):
        '''Получение цены монеты на Bitget'''
        response = requests.get(f'https://api.bitget.com/api/v2/spot/market/tickers?symbol={coin.name}{coin.currency}')
        return response.json()['data'][0]['lastPr']


class KucoinModel(Market):
    def get_price_coin(self, coin):
        '''Получение цены монеты на Kucoin'''
        response = requests.get(
            f'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={coin.name}-{coin.currency}')
        return response.json()['data']['price']


class OKXModel(Market):
    '''Модель класса OKX'''

    def get_price_coin(self, coin):
        '''Получение цены монеты на okx '''

        api = MarketAPI(flag='1', domain='https://www.okx.cab', debug=False)
        price_coin_okx = api.get_ticker(f'{coin.name}-{coin.currency}')['data'][0]['last']
        return price_coin_okx

    def get_balance(self):
        '''Получение баланса аккаунта'''

        url_balance = '/api/v5/account/balance'
        root_url = 'https://www.okx.cab'
        return get_date.get(
            endpoint=url_balance,
            root_url=root_url,
            api_key=self.api_key,
            secret_key=self.secret_key,
            passphrase=self.passphrase
        )


class MEXCModel(Market):
    '''Модель класса MEXC'''

    def get_price_coin(self, coin):
        '''Получение цены монеты на mexc'''

        url_api_mexc = "https://api.mexc.com/api/v3/ticker/price"
        params = {
            'symbol': f'{coin.name}{coin.currency}',
            'interval': '1m',
            'limit': 10
        }
        price_coin_mexc = requests.get(url_api_mexc, params=params).json()['price']
        return price_coin_mexc


class CoinBaseModel(Market):
    '''Модель класса CoinBase'''

    def get_price_coin(self, coin):
        '''Получение цены монеты на coinbase'''

        client = Client(api_key=self.api_key, api_secret=self.secret_key)
        price_coin_coin_base = client.get_spot_price(currency_pair=f'{coin.name}-{coin.currency}')
        return price_coin_coin_base['amount']


class CoinsBitModel(Market):

    def get_price_coin(self, coin):
        '''Получение цены монеты на coinsbit'''
        url_api_coinsbit = requests.get(' https://coinsbit.io/api/v1/public/tickers')
        price_coin_coinsbit = url_api_coinsbit.json()['result'][f'{coin.name}_{coin.currency}']['ticker']['last']
        return price_coin_coinsbit


OKX = OKXModel(
                'OKX',
                2,
                api_key=os.getenv('API_KEY_OKX'),
                secret_key=os.getenv('SECRET_KEY_OKX'),
                passphrase=os.getenv('PASSPHRASE_OKX')
                )
MEXC = MEXCModel(
                'MEXC',
                2,
                api_key=os.getenv('API_KEY_MEXC'),
                secret_key=os.getenv('SECRET_KEY_MEXC')
                )

CoinBase = CoinBaseModel(
                        'CoinBase',
                        2,
                        api_key=os.getenv('API_KEY_COINBASE'),
                        secret_key=os.getenv('SECRET_KEY_COINBASE')
)
CoinsBit = CoinsBitModel('CoinsBit',
                         2,
                         api_key=os.getenv('API_KEY_COINSBIT'),
                         secret_key=os.getenv('SECRET_KEY_COINSBIT')
                         )
Kucoin = KucoinModel('Kucoin',
                     2,
                     api_key=os.getenv('API_KEY_KUCOIN'),
                     secret_key=os.getenv('SECRET_KEY_KUCOIN')
                     )
Bitget = BitgetModel('Bitget',
                     2,
                     api_key=os.getenv('API_KEY_BITGET'),
                     secret_key=os.getenv('SECRET_KEY_BITGET'),
                     passphrase=os.getenv('PASSPHRASE_BITGET')
                     )

list_markets = [OKX, Bitget, CoinsBit, CoinBase, MEXC, Kucoin]

while True:
    for coin in data_coin.coins:
        bank = 1000 - coin.network_commission
        last_price_okx = bank / float(OKX.get_price_coin(coin))
        last_prices_market = {
        'Bitget' : last_price_okx * float(Bitget.get_price_coin(coin)),
        'Coinsbit' : last_price_okx * float(CoinsBit.get_price_coin(coin)),
        'Coinsbase' : last_price_okx * float(CoinBase.get_price_coin(coin)),
        'Mexc' : last_price_okx * float(MEXC.get_price_coin(coin)),
        'Kucoin' : last_price_okx * float(Kucoin.get_price_coin(coin))
        }
        for key, value in last_prices_market.items():
            if (value - bank) > 0.1:
                print(f'Спред составляет {value - bank} USDT на монету {coin.name} с биржей {key}')
