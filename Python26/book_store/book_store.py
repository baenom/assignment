from member.member import Member
from member.member_dao_memory import MemberDAO
from member.member_service import MemberService

class BookStore:
    def __init__(self):
        self.start_menu = ['종료', '로그인', '회원가입','도서조회']
        self.admin_menu = ['돌아가기', '도서 등록', '도서 삭제', '도서 목록']
        self.admin_member_menu = ['돌아가기', '회원 목록', '회원 정보 조회']
        self.msv = MemberService(MemberDAO())
    def main(self):
        self.show_welcome()
        while True:
            self.show_book_list()
            menu = self.select_menu(self.start_menu)
            if menu == 0:
                self.say_goodbye()
                break
            elif menu == 1:
                self.menu_login()
            elif menu == 2:
                self.menu_register()
            elif menu == 3:
                self.menu_search_books()
            else: print('잘못된 메뉴입니다')
    def menu_search_books(self):
        print('========책 조회========')
        book_search = input('>> 도서명 : ')
        
    def menu_login(self):
        print('========로그인========')
        user_id = input('>> 아이디 : ')
        password = input('>> 비밀번호 : ')
        self.msv.current_user = self.msv.login(user_id, password)
        if self.msv.current_user != None:
            print(f'{self.msv.current_user}님 환영합니다')
            if self.msv.current_user == self.msv.ADMIN_ID:
                self.run_admin_menu()
            else: self.run_banking_menu()
        else: print('로그인에 실패하였습니다')
    
    def menu_register(self):
        print('========회원가입========')
        user_id = input('>> 아이디 : ')
        if user_id == self.msv.ADMIN_ID:
            print('가입할수 없는 아이디입니다')
        else:
            password = input('>> 비밀번호 : ')
            name = input('>> 이름 : ')
            address = input('>> 주소 : ')
            if self.msv.join(Member(user_id,password,name,address)):
                print('회원가입에 성공하셨습니다')
            else:
                print('회원가입에 실패하였습니다')
    
    def show_book_list(self):
        print('========도서 목록========')
        print('도서의 상세 정보를 보고싶다면 메뉴에 제목을 입력해주세요')

    def select_menu(self,menu_list):
        print('------------------------')
        for index in range(1,len(menu_list)):
            print(f'{index}.{menu_list[index]}')
        print(f'0.{menu_list[0]}')
        print('------------------------')
        try:
            num = input('>> 메뉴 : ')
        except ValueError:
            return -1
        else:return num

    def show_welcome(self):
        print('========안녕하세요 EuijinBae의 서점입니다========')

    def say_goodbye(self):
        print('안녕히가세요')

if __name__ == "__main__":    
    book_store = BookStore()
    book_store.main()