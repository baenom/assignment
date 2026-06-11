import joblib
class MemberDAO:

    MEMBER_DB_FILE = './db/memberDB.pkl'
    def __init__(self):
        self.__memberDB = self.__load_memberDB(MemberDAO.MEMBER_DB_FILE)

    def __load_memberDB(self):
        try:
            self.__memberDB = joblib.load(MemberDAO.MEMBER_DB_FILE)
        except FileNotFoundError:
            self.__memberDB = {}
        
    def save_memberDB(self):
        if self.__memberDB:
            joblib.dump(self.__memberDB,MemberDAO.MEMBER_DB_FILE)

    def update_memberDB(self):
        self.save_memberDB()
        self.__load_memberDB()

    def insert_member(self, member):
        if self.is_exist(member.get_id()):
            return False
        self.__member_list.append(member)
        return True

    def is_exist(self, id):
        for member in self.__member_list:
            if member.get_id() == id:
                return True
        return False

    def get_member_info(self, id):
        for member in self.__member_list:
            if member.get_id() == id:
                return member
        return None

    def get_all_members(self):
        return self.__member_list

    def delete_member(self, id):
        for idx, member in enumerate(self.__member_list):
            if member.get_id() == id:
                del self.__member_list[idx]
                return True
        return False

    def update_member_info(self, id, new_name):
        member = self.get_member_info(id)
        if member:
            member.set_name(new_name)
            self.save_memberDB()
            return True
        return False


