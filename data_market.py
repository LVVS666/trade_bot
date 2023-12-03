import os
import requests
import get_date


from models import Market
from okx.MarketData import MarketAPI
from dotenv import load_dotenv
from coinbase.wallet.client import Client

load_dotenv()


class KucoinModel(Market):
    def get_price_coin(self, coin):
        '''Получение цены монеты на Kucoin'''
        response = requests.get(
            f'https://api.kucoin.com/api/v1/market/orderbook/level1?symbol={coin.name}-{coin.currency}')
        return float(response.json()['data']['price'])


class OKXModel(Market):
    '''Модель класса OKX'''

    def get_price_coin(self, coin):
        '''Получение цены монеты на okx '''

        api = MarketAPI(flag='1', domain='https://www.okx.cab', debug=False)
        price_coin_okx = api.get_ticker(f'{coin.name}-{coin.currency}')['data'][0]['last']
        return float(price_coin_okx)

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
        return float(price_coin_mexc)


OKX = OKXModel(
                'OKX',
                api_key=os.getenv('API_KEY_OKX'),
                secret_key=os.getenv('SECRET_KEY_OKX'),
                passphrase=os.getenv('PASSPHRASE_OKX')
                )
MEXC = MEXCModel(
                'MEXC',
                api_key=os.getenv('API_KEY_MEXC'),
                secret_key=os.getenv('SECRET_KEY_MEXC')
                )


Kucoin = KucoinModel('Kucoin',
                     api_key=os.getenv('API_KEY_KUCOIN'),
                     secret_key=os.getenv('SECRET_KEY_KUCOIN')
                     )
