class Network:
    def __init__(self, commission):
        self.commission = commission



class Coin:
    def __init__(self, name, network, currency):
        self.name = name
        self.network = network
        self.currency = currency



class Market:
    def __init__(self, address, commission, api_key=None, secret_key=None, passphrase=None):
        self.address = address
        self.commission = commission
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase
