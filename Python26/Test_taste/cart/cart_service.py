class CartService:
    def __init__(self,cartDAO):
        self.__DAO = cartDAO
    def insert_cart(self,id):
        return self.__DAO.insert_cart(id)
    def clening_cart(self):
        self.__DAO.clening_cart()
    def get_cart(self):
        return self.__DAO.get_cart()