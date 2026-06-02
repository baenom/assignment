from member.member import Member
from member.member_dao import MemberDAO
from member.member_service import MemberService
from account.account import Account
from account.account_dao import AccountDAO
from account.account_service import AccountService

class ConsoleBank:
    start_menu = ['종료','로그인','회원가입']
    banking_menu = ['로그아웃','계좌목록','입금','출금','계좌생성','계좌해지','내 정보']
    member_myinfo_menu = ['돌아가기','비밀번호 수정','회원탈퇴',]
    admin_account_menu = ['돌아가기','전체계좌목록','회원별계좌목록','회원강퇴']
    admin_menu = ['로그아웃','회원관리','계좌관리']
    admin_member_menu = ['돌아가기','회원목록','회원정보조회']

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.asv = AccountService(AccountDAO())
        
        # self.msv.join(Member('Euijin','1234','BaeEuijin'))
        # self.asv.create_account(Account(0,'Euijin',10000,'1234'))
    def main(self):
        self.show_welcome()
        while True:
            menu = self.select_menu(ConsoleBank.start_menu)
            if menu == 0: break
            elif menu == 1:
                self.menu_login()
            elif menu == 2:
                self.menu_join()
        self.say_goodbye
    def show_welcome(self):
        pass
    def say_goodbye(self):
        pass
    def select_menu(self,menu_list):
        print('------------------------')
        for index in range(1,len(menu_list)):
            print(f'{index}.{menu_list[index]}')
        print(f'0.{menu_list[0]}')
        print('------------------------')
        try:
            num = int(input('>> 메뉴 : '))
        except ValueError:
            return -1
        else:return num
    def menu_login(self):
        print('========로그인========')
        user_id = input('>> 아이디 : ')
        password = input('>> 비밀번호 : ')
        
        if self.msv.login(user_id,password):
            self.msv.current_user = self.msv.login(user_id, password)
            print(f'{self.msv.current_user}님 환영합니다')
            if self.msv.current_user == self.msv.ADMIN_ID:
                self.run_admin_menu()
            else: self.run_banking_menu()
    def menu_join(self):
        print('========회원가입========')
        user_id = input('>> 아이디 : ')
        password = input('>> 비밀번호 : ')
        name = input('>> 이름 : ')
        if self.msv.join(Member(user_id,password,name)):
            print('회원가입에 성공하셨습니다')
        else:
            print('회원가입에 실패하였습니다')

    def run_banking_menu(self):
        print('========은행 업무 메뉴========')
        while True:
            menu = self.select_menu(ConsoleBank.banking_menu)
            if menu == 0:
                self.msv.logout() 
                break
            elif menu == 1:
                self.menu_list_my_account() 
            elif menu == 2:
                self.menu_deposit()
            elif menu == 3:
                self.menu_withdraw()
            elif menu == 4:
                self.menu_create_account()
            elif menu == 5:
                self.menu_delete_account()
            elif menu == 6:
                if self.menu_view_myinfo():
                    break


    def menu_update_password(self):
        org_password = input('>> 기존 비밀번호 입력 : ')
        new_password = input('>> 새 비밀번호 입력 : ')
        
        self.msv.update_password(self.msv.current_user,org_password, new_password)

    def menu_delete_membership(self):
        self.msv.logout() 
        return self.msv.delete(self.msv.current_user)

    def menu_view_myinfo(self):
        return self.run_my_info_menu()

    def run_my_info_menu(self):
        print('========내 정보 메뉴========')
        while True:
            menu = self.select_menu(ConsoleBank.member_myinfo_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_update_password() 
            elif menu == 2:
                if self.menu_delete_membership():
                    return True

    
    def menu_delete_account(self):
        account_no = input('>> 삭제할 계좌번호 : ')
        password = input('>> 삭제할 계좌 비밀번호 : ')
        self.asv.delete_account(self.msv.current_user,account_no,password)

    def menu_create_account(self):
        account_password = input('>> 생성할 계좌 비밀번호 : ')
        self.asv.create_account(Account(0,self.msv.current_user,0,account_password))
    def menu_withdraw(self):
        print('========출금========')
        self.list_member_account(self.msv.current_user)
        id = input('>> 아이디 : ')
        account_no = input('>> 계좌번호 : ')
        amount = int(input('>> 입금액 : '))
        password = input('>> 비밀번호 : ')
        if self.asv.withdraw(id,account_no,amount,password):
            print(f'계좌번호{account_no}에서{amount:,}원을 출금했습니다')
            balance = self.asv.get_account_balance(account_no)
            if balance >= 0:
                print(f'잔액{balance:,}')
        else:print('출금 실패')
    def menu_deposit(self):
        print('========입금========')
        self.list_member_account(self.msv.current_user)
        account_no = input('>> 계좌번호 : ')
        amount = int(input('>> 입금액 : '))
        if self.asv.diposit(account_no,amount):
            print(f'계좌번호{account_no}에{amount:,}원을 입금했습니다')
            balance = self.asv.get_account_balance(account_no)
            if balance >= 0:
                print(f'잔액{balance:,}')
        else:print('입금실패')

    def menu_list_my_account(self):
        self.list_member_account(self.msv.current_user)

    def list_member_account(self,id):
        account_list = self.asv.get_member_account(id)
        print('------------------------')
        if account_list:
            for i in self.asv.get_member_account(id):
                print(i)
        else: print('등록된 계좌가 없습니다')
        print('------------------------')
    def run_admin_menu(self):
        print('========관리자 메뉴========')
        while True:
            menu = self.select_menu(ConsoleBank.admin_menu)
            if menu == 0:
                self.msv.logout() 
                break
            elif menu == 1:
                self.menu_manage_members()
            elif menu == 2:
                self.menu_manage_accounts()
    def menu_manage_members(self):
        self.run_admin_member_menu()
    def menu_manage_accounts(self):
        self.run_admin_account_menu()

    def run_admin_account_menu(self):
        print('========회원 관리 메뉴========')
        while True:
            menu = self.select_menu(ConsoleBank.admin_member_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_list_members()

            elif menu == 2:
                self.menu_view_member_info()
    def run_admin_member_menu(self):
        print('========회원 계좌 관리 메뉴========')
        while True:
            menu = self.select_menu(ConsoleBank.admin_account_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_list_all_accounts()
            elif menu == 2:
                self.menu_list_member_accounts()
            elif menu == 3:
                self.menu_delete_member()

    def menu_list_all_accounts(self):
        if self.msv.list_member() == None:
            print('유저가 없습니다')
        else:
            self.msv.list_member()
    def menu_list_member_accounts(self):
        user_id = input('>> 조회할 유저 아이디 : ')
        if self.asv.get_member_account(user_id) == None:
            print('유저가 없거나 유저의 계좌가 존재하지 않습니다')
        else:
            self.asv.get_member_account(user_id)
    def menu_delete_member(self):
        user_id = input('>> 강퇴시킬 유저 아이디 : ')
        if user_id == self.msv.current_user:
            print('관리자는 탈퇴가 불가능합니다')
        else:
            if self.asv.get_member_account(user_id):
                for i in self.asv.get_member_account(user_id):
                    self.asv.admin_delete_account(i)
            self.msv.delete(user_id)
    

    def menu_list_members(self):
        self.msv.list_member()
    def menu_view_member_info(self):
        user_id = input('>> 조회할 유저 아이디 : ')
        self.msv.view_member_info(user_id)



if __name__ == '__main__':
    consolebank = ConsoleBank()
    consolebank.main()
