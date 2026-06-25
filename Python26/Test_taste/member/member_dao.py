import joblib
class MemberDAO:
    def __init__(self):
        self.memberDB_path = './db/memberDB.pkl'
        self.__memberDB = []
        self.__memberDB = self.__load_memberDB()
    def __load_memberDB(self):
        try:
            return joblib.load(self.memberDB_path)
        except FileNotFoundError:
            return []
    def __save_memberDB(self):
        if self.__memberDB:
            joblib.dump(self.__memberDB,self.memberDB_path)
    def update_memberDB(self):
        self.__save_memberDB()
        self.__load_memberDB()
    def insert_member(self,member):
        if self.member_confirm(member.get_id()):
            self.__memberDB.append(member)
            self.update_memberDB()
            return True
        return False
    def delete_member(self,id):
        if not self.__memberDB:
            return False
        index = 0
        for i in self.__memberDB:
            index += 1
            if i.get_id() == id:
                del self.__memberDB[index-1]
                self.update_memberDB()
                return True
        return False
    
    def delete_member_test(self,id,test_id_list):
        if not self.__memberDB:
            return False
        index = 0
        for i in self.__memberDB:
            index += 1
            if i.get_id() == id:
                self.__memberDB[index-1].set_my_test_list(test_id_list)
                self.update_memberDB()
                return True
        return False
    def update_member_info(self,member):
        if not self.__memberDB:
            return False
        index = 0
        for i in self.__memberDB:
            index += 1
            if i.get_id() == member.get_id():
                self.__memberDB[index-1] = member
                self.update_memberDB()
                return True
        return False
    def get_all_members(self):
        if self.__memberDB is None:
            return []
        return self.__memberDB
    def get_members_info(self,id):
        if not self.__memberDB:
            return None
        for member in self.__memberDB:
            if member.get_id() == id:
                return member
        return None
    def get_members_test(self,id):
        if not self.__memberDB:
            return None
        for member in self.__memberDB:
            if member.get_id() == id:
                return member.get_my_test_list()
        return None
    def member_confirm(self,id):
        for i in self.__memberDB:
            if i.get_id() == id:
                return False
        return True
    def insert_test(self,member):
        if self.member_confirm(member.get_id()):
            self.__memberDB.append(member)
            self.update_memberDB()
            return True
        return False