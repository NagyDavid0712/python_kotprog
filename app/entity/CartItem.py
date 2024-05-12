

class CartItem:

    def __init__(self, product, quantity):
        self._product = product
        self._quantity = quantity
        self.price = self._product.product_price * self._quantity

    @property
    def product(self):
        return self._product
    
    @product.setter
    def product(self, n):
        self._product = n

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, n):
        self._quantity = n

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, n):
        self._price = n