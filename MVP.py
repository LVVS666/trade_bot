class Network:
    def __init__(self, commission):
        self.commission = commission



class Coin:
    def __init__(self, name, network, currency):
        self.name = name
        self.network = network
        self.currency = currency


    def get_price(self):
        '''Получение цены на площадке'''
        pass

    def get_last_price(self):
        '''Последня цена = цена + комиссия площадки + коммиссия сети'''
        pass


class Market:
    def __init__(self, name, address, commission, api_key):
        self.name = name
        self.address = address
        self.commission = commission
        self.api_key = api_key
