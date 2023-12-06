import os
import logging
import subprocess

from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv

from trade_actions import search_spread_to_market

load_dotenv()

logging.basicConfig(
                    level=logging.INFO,
                    filename='logging_bot',
                    filemode='w'
                    )

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
CHAT_ID = -1002146934058


async def send_to_channel():
    while True:
        try:
            await search_spread_to_market(bot, CHAT_ID)
            logging.info('Бот запущен.')
        except ConnectionError:
            logging.error('Произошла ошибка соединения с сервером')
            # Перезапуск бота.
            restart_bot = subprocess.Popen(['python', 'bot.py'])
            restart_bot.wait()




if __name__ == '__main__':
    executor.start(dp, send_to_channel())
