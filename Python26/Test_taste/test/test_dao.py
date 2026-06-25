import joblib

class TestDAO:
    def __init__(self):
        self.testDB_path = './db/testDB.pkl'
        self.__testDB = []
        self.__testDB = self.__load_testDB()
    def __load_testDB(self):
        try:
            return joblib.load(self.testDB_path)
        except FileNotFoundError:
            return []
    def __save_testDB(self):
        if self.__testDB:
            joblib.dump(self.__testDB,self.testDB_path)
    def update_testDB(self):
        self.__save_testDB()
        self.__load_testDB()
    def insert_test(self,test_list):
        self.__testDB.append(test_list)
        self.update_testDB()
        return True
    def get_all_test_name(self):
        show_list = []
        if self.__testDB is None:
            return []
        for i in self.__testDB:
            if i and i[0].get_is_hide() == True:
                show_list.append([i[0].get_id(),i[0].get_test()])
        return show_list
    def get_test_name(self,id):
        if self.__testDB is None:
            return []
        for i in self.__testDB:
            if i[0].get_id() == id:
                return i[0].get_test()
    def get_all_test(self):
        if self.__testDB is None:
            return []
        return self.__testDB
    def get_test_test(self,id):
        test_list = []
        for i in self.__testDB:
            if i[0].get_id() == id:
                for j in i:
                    test_list.append(j.get_test())
                return test_list
    def get_test_answer(self,id):
        test_list = []
        for i in self.__testDB:
            if i[0].get_id() == id:
                for j in i:
                    test_list.append(j.get_answer())
                return test_list
    def get_last_test_index(self):
        if not self.__testDB or self.__testDB == []:
            return 0
        return self.__testDB[-1][-1].get_id()
    def hiden_test(self,id):
        for i in self.__testDB:
            if i[0].get_id() == id:
                if i[0].get_is_hide():
                    i[0].set_is_hide(False)
                    return False
                else: 
                    i[0].set_is_hide(True)
                    return True