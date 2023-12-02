import data_coin
from data_market import OKX, Bitget, CoinsBit, MEXC, CoinBase, Kucoin


def search_spread_to_market(bot, CHAT_ID):
    while True:
        for coin in data_coin.coins:
            bank = 100
            last_prices_market = {
            'OKX': bank * float(OKX.get_price_coin(coin)),
            'Bitget' : bank * float(Bitget.get_price_coin(coin)),
            'Coinsbit' : bank * float(CoinsBit.get_price_coin(coin)),
            'Coinsbase' : bank * float(CoinBase.get_price_coin(coin)),
            'Mexc' : bank * float(MEXC.get_price_coin(coin)),
            'Kucoin' : bank * float(Kucoin.get_price_coin(coin))
            }
            max_price = max(last_prices_market.items(), key=lambda x: x[1])
            min_price = min(last_prices_market.items(), key=lambda x: x[1])
            spread = float(max_price[1]) - (float(min_price[1]) - coin.network_commission)
            if spread > 1:
                text_message = f'Покупка {coin.name} на бирже {min_price[0]} и продажа на бирже {max_price[0]},принесет {spread} USDT'
                await bot.send_message(chat_id=CHAT_ID, text=text_message)
