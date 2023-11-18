import os

from okx.MarketData import MarketAPI
from pymexc import spot
from dotenv import load_dotenv
from date import OKB, XRP

load_dotenv()

API_KEY_MEXC = os.getenv('API_KEY_MEXC')
SECRET_KEY_MEXC = os.getenv('SECRET_KEY_MEXC')


def get_price_coin_in_mexc(coin):
    '''Получение цены монеты на mexc'''
    spot_client = spot.HTTP(api_key=API_KEY_MEXC, api_secret=SECRET_KEY_MEXC)
    print(spot_client.ticker_price(symbol=f'{coin.name}{coin.currency}'))



def get_price_coin_in_okx(coin):
    '''Получение цены монеты на okx '''
    api = MarketAPI(flag='1', domain='https://www.okx.cab', debug=False)
    price_coin = api.get_ticker(f'{coin.name}-{coin.currency}')['data'][0]['last']
    return price_coin


def get_comparison_price(coin, network, market):
    '''Сравнение цен на разных биржах'''
    pass

