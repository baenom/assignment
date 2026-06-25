class MemberService:
    def __init__(self,memberDAO):
        self.ADMIN_ID = 'admin'
        self.ADMIN_PASSWORD = '1234'
        self.current_user = None  
        self.__DAO = memberDAO
    def join(self, member):
        if self.format(member.get_id()):
            return self.__DAO.insert_member(member)
    def format(self,id):
        return id.isalpha()
    def login(self, id, password):
        member = self.__DAO.get_members_info(id)
        if member and password == member.get_password():
            self.current_user = member
            return id
        return None
    def logout(self):
        self.current_user = None
    def list_member(self):
        return self.__DAO.get_all_members()
    def delete_member(self, id):
        return self.__DAO.delete_member(id)
    def update_password(self, member,org_password,new_password):
        if member.get_password() == org_password:
            member.set_password(new_password)
            return self.__DAO.update_member_info(member)
        else:
            print("기존 비밀번호가 일치하지 않습니다")
            return False
    def update_info(self,member,id,name):
        member.set_id(id)
        member.set_name(name)
        return self.__DAO.update_member_info(member)
    def update_test_id_info(self,member,test_id):
        test_list = []
        test_list = member.get_my_test_list()
        test_list.append(test_id)
        member.set_my_test_list(test_list)
        if self.__DAO.update_member_info(member):
            return True
        return False
    def get_members_info(self,id):
        return self.__DAO.get_members_info(id)
    def get_members_test(self,id):
        return self.__DAO.get_members_test(id)