class MemberDAO:
    def __init__(self):
        self.__memberDB = {}

    def insert_member(self, member):
        if self.is_exist(member.get_id()):
            return False
        self.__memberDB[member.get_id()] = member
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
    # def update_member_info(self, id, member):
    #     member = self.__DAO.get_member_info(id)
    #     if member:
    #         member.set_password(new_password)
    #         member.set_name(new_name)
    #         return True
    #     return False
    
    def update_password(self, id, new_password):
        member = self.get_member_info(id)
        if member:
            member.set_password(new_password)
            return True
        return False

    def update_member_info(self, id, new_name):
        member = self.get_member_info(id)
        if member:
            member.set_name(new_name)
            return True
        return False

    def delete_member(self, id):
        if self.is_exist(id):
            del self.__memberDB[id]
            return True
        return False


