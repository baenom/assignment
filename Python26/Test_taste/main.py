from test.test import Test
from test.test_service import TestService
from test.test_dao import TestDAO
from member.member import Member
from member.member_service import MemberService
from member.member_dao import MemberDAO
from cart.cart_service import CartService
from cart.cart_dao import CartDAO
    
class TestTaste:
    def __init__(self):
        self.start_menu = ['종료','로그인','회원가입']
        self.admin_menu = ['로그아웃','회원 강퇴','문제 숨기기']
        self.member_menu = ['로그아웃','문제 만들기','내 문제보기','내 정답보기','내 정보보기','문제 바로구매','장바구니 결제','장바구니 추가']
        self.my_info_menu = ['뒤로가기','내정보 업데이트','비밀번호 수정','회원 탈퇴']
        self.msv = MemberService(MemberDAO())
        self.tsv = TestService(TestDAO())
        self.csv = CartService(CartDAO())
        if self.msv.get_members_info(self.msv.ADMIN_ID) is None:
            self.msv.join(Member(self.msv.ADMIN_ID,'관리자',self.msv.ADMIN_PASSWORD,None))
    def start(self):
        while True:
            self.select_menu(self.start_menu)
            self.test_list_shows()
            try:
                menu = int(input("메뉴를 선택하세요: "))
            except ValueError:
                print('올바른 메뉴를 입력하세요')
            else:
                if menu == 1:
                    self.login()
                elif menu == 2:
                    self.join()
                elif menu == 0:
                    break
                else:
                    print('잘못된 메뉴입니다')
    def join(self):
        id = input('id를 입력하세요: ')
        name = input('name을 입력하세요: ')
        password = input('password를 입력하세요: ')
        self.msv.join(Member(id,name,password,[]))
        print(f"{id}님 환영합니다")
        
    def login(self):
        id = input('id를 입력하세요: ')
        password = input('password를 입력하세요: ')
        if id == self.msv.login(id,password):
            print(f"{id}님 환영합니다")
            if id == self.msv.ADMIN_ID:
                self.admin_main()
            else:
                self.member_main()
        else:
            print("로그인에 실패하였습니다")
    def select_menu(self,menu):
        print('-----------------')
        for i in range(len(menu)):
            print(f'{i}. {menu[i]}')
        print('-----------------')

    def admin_main(self):
        while True:
            self.select_menu(self.admin_menu)
            self.admin_test_list_shows()
            try:
                menu = int(input("메뉴를 선택하세요: "))
            except ValueError:
                print('올바른 메뉴를 입력하세요')
            else:
                if menu == 1:
                    self.delete_member()
                elif menu == 2:
                    self.hiden_test()
                elif menu == 0:
                    self.msv.logout()
                    break
                else:
                    print('잘못된 메뉴입니다')
    def delete_member(self):
        if self.msv.list_member() == []:
            print('회원이 없습니다')
        else:
            id = input('강퇴시킬 id를 입력하세요')
            if id != self.msv.ADMIN_ID:
                self.msv.delete_member(id)
    def hiden_test(self):
        if self.tsv.get_all_test_name() == []:
            print('문제가 없습니다')
        else:
            id = input('상태를 바꿀 문제지id를 입력하세요')
            self.tsv.hiden_test(id)

    def member_main(self):
        while True:
            self.select_menu(self.member_menu)
            self.test_list_shows()
            try:
                menu = int(input("메뉴를 선택하세요: "))
            except ValueError:
                print('올바른 메뉴를 입력하세요')
            else:
                if menu == 1:
                    self.make_test()
                elif menu == 2:
                    self.my_test()
                elif menu == 3:
                    self.my_answer()
                elif menu == 4:
                    if self.my_menu():
                        self.msv.logout()
                        self.csv.clening_cart()
                        break
                elif menu == 5:
                    self.buy_test()
                elif menu == 6:
                    self.cart_test_buy()
                elif menu == 7:
                    self.cart_test_add()
                elif menu == 0:
                    self.msv.logout()
                    self.csv.clening_cart()
                    break
                else: 
                    print('잘못된 메뉴입니다')

    def buy_test(self):
        if self.tsv.get_all_test_name() == []:
            print('문제가 없습니다')
            return
        try:
            id = int(input('구매할 문제지 id를 입력하세요: '))
            user_id = self.msv.current_user

            member_obj = self.msv.get_members_info(user_id)

            if member_obj is not None:
                if self.msv.update_test_id_info(member_obj, id):
                    print('문제를 바로 구매하였습니다')
            else:
                print("유저 정보를 데이터베이스에서 찾을 수 없습니다")
        except ValueError:
            print("숫자로 된 ID를 입력해 주세요")


    def cart_test_add(self):
        if self.tsv.get_all_test_name() == []:
            print('문제가 없습니다')
        else:
            try:
                id = int(input('문제지 id를 입력하세요: '))
                
                if self.csv.insert_cart(id):
                    print('문제가 추가되었습니다')
            except ValueError:
                print('숫자로 입력하세요')

    def cart_test_buy(self):
        test_list = []
        for i in self.csv.get_cart():
            print(self.tsv.get_test_name(i))
            test_list.append(i)

        cart = input('(y/n)로 구매를 결정해주세요: ')
        
        if cart.lower() == 'y':
            user_id = self.msv.current_user
            
            member_obj = self.msv.get_members_info(user_id)
            
            if member_obj is not None:
                for i in test_list:
                    self.msv.update_test_id_info(member_obj, i)
                self.csv.clening_cart()
                print("장바구니 결제가 완료되었습니다")
            else:
                print("유저 정보를 데이터베이스에서 찾을 수 없습니다")

    def my_test(self):
        user_id = self.msv.current_user

        test_ids = self.msv.get_members_test(user_id)
        
        if test_ids:
            for i in test_ids:
                answers = self.tsv.get_test_test(i)
                if answers:
                    for j in answers:
                        print(j)
        else:
            print("구매한 문제지가 없거나 유저 정보를 찾을 수 없습니다")
    def my_answer(self):
        user_id = self.msv.current_user

        test_ids = self.msv.get_members_test(user_id)
        
        if test_ids:
            for i in test_ids:
                answers = self.tsv.get_test_answer(i)
                if answers:
                    for j in answers:
                        print(j)
        else:
            print("구매한 문제지가 없거나 유저 정보를 찾을 수 없습니다")
    def my_menu(self):
        while True:
            self.select_menu(self.my_info_menu)
            self.msv.get_members_info(self.msv.current_user)
            try:
                menu = int(input("메뉴를 선택하세요: "))
            except ValueError:
                print('올바른 메뉴를 입력하세요')
            else:
                if menu == 1:
                    self.update_info()
                elif menu == 2:
                    self.update_password()
                elif menu == 3:
                    return self.delete_me()
                elif menu == 0:
                    break
                else: 
                    print('잘못된 메뉴입니다')

    def delete_me(self):
        user_id = self.msv.current_user
            
        if self.msv.delete_member(user_id):
            print("회원 탈퇴가 성공적으로 완료되었습니다")
            return True
        else:
            print("탈퇴 처리에 실패했습니다")
            return False

    def update_info(self):
        id = input('새로운 id를 입력하세요: ')
        name = input('새로운 name를 입력하세요: ')
        self.msv.update_info(self.msv.get_members_info(id),id,name)
    def update_password(self):
        old_password = input('이전 password를 입력하세요: ')
        new_password = input('새로운 password를 입력하세요: ')
        
        member_obj = self.msv.get_members_info(self.msv.current_user)
            
        if member_obj is not None:
            if self.msv.update_password(member_obj, old_password, new_password):
                print("비밀번호가 성공적으로 변경되었습니다")
        else:
            print("회원 정보를 확인할 수 없습니다")

        
    def make_test(self):
        try:
            count = int(input("제작하실 문제 개수를 입력하세요: "))
            price = int(input("제작하실 문제지 가격을 입력하세요: "))
            index = self.tsv.get_last_test_index()
            for i in range(count):
                index += 1
                test_list = []
                test = input(f'{i}번 문제 내용을 입력하세요: ')
                answer = input(f'{i}번 문제의 정답을 입력하세요: ')
                test_list.append(Test(index,test,answer,True,price))
                if self.tsv.insert_test(test_list):
                    print('문제지가 추가되었습니다')
        except ValueError:
            print('숫자를 입력하세요')

    def test_list_shows(self):
        if self.tsv.get_all_test_name() == []:
            print('문제가 없습니다')
        else:
            for i in self.tsv.get_all_test_name():
                print(i[0],i[1])
                
    def admin_test_list_shows(self):
        if self.tsv.get_all_test() == []:
            print('문제가 없습니다')
        else:
            for i in self.tsv.get_all_test():
                if i and len(i) > 0:
                    status = "[숨김]" if not i[0].get_is_hide() else "[표시중]"
                    print(f"ID {i[0].get_id()} | {status} | {i[0].get_test()}")

if __name__ == '__main__':
    app = TestTaste()
    app.start()