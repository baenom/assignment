class Member:
    def __init__(self, user_id, password, name):
        self.__id = user_id
        self.__password = password
        self.__name = name

    def get_id(self): return self.__id
    def get_password(self): return self.__password
    def get_name(self): return self.__name
    def get_role(self): return self.__role
    
    def set_password(self, password): self.__password = password
    def set_name(self, name): self.__name = name

    def __str__(self):
        return f'ID: {self.__id}\t이름: {self.__name}\t역할: {self.__role}'