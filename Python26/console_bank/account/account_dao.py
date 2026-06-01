from account import Account

class AccountDAO:
    def __init__(self):
        self.__accountDB = {}
    def insert_account(self,account):
        account_no = account.get_account_no()
        if account_no not in self.__accountDB:
            self.__accountDB[account.get_account_no()] = account
            return True
        return False
    def select_account_by_account_no(self,account_no):
        if account_no in self.__accountDB:
            return self.__accountDB[account_no]
    def select_account_by_member_id(self,member_id):
        account_list = []
        for account in self.__accountDB.values():
            if account.get_owner() == member_id:
                account_list.append(account)
        if len(account_list):return account_list
        return None
    def select_all_account(self,):
        account_list = list(self.__accountDB.values())
        if len(account_list):
            return account_list
        return []
    def update_account(self,account_no,account):
        account_no = account.get_account_no()
        if account_no not in self.__accountDB:
            self.__accountDB[account_no] = account
            return True
        return False
    def delete_account(self,account_no):
        if account_no in self.__accountDB:
            self.__accountDB.pop(account_no)
            return True
        return False
if __name__ == '__main__':
    dao = AccountDAO()
    ac_list = dao.select_all_account()
    print(ac_list)
    ac = Account('111111','baeeuijin',10000,'1234')
    dao.insert_account(ac)
    for account in dao.select_all_account():
        print(account)
    for account in dao.select_account_by_member_id('baeeuijin'):
        print(account)