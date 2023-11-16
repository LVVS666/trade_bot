from MVP import Network, Coin, Market

#Сети
Optimist = Network(0.1)
ArpitrumOne = Network(0.1)

#Биржи
OKX = Market('здесь адрес кошелька', 2)

#Монеты
Tether = Coin('Tether', Optimist, 'USDT')



