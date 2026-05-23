
class Member:
    def __init__(self, id, password, name):
        self.__member_number = 0
        self.__id = id
        self.__password = password
        self.__name = name

    def get_member_number(self):
        return self.__member_number
    
    def get_id(self):
        return self.__id
    
    def get_password(self):
        return self.__password
    
    def get_name(self):
        return self.__name
    
    def set_password(self, password):
        self.__password = password

    def set_name(self, name):
        self.__name = name

    def __str__(self):
        return f'{self.__id}\t{self.__name}\t{self.__password}'


class MemberDAO:
    def __init__(self):
        self.__memberDB = {}

    def insert_member(self, member):
        self.__memberDB[member.get_id()] = member

    def is_exist(self, id):
        return id in self.__memberDB

    def get_member_info(self, id):
        if self.is_exist(id):
            return self.__memberDB[id]
        return None

    def get_all_members(self):
        if self.__memberDB:
            return list(self.__memberDB.values())
        return []

    def delete_member(self, id):
        if self.is_exist(id):
            del self.__memberDB[id]
            return True
        return False


class MemberService:
    def __init__(self, memberDAO):
        self.__DAO = memberDAO

    def join(self, member):
        if self.__DAO.is_exist(member.get_id()):
            return False
        self.__DAO.insert_member(member)
        return True

    def login(self, id, password):
        member = self.__DAO.get_member_info(id)
        if member:
            if password == member.get_password():
                return id
        return None

    def list_member(self):
        return self.__DAO.get_all_members()

    def find_member(self, id):
        return self.__DAO.get_member_info(id)

    def update(self, id, new_password, new_name):
        member = self.__DAO.get_member_info(id)
        if member:
            member.set_password(new_password)
            member.set_name(new_name)
            return True
        return False

    def delete(self, id):
        return self.__DAO.delete_member(id)
        