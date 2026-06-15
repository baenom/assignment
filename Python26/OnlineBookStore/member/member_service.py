from member.member_dao_memory import MemberDAO
from member.member import Member

class MemberService:
    def __init__(self, memberDAO):
        self.ADMIN_ID = 'admin'
        self.ADMIN_PASSWORD = '1234'
        self.current_user = None  
        self.__DAO = memberDAO

    def join(self, member):
        if not self.is_valid_id(member.get_id()) or self.__DAO.is_exist(member.get_id()):
            return False
        return self.__DAO.insert_member(member)
    
    def is_valid_id(self, id):
        return id.isalpha()

    def login(self, id, password):
        member = self.__DAO.get_member_info(id)
        if member and password == member.get_password():
            self.current_user = member
            return id
        return None

    def logout(self):
        self.current_user = None

    def list_member(self):
        return self.__DAO.get_all_members()

    def update_address(self, id, new_address):
        member = self.__DAO.get_member_info(id)
        if member:
            member.set_address(new_address)
            self.save_member_data()
            return True
        return False

    def delete_account(self, id):
        return self.__DAO.delete_member(id)

    def save_member_data(self):
        self.__DAO.save_memberDB()

    def update_password(self, member, org_password, new_password):
        if member.get_password() == org_password:
            member._Member__password = new_password
            self.save_member_data()
            print("\n비밀번호가 성공적으로 변경되었습니다.")
            return True
        else:
            print("\n기존 비밀번호가 일치하지 않습니다.")
            return False