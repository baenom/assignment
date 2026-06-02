from member.member_dao import MemberDAO
from member.member import Member

class MemberService:
    def __init__(self, memberDAO):
        self.ADMIN_ID = 'admin'
        self.ADMIN_PASSWORD = '1234'
        self.current_user = None
        self.__DAO = memberDAO
        self.join(Member(self.ADMIN_ID, self.ADMIN_PASSWORD, self.ADMIN_ID))

    def join(self, member):
        # member.set_id(member.get_id().lower())
        if not self.is_valid_id(member.get_id()):
            return False
        if self.__DAO.is_exist(member.get_id()):
            return False
        return self.__DAO.insert_member(member)
    
    def is_valid_id(self, id):
        if id.isalpha(): return True

    def login(self, id, password):
        member = self.__DAO.get_member_info(id)
        if member:
            if password == member.get_password():
                return id
        return None

    def list_member(self):
        return self.__DAO.get_all_members()

    def view_member_info(self, id):
        return self.__DAO.get_member_info(id)

    def update_member_info(self, id, member):
        return self.__DAO.update_member_info(id, member)

    def delete(self, id):
        if self.current_user == id or self.current_user == self.ADMIN_ID:
            return self.__DAO.delete_member(id)
    
    def update_password(self, id, org_password, new_password):
        if self.current_user != id: return False
        member = self.__DAO.get_member_info(id)
        if member:
            if member.get_password() == org_password:
                return self.__DAO.update_password(id, new_password)
            else:
                print("현재 비밀번호가 일치하지 않습니다")
                return False
        print("존재하지 않는 회원입니다")
        return False
    
    def logout(self):
        self.current_user = None

    
if __name__ == '__main__':
    ms = MemberService(MemberDAO())
    ms.join(Member('Euijin','1234','BaeEuijin'))
    members = ms.list_member()
    for member in members:
        print(member)
    current_user = ms.login('Euijin','1234')
    print(current_user)
    ms.login('Euijin','1234')
    print(current_user)

