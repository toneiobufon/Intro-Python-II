class User:
    def __init__(self, money):
        self.money = money
        self.cart = []
    def __str__(self):
        return f"Money: ${self.money}, Cart: {self.cart}"