class Test:
    def __init__(self,id,test,answer,is_hide,price):
        self.__id = id
        self.__answer = answer
        self.__test = test
        self.__is_hide = is_hide
        self.__price = price

    def get_id(self):
        return self.__id
    def get_price(self):
        return self.__price
    def get_answer(self):
        return self.__answer
    def get_test(self):
        return self.__test
    def get_is_hide(self):
        return self.__is_hide
    def set_is_hide(self,is_hide):
        self.__is_hide = is_hide
    def set_test(self,test):
        self.__test = test
    def set_id(self,id):
        self.__id = id
    def set_answer(self,answer):
        self.__answer = answer