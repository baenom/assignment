import joblib
import os

class MemberDAO:
    MEMBER_DB_FILE = './db/memberDB.pkl'

    def __init__(self):
        os.makedirs('./db', exist_ok=True)
        self.__memberDB = self.__load_memberDB()

    def __load_memberDB(self):
        try:
            return joblib.load(MemberDAO.MEMBER_DB_FILE)
        except FileNotFoundError:
            return {}
        
    def save_memberDB(self):
        joblib.dump(self.__memberDB, MemberDAO.MEMBER_DB_FILE)

    def insert_member(self, member):
        if self.is_exist(member.get_id()):
            return False
        self.__memberDB[member.get_id()] = member
        self.save_memberDB()
        return True

    def is_exist(self, user_id):
        return user_id in self.__memberDB

    def get_member_info(self, user_id):
        return self.__memberDB.get(user_id, None)

    def get_all_members(self):
        return list(self.__memberDB.values())

    def delete_member(self, user_id):
        if self.is_exist(user_id):
            del self.__memberDB[user_id]
            self.save_memberDB()
            return True
        return False