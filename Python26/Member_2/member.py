
#데이터 모델정의
class Member:
    def __init__(self,id,password,name):
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
    def set_password(self,password):
        self.__password = password
    def __str__(self):
        return f'{self.__id}\t{self.__name}\t{self.__password}'


# 회원관리 로직
class MemberService:
    def __init__(self,memberDAO):
        self.__DAO = memberDAO
    def join(self,member):
        if self.__DAO.is_exist(member.get_id()):
            return False
        self.__DAO.insert_member(member)
        return True
    def login(self,id,password):
        member = self.__DAO.get_member_info(id)
        if member:
            if password == member.get_password():
                return id
        return None
    def list_member(self):
        member_list = self.__DAO.get_all_members()
        return member_list
    pass

class MemberDAO:
    def __init__(self):
        self.__memberDB = {}

    def insert_member(self,member):
        self.__memberDB[member.get_id()] = member

    def is_exist(self,id):
        if id in self.__memberDB.keys() : return True
        return False

    def get_member_info(self,id):
        if self.is_exist(id):
            return self.__memberDB[id]
        else:
            return None
    def get_all_member(self):
        if self.__memberDB:
            return list(self.__memberDB.values())
    pass