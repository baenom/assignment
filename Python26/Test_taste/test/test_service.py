
class TestService:
    def __init__(self,testDAO):
        self.__DAO = testDAO
    def get_test_test(self,id):
        return self.__DAO.get_test_test(id)
    def get_test_answer(self,id):
        return self.__DAO.get_test_answer(id)
    def get_all_test(self):
        return self.__DAO.get_all_test()
    def get_all_test_name(self):
        return self.__DAO.get_all_test_name()
    def insert_test(self,test_list):
        return self.__DAO.insert_test(test_list)
    def get_last_test_index(self):
        return self.__DAO.get_last_test_index()
    def get_test_name(self,id):
        return self.__DAO.get_test_name(id)
    def hiden_test(self, id):
        return self.__DAO.hiden_test(id)
