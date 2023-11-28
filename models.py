class Coin:
    def __init__(self, name, network_commission, currency):
        self.name = name
        self.network_commission = network_commission
        self.currency = currency


class Market:
    def __init__(self, name, api_key=None, secret_key=None, passphrase=None):
        self.name = name
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase
