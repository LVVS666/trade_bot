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


class BitgetModel(Market):

    def get_price_coin(self, coin):
        '''Получение цены монеты на Bitget'''
        response = requests.get(f'https://api.bitget.com/api/v2/spot/market/tickers?symbol={coin.name}{coin.currency}')
        return response.json()['data'][0]['lastPr']


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
CoinBase = CoinBaseModel(
                        'CoinBase',
                        api_key=os.getenv('API_KEY_COINBASE'),
                        secret_key=os.getenv('SECRET_KEY_COINBASE')
)
CoinsBit = CoinsBitModel('CoinsBit',
                         api_key=os.getenv('API_KEY_COINSBIT'),
                         secret_key=os.getenv('SECRET_KEY_COINSBIT')
                         )
Bitget = BitgetModel('Bitget',
                     api_key=os.getenv('API_KEY_BITGET'),
                     secret_key=os.getenv('SECRET_KEY_BITGET'),
                     passphrase=os.getenv('PASSPHRASE_BITGET')
                     )