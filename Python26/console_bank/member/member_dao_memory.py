import jodlib
class MemberDAO:

    MEMBER_DB_FILE = './db/memberDB.pkl'
    def __init__(self):
        self.__memberDB = self.__load_memberDB(MemberDAO.MEMBER_DB_FILE)

    def __load_memberDB(self):
        try:
            self.__memberDB = jodlib.load(MemberDAO.MEMBER_DB_FILE)
        except FileNotFoundError:
            self.__memberDB = {}
        
    def save_memberDB(self):
        if self.__memberDB:
            jodlib.dump(self.__memberDB,MemberDAO.MEMBER_DB_FILE)

    def update_memberDB(self):
        self.save_memberDB()
        self.__load_memberDB()
    def insert_member(self, member):
        if self.is_exist(member.get_id()):
            return False
        self.__memberDB[member.get_id()] = member
        self.save_memberDB()
        return True

    def is_exist(self, id):
        if id in self.__memberDB.keys() : return True
        return False

    def get_member_info(self, id):
        if self.is_exist(id):
            return self.__memberDB[id]
        else:
            return None

    def get_all_members(self):
        if self.__memberDB:
            return list(self.__memberDB.values())
        return []
    
    def update_password(self, id, new_password):
        member = self.get_member_info(id)
        if member:
            member.set_password(new_password)
            self.save_memberDB()
            return True
        return False

    def update_member_info(self, id, new_name):
        member = self.get_member_info(id)
        if member:
            member.set_name(new_name)
            self.save_memberDB()
            return True
        return False

    def delete_member(self, id):
        if self.is_exist(id):
            del self.__memberDB[id]
            self.save_memberDB()
            return True
        return False


