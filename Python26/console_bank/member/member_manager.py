from member.member import Member
from member.member_service import MemberService
from member.member_dao_memory import MemberDAO

class MemberManager:
    
    def __init__(self):
        self.start_menu = ['종료', '로그인', '회원가입']
        self.admin_menu = ['로그아웃', '회원목록', '회원정보조회', '회원탈퇴']
        self.member_menu = ['로그아웃', '내정보수정', '내정보조회', '회원탈퇴']
        self.member_dao = MemberDAO()
        self.ms = MemberService(self.member_dao)
        # self.ADMIN_ID = self.ms.ADMIN_ID
        # self.ADMIN_PASSWORD = self.ms.ADMIN_PASSWORD
        # self.current_user = self.ms.current_user
        


    def main(self):
        self.show_welcome()
        
        while True:
            menu = self.select_menu(self.start_menu)
            if menu == 0: 
                self.say_goodbye()
                break
            elif menu == 1:
                id = input('>> id : ')
                password = input('>> password : ')
                self.ms.current_user = self.ms.login(id, password)
                
                if self.ms.current_user:
                    if self.ms.current_user == self.ms.ADMIN_ID:
                        self.start_admin_menu()
                    else:
                        self.start_member_menu()
                else:
                    print('로그인 실패')
            
            elif menu == 2:
                print('==============회원 가입==============')
                id = input('>> id : ')
                password = input('>> password : ')
                name = input('>> name : ')
                member = Member(id, password, name)
                
                if self.ms.join(member):
                    print('회원가입 성공')
                else:
                    print('회원 가입 실패')
            else:
                print('없는 메뉴입니다. 다시 입력해주세요.')

    def start_admin_menu(self):
        while True:
            print('==============관리자 메뉴==============')
            menu = self.select_menu(self.admin_menu)
            if menu == 0:
                self.menu_logout()
                print('로그아웃 되었습니다.')
                break
            elif menu == 1:
                self.list_all_member()
            elif menu == 2:
                id = input('조회할 회원 아이디: ')
                member = self.ms.view_member_info(id)
                if member:
                    print('\n아이디\t이름\t비밀번호')
                    print(member)
                else:
                    print('존재하지 않는 회원입니다.')
            elif menu == 3:
                id = input('강제 탈퇴시킬 회원 아이디: ')
                if id == self.ms.ADMIN_ID:
                    print('탈퇴 불가')
                    continue
                if self.ms.delete(id):
                    print(f'{id} 탈퇴 완료')
                else:
                    print('존재하지 않는 아이디 입니다')
            else:
                print('없는 메뉴입니다')
    def menu_logout(self):
        self.ms.logout()

    def list_all_member(self):
        if self.ms.current_user != self.ms.ADMIN_ID:
            print('사용권한이 없습니다')
            return
        
        member_list = self.ms.list_member()
        if len(member_list) <= 1:
            print('가입한 회원이 없습니다')
        else:
            print('아이디\t이름\t비밀번호')
            for i in member_list:
                if i.get_id() == self.ms.ADMIN_ID:
                    continue
                print(i)
        

    def start_member_menu(self):
        while True:
            print('\n==============회원 메뉴==============')
            menu = self.select_menu(self.member_menu)
            if menu == 0:
                self.ms.current_user = None
                print('로그아웃 되었습니다')
                break
            elif menu == 1:
                new_name = input('새 이름 입력: ')
                if self.ms.update_member_info(self.ms.current_user, new_name):
                    print('정보 수정 완료')
                else:
                    print('정보 수정 실패')

                org_password = input('기존 비밀번호 입력: ')
                new_password = input('새 비밀번호 입력: ')

                if self.ms.update_password(self.ms.current_user, org_password, new_password):
                    print('비밀번호 수정 완료')
                else:
                    print('비밀번호 수정 실패')
            elif menu == 2:
                member = self.ms.view_member_info(self.ms.current_user)
                if member:
                    print('아이디\t이름\t비밀번호')
                    print(member)
            elif menu == 3:
                if self.ms.delete(self.ms.current_user):
                    print('탈퇴 완료')
                    self.ms.current_user = None
                    break
            else:
                print('없는 메뉴입니다.')

    def show_welcome(self):
        print('='*50)
        title = 'Member Manager'
        print(f'{title:^50}')
        print('='*50)

    def say_goodbye(self):
        print('프로그램을 종료합니다. 안녕히 계세요!')

    def print_menu(self, menu_list):
        for i in range(1, len(menu_list)):
            print(f'{i}. {menu_list[i]}')
        print(f'0. {menu_list[0]}')

    def select_menu(self, menu_list):
        self.print_menu(menu_list)
        try:
            menu = int(input('메뉴 선택: '))
            return menu
        except ValueError:
            return -1


if __name__ == '__main__':
    membermanager = MemberManager()
    membermanager.main()