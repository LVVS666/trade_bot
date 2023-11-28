import asyncio
import os

from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv

import data_coin
from data_market import  OKX, Bitget, CoinsBit, CoinBase, MEXC, Kucoin

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
CHAT_ID = -1002146934058


async def send_to_channel():
    while True:
        for coin in data_coin.coins:
            bank = 100 - coin.network_commission
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
                    result = f'Спред составляет {value - bank} USDT на монету {coin.name} с биржей {key}'
                    await bot.send_message(chat_id=CHAT_ID, text=result)

if __name__ == '__main__':
    executor.start(dp, send_to_channel())




