from member import Member, MemberDAO, MemberService
class MemberManager:
    
    def __init__(self):
        self.start_menu = ['종료','로그인','회원가입']
        self.admin_menu = ['로그아웃','회원목록','회원정보조회','회원탈퇴']
        self.member_menu = ['로그아웃','회원정보수정','회원정보조회','회원탈퇴']
        self.ADMIN_ID = 'admin'
        self.ADMIN_PASSWORD = '1234'
        self.current_user = None
        self.member_dao = MemberDAO()
        self.ms = MemberService(self.member_dao)

    def main(self):
        self.show_welcome()
        self.ms.join(Member(self.ADMIN_ID,self.ADMIN_PASSWORD,self.ADMIN_ID))
        while True:
            menu = self.select_menu(self.start_menu)
            if menu == 0: 
                self.say_goodbye()
                break
            elif menu == 1:
                id = input('>> id : ')
                password = input('>> password : ')
                self.current_user = self.ms.login(id,password)
                if self.current_user:
                    if self.current_user == self.ADMIN_ID:
                        self.start_admin_menu()
                    else:
                        self.start_member_manu()
                else:
                    print('로그인 실패')
                
                name = input('>> name : ')
                member = Member(id,password,name)
                if self.ms.join(member):
                    print('회원가입 성공')
                else:
                    print('회원 가입 실패')
            elif menu == 2:
                pass
            else:
                print('없는 메뉴입니다')

    def start_admin_menu(self):
        print('==============관리자 메뉴=============')
        while True:
            menu = self.select_menu(self.admin_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.list_all_member()
            elif menu == 2:
                pass
            elif menu == 3:
                pass
            else:
                print('없는 메뉴입니다')

    def list_all_member(self):
        if self.current_user != self.ADMIN_ID:
            print('사용권한이 없습니다')
            return
        member_list = self.ms.list_member()
        if len(member_list) == 1:
            print('가입한 회원이 없습니다')
        else:
            for i in member_list[1:]:
                print(i)
        

    def start_member_manu(self):
        print('==============회원 메뉴==============')
        self.print_menu()
    def show_welcome(self):
        print('='*20)
        title = 'Member Manager'
        print(f'{title:^50}')
        print('='*20)

    def say_goodbye(self):
        print('안녕히 계세요')

    def print_menu(self,menu_list):
        for i in range(1,len(menu_list)):
            print(f'{i}. {menu_list[i]}')
        print(f'0. {menu_list[0]}')

    def select_menu(self,menu_list):
        self.print_menu(menu_list)
        try:
            menu = int(input('메뉴 선택:'))
            return menu
        except ValueError:
            return -1


if __name__ == '__main__':
    membermanager = MemberManager()
    membermanager.main()