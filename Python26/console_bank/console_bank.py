from member.member import Member
from member.member_dao import MemberDAO
from member.member_service import MemberService
from account.account import Account
from account.account_dao import AccountDAO
from account.account_service import AccountService

class ConsoleBank:
    start_menu = ['종료','로그인','회원가입']
    banking_menu = []
    member_myinfo_menu = []
    admin_account_menu = []
    admin_member_menu = []

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.asv = AccountService(AccountDAO())
    def main(self):
        self.show_welcome()
        while True:
            menu = self.select_menu(ConsoleBank.select_menu)
            if menu == 0: break
        self.say_goodbye
    def show_welcome(self):
        pass
    def say_goodbye(self):
        pass
    def select_menu(self):
        pass

if __name__ == '__main__':
    consolebank = ConsoleBank()
    ConsoleBank.main()
