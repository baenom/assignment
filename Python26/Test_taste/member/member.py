class Member:
    def __init__(self,id,name,password,my_test_list):
        self.__id = id
        self.__name = name
        self.__password = password
        self.__my_test_list = my_test_list

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_password(self):
        return self.__password
    def get_my_test_list(self):
        return self.__my_test_list
    def set_password(self,password):
        self.__password = password
    def set_my_test_list(self,my_test_list):
        self.__my_test_list = my_test_list
    def set_id(self,id):
        self.__id = id
    def set_name(self,name):
        self.__name = name