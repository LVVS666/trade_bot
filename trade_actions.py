from time import sleep

import data_coin
from data_market import OKX,  MEXC, Kucoin

def get_spread(coin):
    print(coin.name)
    last_prices_market = {
        'OKX':  OKX.get_price_coin(coin),
        'Mexc':  MEXC.get_price_coin(coin),
        'Kucoin': Kucoin.get_price_coin(coin)
    }
    max_price = max(last_prices_market.items(), key=lambda x: x[1])
    min_price = min(last_prices_market.items(), key=lambda x: x[1])
    spread = max_price[1] - min_price[1]
    spread_date = {'spread': spread, 'max_price': max_price, 'min_price': min_price}
    return spread_date

async def search_spread_to_market(bot, CHAT_ID):
    while True:
        for coin in data_coin.coins:
            spread_date = get_spread(coin)
            while spread_date['spread'] > 1:
                text_message = f'Покупка {coin.name} на бирже ' \
                               f'{spread_date["min_price"][0]} ' \
                               f'и продажа на бирже {spread_date["max_price"][0]},' \
                               f'принесет {spread_date["spread"]} USDT'
                await bot.send_message(chat_id=CHAT_ID, text=text_message)
                sleep(5)
                spread_date = get_spread(coin)
