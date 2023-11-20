import os
import requests

from models import Market
from okx.MarketData import MarketAPI
from dotenv import load_dotenv


load_dotenv()


class OKXModel(Market):
    '''Модель класса OKX'''
    def get_price_coin_in_okx(self, coin):
        '''Получение цены монеты на okx '''
        api = MarketAPI(flag='1', domain='https://www.okx.cab', debug=False)
        price_coin_okx = api.get_ticker(f'{coin.name}-{coin.currency}')['data'][0]['last']
        return price_coin_okx


class MEXCModel(Market):
    '''Модель класса MEXC'''
    def get_price_coin_in_mexc(self, coin):
        '''Получение цены монеты на mexc'''
        url_api_mexc = "https://api.mexc.com/api/v3/ticker/price"
        params = {
            'symbol': f'{coin.name}{coin.currency}',
            'interval': '1m',
            'limit': 10
        }
        price_coin_mexc = requests.get(url_api_mexc, params=params).json()['price']
        return price_coin_mexc


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
