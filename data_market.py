import os

from models import Market
from okx.MarketData import MarketAPI
from dotenv import load_dotenv


load_dotenv()


class OKX_Models(Market):
    '''Модель класса OKX'''
    def get_price_coin_in_okx(self, coin):
        '''Получение цены монеты на okx '''
        api = MarketAPI(flag='1', domain='https://www.okx.cab', debug=False)
        price_coin_okx = api.get_ticker(f'{coin.name}-{coin.currency}')['data'][0]['last']
        return price_coin_okx


OKX = OKX_Models(
                'OKX',
                2,
                api_key=os.getenv('API_KEY_OKX'),
                secret_key=os.getenv('SECRET_KEY_OKX'),
                passphrase=os.getenv('PASSPHRASE_OKX')
                )
