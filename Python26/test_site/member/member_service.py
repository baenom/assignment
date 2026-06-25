from member import Member

class MemberService:
    def __init__(self, member_dao):
        self.ADMIN_ID = 'admin'
        self.ADMIN_PASSWORD = '1234'
        self.current_user = None
        self.__DAO = member_dao
        if not self.__DAO.is_exist(self.ADMIN_ID):
            self.__DAO.insert_member(Member(self.ADMIN_ID, self.ADMIN_PASSWORD, "시스템관리자"))

    def join(self, member):
        if self.__DAO.is_exist(member.get_id()):
            return False
        return self.__DAO.insert_member(member)

    def login(self, user_id, password):
        member = self.__DAO.get_member_info(user_id)
        if member and member.get_password() == password:
            self.current_user = member
            return member
        return None

    def logout(self):
        self.current_user = None

    def list_members(self):
        return self.__DAO.get_all_members()

    def delete_member(self, user_id):
        return self.__DAO.delete_member(user_id)