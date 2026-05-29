from member_dao import MemberDAO

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
        

if __name__ == '__main__':
    dao = MemberDAO()
    member = Member('의진','1234','배의진')
    dao.insert_member(member)
    print(dao.is_exist('의진'))

    members = dao.get_all_members()
    for member in members:
        print(member)
    member = dao.get_member_info('의진')
    if member:
        member.set_password('1111')
        dao.update_member_info('의진',member)

    members = dao.get_all_members()
    for member in members:
        print(member)