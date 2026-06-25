class CartDAO:
    def __init__(self):
        self.cart_list = []
    def insert_cart(self,id):
        self.cart_list.append(id)
        return True
    def clening_cart(self):
        self.cart_list.clear()
    def get_cart(self):
        return self.cart_list