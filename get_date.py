from okx.MarketData import MarketAPI

from date import OKB, XRP


def get_price_coin_in_okx(coin):
    '''Получение цены монеты на okx '''
    api = MarketAPI(flag='1', domain='https://www.okx.cab', debug=False)
    price_coin = api.get_ticker(f'{coin.name}-{coin.currency}')['data'][0]['last']
    return price_coin


def get_comparison_price(coin, network, market):
    '''Сравнение цен на разных биржах'''
    pass



