from MVP import Network, Coin, Market

#Сети
Optimist = Network(0.1)
ArpitrumOne = Network(0.1)

#Биржи
OKX = Market('здесь адрес кошелька', 2)

#Монеты
BTC = Coin('BTC', Optimist, 'USDT')
OKB = Coin('OKB', Optimist, 'USDT')
XRP = Coin('XRP', Optimist, 'USDT')



