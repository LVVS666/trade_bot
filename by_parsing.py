import requests
import time

'''Тестовые данные для парсинга и сравнения для двух бирж'''

url_binance = "https://api.binance.com/api/v3/ticker/price"
url_bybit = "https://api.bybit.com/v2/public/tickers"
BTC_BINANCE = "BTCUSDT"
BTC_BYBIT = "BTCUSD"

params_binance = {
    "symbol": BTC_BINANCE
}
params_bybit = {
    "symbol": BTC_BYBIT
}

while True:
    response_binance = requests.get(url_binance, params=params_binance)
    response_bybit = requests.get(url_bybit, params=params_bybit)
    if response_binance.status_code == 200:
        data = response_binance.json()
        last_price_binance = round(float(data['price']), 5)
        print(f"Последняя цена {BTC_BINANCE} на бирже Binance: {last_price_binance}")
    else:
        print("Не удалось получить данные. Проверьте параметры запроса и интернет-соединение.")

    if response_bybit.status_code == 200:
        data = response_bybit.json()
        last_price_bybit = data['result'][0]['last_price']
        print(f"Последняя цена {BTC_BYBIT} на бирже Bybit: {last_price_bybit}")
    else:
         print("Не удалось получить данные. Проверьте параметры запроса и интернет-соединение.")
    time.sleep(1)
    if float(last_price_bybit) > float(last_price_binance):
        print(f'Цена биткоина на Bybit больше чем на Binance на {float(last_price_bybit) - float(last_price_binance)}$')
    else:
        print(f'Цена биткоина на Binance больше чем на Bybit на {float(last_price_binance) - float(last_price_bybit)}$')
    time.sleep(2)
