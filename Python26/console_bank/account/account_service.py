from account.account import Account
from account.account_dao import AccountDAO

class AccountService:
    account_no_seq = 111111
    def __init__(self,account_dao):
        self.__dao = account_dao

    def create_account(self,account):
        # if self.__dao.is_exist(account.get_account_no()):

        account.set_account_no(str(AccountService.account_no_seq))
        AccountService.account_no_seq += 1

        return self.__dao.insert_account(account)
    def get_all_account(self):
        return self.__dao.select_all_account()
    def get_member_account(self,id):
        return self.__dao.select_account_by_member_id(id)
    def diposit(self,account_no,amount):
        account = self.__dao.select_account_by_account_no(account_no)
        if account:
            new_balance = account.get_balance() + amount
            account.set_balance(new_balance)
            return self.__dao.update_account(account_no,account)
        return False
    def withdraw(self,id,account_no,amount,password):
        account = self.__dao.select_account_by_account_no(account_no)
        if account:
            if account.get_owner()!= id or account.get_password()!= password:
                raise KeyError
            new_balance = account.get_balance() - amount
            if new_balance < 0:
                raise ValueError
            
            account.set_balance(new_balance)
            return self.__dao.update_account(account_no,account)
        return False
    def delete_account(self,id,account_no,password):
        account = self.__dao.select_account_by_account_no(account_no)
        if not account:
            return False
        if account.get_owner() != id or account.get_password() != password:
            raise KeyError
        return self.__dao.delete_account(account_no)
    def admin_delete_account(self,account_no):
        account = self.__dao.select_account_by_account_no(account_no)
        if not account:
            return False
        return self.__dao.delete_account(account_no)
    def get_account_balance(self,account_no):
        account = self.__dao.select_account_by_account_no(account_no)
        if account:
            return account.get_balance()
        return-1



if __name__ == "__main__":
    aservice = AccountService(AccountDAO())
    aservice.create_account(Account(0,'baeeuijin',10000,'1234'))
    for account in aservice.get_all_account():
        print(account)

    for account in aservice.get_member_account('baeeuijin'):
        print(account)
    aservice.diposit('111111',2000)
    print()
    for account in aservice.get_member_account('baeeuijin'):
        print(account)
    if aservice.diposit('111111',2000):
        for account in aservice.get_all_account():
            print(account)
    else:
        print('no account')
    try:
        aservice.withdraw('baeeuijin','111111',50000,'1234')
    except Exception as e:
        print(type(e))
    else:
        for account in aservice.get_all_account():
            print(account)
    try:
        if not aservice.delete_account('baeeuijin', '111111', '1234'):
            print('no account')
    except Exception as e:
        print(type(e))
    else:
        for account in aservice.get_all_account():
            print(account)
            

