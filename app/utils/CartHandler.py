class CartHandler:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CartHandler, cls).__new__(cls)
            cls.items_in_cart = []
        return cls._instance
    
    def __init__(self):
        pass

    def add_item_to_cart(self, cart_item):
        self.items_in_cart.append(cart_item)

    def get_items_from_cart(self):
        return self.items_in_cart