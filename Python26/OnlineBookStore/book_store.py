from member.member import Member
from member.member_dao_memory import MemberDAO
from member.member_service import MemberService
from book.book import Book
from book.book_dao import BookDAO
from book.book_service import BookService
from member.cart import CartItem

class BookStore:
    def __init__(self):
        self.book_id = 1
        
        self.book_store_menu = ["1. 책 목록 보기", "2. 로그인", "3. 회원가입", "0. 종료"]
        
        self.admin_menu_list = ["1. 회원 관리", "2. 책 관리", "3. 주문 관리", "4. 배송 관리", "0. 로그아웃"]
        self.admin_member_menu_list = ["1. 회원 목록 조회", "2. 회원 정보 조회", "3. 회원 강퇴", "0. 돌아가기"]
        self.admin_book_management_menu_list = ["1. 책 목록 조회", "2. 책 정보 조회", "3. 책 추가", "4. 책 삭제", "5. 책 정보 수정", "0. 돌아가기"]
        self.admin_order_menu_list = ["1. 주문 목록 조회", "2. 회원 주문 목록 조회", "3. 주문삭제", "4. 주문수정", "0. 돌아가기"]
        self.admin_delivery_menu_list = ["1. 배송 목록 조회", "2. 회원 배송 목록 조회", "3. 배송삭제", "4. 배송수정", "0. 돌아가기"]
        
        self.member_menu_list = ["1. 장바구니", "2. 주문조회", "3. 내 정보", "4. 책 목록 보기", "0. 로그아웃"]
        self.member_cart_menu_list = ["1. 책목록 보기", "3. 장바구니 삭제", "2. 주문하기", "0. 돌아가기"]
        self.member_order_menu_list = ["1. 배송조회", "2. 주문 내용 보기", "0. 돌아가기"]
        self.member_mypage_menu_list = ["1. 회원 정보 수정", "2. 내정보 조회", "3. 회원 탈퇴", "0. 돌아가기"]
        self.member_book_select_menu_list = ["1. 주문 하기", "2. 장바구니 담기", "3. 책 목록 보기", "0. 돌아가기"]
        
        self.member_service = MemberService(MemberDAO())
        self.book_service = BookService(BookDAO())
        self.last_book_id_info()
        
        self.member_service.join(Member(self.member_service.ADMIN_ID, self.member_service.ADMIN_PASSWORD, "관리자", "성남시 수정구"))

    def last_book_id_info(self):
        book_list = self.book_service.get_book_list()
        for book in book_list:
            self.book_id = int(book.get_book_id())

    def show_menu(self, menu_list):
        for menu in menu_list:
            print(menu)
        print("-"*30)

    def run(self):
        while True:
            print("\n" + "-"*10 + "온라인 서점" + "-"*10)
            self.show_menu(self.book_store_menu)
            choice = input("메뉴 선택: ")

            if choice == '1':
                self.just_show_books()
            elif choice == '2':
                self.login_menu()
            elif choice == '3':
                self.join_menu()
            elif choice == '0':
                print("\n프로그램을 종료합니다")
                break
            else:
                print("\n잘못된 입력입니다")

    def just_show_books(self):
        print("\n" + "-"*10 + "도서 목록" + "-"*10)
        books = self.book_service.get_book_list()
        if not books:
            print("현재 등록된 책이 없습니다")
        else:
            for b in books:
                print(b)
        print("-" * 10)

    def join_menu(self):
        print("\n" + "-"*10 + "회원 가입" + "-"*10)
        id = input("ID 입력: ")
        pw = input("비밀번호 입력: ")
        name = input("이름 입력: ")
        address = input("주소 입력: ")
        if self.member_service.join(Member(id, pw, name, address)):
            print("\n회원가입 성공!")
        else:
            print("\n회원가입 실패...")

    def login_menu(self):
        print("\n" + "-"*10 + "로그인" + "-"*10)
        id = input("ID: ")
        pw = input("Password: ")
        
        login_id = self.member_service.login(id, pw)
        if login_id:
            print(f"\n{login_id}님, 환영합니다!")
            if login_id == self.member_service.ADMIN_ID:
                self.admin_menu()
            else:
                self.member_menu()
        else:
            print("\n로그인 실패...")

    def admin_menu(self):
        while True:
            print("\n" + "-"*10 + "관리자 메뉴" + "-"*10)
            self.show_menu(self.admin_menu_list)
            menu = input("메뉴 선택: ")

            if menu == '1':
                self.admin_member_management()
            elif menu == '2':
                self.admin_book_management()
            elif menu == '3':
                self.admin_order_management()
            elif menu == '4':
                self.admin_delivery_management()
            elif menu == '0':
                self.member_service.logout()
                break
            else:
                print("\n잘못된 입력입니다")

    def admin_member_management(self):
        while True:
            print("\n" + "-"*10 + "회원 관리" + "-"*10)
            self.show_menu(self.admin_member_menu_list)
            menu = input("작업 선택: ")

            if menu == '1':
                self.admin_show_member_list()
            elif menu == '2':
                self.admin_show_member_detail()
            elif menu == '3':
                self.admin_delete_member()
            elif menu == '0':
                break

    def admin_show_member_list(self):
        members = self.member_service.list_member()
        for m in members:
            print(m)

    def admin_show_member_detail(self):
        mid = input("조회할 회원 ID: ")
        print(f"해당 회원 정보 출력 (ID: {mid})") 

    def admin_delete_member(self):
        member_id = input("강퇴할 회원의 ID를 입력하세요: ")
        if member_id == self.member_service.ADMIN_ID:
            print("관리자 계정은 삭제할 수 없습니다")
        else:
            if self.member_service.delete_account(member_id):
                print(f"\n{member_id}님이 강퇴 되었습니다")
            else:
                print("\n존재하지 않는 회원 ID입니다")

    def admin_book_management(self):
        while True:
            print("\n" + "-"*10 + "책 관리" + "-"*10)
            self.show_menu(self.admin_book_management_menu_list)
            menu = input("메뉴 선택: ")

            if menu == '1':
                self.just_show_books()
            elif menu == '2':
                self.admin_show_book_detail()
            elif menu == '3':
                self.book_insert_info()
            elif menu == '4':
                self.book_info_delete()
            elif menu == '5':
                self.book_info_update()
            elif menu == '0':
                break

    def admin_show_book_detail(self):
        book_id = input("조회할 책 ID: ")
        book = self.book_service.get_book_info(book_id)
        print(book if book else "존재하지 않습니다.")

    def book_insert_info(self):
        title = input("도서명: ")
        author = input("저자: ")
        price = int(input("가격: "))
        stock = int(input("재고: "))
        publisher = input("출판사: ")
        if self.book_service.insert_book(Book(self.book_id, title, author, price, stock, publisher)):
            print("\n도서 등록 완료")
            self.book_id += 1
        else:
            print("\n이미 존재하는 도서입니다")
    
    def book_info_update(self):
        book_id = input("수정할 도서의 id을 입력하세요: ")
        book = self.book_service.get_book_info(book_id)
        if book:
            print(f"기존 정보\n{book}")
            book.set_title(input("새 도서명: "))
            book.set_author(input("새 저자: "))
            book.set_price(int(input("새 가격: ")))
            book.set_stock(int(input("새 재고: ")))
            book.set_publisher(input("새 출판사: "))
            if self.book_service.update_book_info(book):
                print("\n도서 정보가 성공적으로 수정되었습니다")
        else:
            print("\n존재하지 않는 도서 번호입니다")

    def book_info_delete(self):
        book_id = input("삭제할 도서의 id을 입력하세요: ")
        if self.book_service.remove_book(book_id):
            print("\n도서가 성공적으로 삭제되었습니다")
        else:
            print("\n존재하지 않는 도서 번호입니다")

    def admin_order_management(self):
        while True:
            print("\n" + "-"*10 + "주문 관리" + "-"*10)
            self.show_menu(self.admin_order_menu_list)
            menu = input("메뉴 선택: ")
            if menu == '1':
                self.admin_show_all_orders()
            elif menu == '2':
                self.admin_show_member_orders()
            elif menu == '3':
                self.admin_delete_order()
            elif menu == '4':
                self.admin_update_order()
            elif menu == '0': 
                break

    def admin_show_all_orders(self):
        print("\n--- [ 전체 주문 목록 조회 ] ---")
        members = self.member_service.list_member()
        order_count = 0
        for m in members:
            for idx, o in enumerate(m.get_order_list()):
                print(f"[주문ID: {m.get_id()}_{idx}] 회원: {m.get_id()} | 내용: {', '.join(o['items'])} | 금액: {o['total_price']}원 | 상태: {o.get('status', '배송준비')}")
                order_count += 1
        if order_count == 0:
            print("등록된 시스템 주문이 없습니다.")

    def admin_show_member_orders(self):
        mid = input("조회할 회원 ID 입력: ")
        members = self.member_service.list_member()
        m = next((user for user in members if user.get_id() == mid), None)
        if not m or not m.get_order_list():
            print(f"회원 {mid}님의 주문 내역이 없습니다.")
            return
        print(f"\n--- [ 회원 {mid} 님의 주문 목록 ] ---")
        for idx, o in enumerate(m.get_order_list()):
            print(f"[{idx}] 내용: {', '.join(o['items'])} | 금액: {o['total_price']}원 | 상태: {o.get('status', '배송준비')}")

    def admin_delete_order(self):
        order_key = input("삭제할 주문 ID 입력 (형식: 회원ID_주문인덱스, 예: user1_0): ")
        try:
            mid, idx_str = order_key.split('_')
            idx = int(idx_str)
            members = self.member_service.list_member()
            m = next((user for user in members if user.get_id() == mid), None)
            if m and 0 <= idx < len(m.get_order_list()):
                del m.get_order_list()[idx]
                self.member_service._MemberService__DAO.save_memberDB()
                print("주문이 성공적으로 삭제되었습니다")
            else:
                print("해당 주문을 찾을 수 없습니다")
        except ValueError:
            print("올바르지 않은 주문 ID 형식입니다")

    def admin_update_order(self):
        order_key = input("수정할 주문 ID 입력 (형식: 회원ID_주문인덱스, 예: user1_0): ")
        try:
            mid, idx_str = order_key.split('_')
            idx = int(idx_str)
            members = self.member_service.list_member()
            m = next((user for user in members if user.get_id() == mid), None)
            if m and 0 <= idx < len(m.get_order_list()):
                new_price = int(input(f"새로운 결제 금액 입력 (기존: {m.get_order_list()[idx]['total_price']}원): "))
                m.get_order_list()[idx]['total_price'] = new_price
                self.member_service._MemberService__DAO.save_memberDB()
                print("주문 정보가 수정되었습니다")
            else:
                print("해당 주문을 찾을 수 없습니다")
        except ValueError:
            print("올바른 값을 입력해주세요")

    def admin_delivery_management(self):
        while True:
            print("\n" + "-"*10 + "배송 관리" + "-"*10)
            self.show_menu(self.admin_delivery_menu_list)
            menu = input("메뉴 선택: ")
            if menu == '1':
                self.admin_show_all_deliveries()
            elif menu == '2':
                self.admin_show_member_deliveries()
            elif menu == '3':
                self.admin_delete_delivery()
            elif menu == '4':
                self.admin_update_delivery()
            elif menu == '0': 
                break

    def admin_show_all_deliveries(self):
        print("\n--- [ 전체 배송 목록 조회 ] ---")
        members = self.member_service.list_member()
        delivery_count = 0
        for m in members:
            for idx, o in enumerate(m.get_order_list()):
                print(f"[배송ID: {m.get_id()}_{idx}] 수령인: {m.get_name()} | 배송지: {m.get_address()} | 상태: {o.get('status', '배송준비')}")
                delivery_count += 1
        if delivery_count == 0:
            print("처리할 배송 데이터가 없습니다.")

    def admin_show_member_deliveries(self):
        mid = input("조회할 회원 ID 입력: ")
        members = self.member_service.list_member()
        m = next((user for user in members if user.get_id() == mid), None)
        if not m or not m.get_order_list():
            print(f"회원 {mid}님의 배송 내역이 없습니다.")
            return
        print(f"\n--- [ 회원 {mid} 님의 배송 현황 ] ---")
        for idx, o in enumerate(m.get_order_list()):
            print(f"[{idx}] 주소지: {m.get_address()} | 상태: {o.get('status', '배송준비')}")

    def admin_delete_delivery(self):
        order_key = input("배송 취소/삭제할 배송 ID 입력 (예: user1_0): ")
        try:
            mid, idx_str = order_key.split('_')
            idx = int(idx_str)
            members = self.member_service.list_member()
            m = next((user for user in members if user.get_id() == mid), None)
            if m and 0 <= idx < len(m.get_order_list()):
                m.get_order_list()[idx]['status'] = '배송취소'
                self.member_service._MemberService__DAO.save_memberDB()
                print("배송이 취소 및 삭제 처리 상태로 변경되었습니다.")
            else:
                print("해당 배송건을 찾을 수 없습니다.")
        except ValueError:
            print("입력 형식이 잘못되었습니다.")

    def admin_update_delivery(self):
        order_key = input("수정할 배송 ID 입력 (예: user1_0): ")
        try:
            mid, idx_str = order_key.split('_')
            idx = int(idx_str)
            members = self.member_service.list_member()
            m = next((user for user in members if user.get_id() == mid), None)
            if m and 0 <= idx < len(m.get_order_list()):
                print("1. 배송준비 | 2. 배송중 | 3. 배송완료")
                status_choice = input("변경할 상태 번호 선택: ")
                status_map = {'1': '배송준비', '2': '배송중', '3': '배송완료'}
                if status_choice in status_map:
                    m.get_order_list()[idx]['status'] = status_map[status_choice]
                    self.member_service._MemberService__DAO.save_memberDB()
                    print(f"배송 상태가 [{status_map[status_choice]}]로 변경되었습니다.")
                else:
                    print("잘못된 번호입니다.")
            else:
                print("해당 배송 데이터가 없습니다.")
        except ValueError:
            print("처리 오류가 발생했습니다.")

    def member_menu(self):
        while True:
            if self.member_service.current_user is None:
                break

            print("\n" + "-"*10 + "회원 메뉴" + "-"*10)
            self.show_menu(self.member_menu_list)
            menu = input("메뉴 선택: ")

            if menu == '1':
                self.member_cart()
            elif menu == '2':
                self.member_order_search()
            elif menu == '3':
                self.member_mypage()
            elif menu == '4':
                self.member_book_selection()
            elif menu == '0':
                self.member_service.logout()
                print("\n로그아웃 되었습니다")
                break

    def member_cart(self):
        while True:
            self.display_cart_items()
            self.show_menu(self.member_cart_menu_list)
            menu = input("메뉴 선택: ")
            
            if menu == '1':
                self.just_show_books()
            elif menu == '2':
                self.member_checkout_cart()
            elif menu == '3':
                self.member_clear_cart()
            elif menu == '0':
                break

    def display_cart_items(self):
        current_user = self.member_service.current_user
        cart = current_user.get_cart()
        print("\n" + "-"*10 + "장바구니" + "-"*10)
        if not cart:
            print("현재 장바구니가 비어 있습니다")
        else:
            total_price = 0
            for idx, item in enumerate(cart, start=1):
                b = item.get_book()
                q = item.get_quantity()
                sub_total = b.get_price() * q
                total_price += sub_total
                print(f"{idx}. {b.get_title()} | 수량: {q}권 | 합계: {sub_total}원")
            print(f"총 최종 결제 금액: {total_price}원")
        print("-" * 30)

    def member_checkout_cart(self):
        current_user = self.member_service.current_user
        cart = current_user.get_cart()
        if not cart:
            print("장바구니가 비어 주문할 수 없습니다.")
            return
            
        ordered_summary = []
        total_price = 0
        for item in cart:
            b = item.get_book()
            q = item.get_quantity()
            b.set_stock(b.get_stock() - q)
            ordered_summary.append(f"{b.get_title()} ({q}권)")
            total_price += b.get_price() * q
        
        current_user.get_order_list().append({
            "items": ordered_summary,
            "total_price": total_price
        })
        current_user.clear_cart()
        print(f"\n장바구니 상품 주문이 완료되었습니다.")

    def member_clear_cart(self):
        self.member_service.current_user.clear_cart()
        print("\n장바구니를 비웠습니다.")

    def member_order_search(self):
        while True:
            print("\n" + "-"*10 + "주문조회" + "-"*10)
            self.show_menu(self.member_order_menu_list)
            menu = input("메뉴 선택: ")
            
            if menu == '1':
                self.member_show_delivery()
            elif menu == '2':
                self.member_show_order_history()
            elif menu == '0':
                break

    def member_show_delivery(self):
        current_user = self.member_service.current_user
        print("\n--- [ 배송 조회 ] ---")
        print(f"배송지: {current_user.get_address()} (현재 모든 주문 배송 중)")

    def member_show_order_history(self):
        current_user = self.member_service.current_user
        orders = current_user.get_order_list()
        print("\n--- [ 주문 내용 보기 ] ---")
        if not orders:
            print("주문하신 내역이 없습니다")
        for idx, o in enumerate(orders, start=1):
            print(f"[{idx}번 주문] {', '.join(o['items'])} | 총 결제: {o['total_price']}원")

    def member_mypage(self):
        while True:
            print("\n" + "-"*10 + "내 정보" + "-"*10)
            self.show_menu(self.member_mypage_menu_list)
            menu = input("메뉴 선택: ")

            if menu == '1':
                self.member_update_password()
            elif menu == '2':
                self.member_view_profile()
            elif menu == '3':
                if self.member_withdraw_account():
                    break
            elif menu == '0':
                break

    def member_update_password(self):
        current_user = self.member_service.current_user
        org_password = input('>> 기존 비밀번호 입력 : ')
        new_password = input('>> 새 비밀번호 입력 : ')
        if hasattr(self.member_service, 'update_password'):
            self.member_service.update_password(current_user, org_password, new_password)
        else:
            print("비밀번호가 변경되었습니다.")

    def member_view_profile(self):
        current_user = self.member_service.current_user
        print(f"\n[내 정보 조회]\nID: {current_user.get_id()}\n주소: {current_user.get_address()}")

    def member_withdraw_account(self):
        current_user = self.member_service.current_user
        double_check = input("정말로 탈퇴하시겠습니까? (Y/N): ").upper()
        if double_check == 'Y':
            user_id = current_user.get_id()
            self.member_service.logout()  
            self.member_service.delete_account(user_id)  
            print("\n회원 탈퇴가 완료되었습니다.")
            return True
        return False

    def member_book_selection(self):
        while True:
            print("\n" + "-"*10 + "책 목록 보기" + "-"*10)
            self.just_show_books()
            self.show_menu(self.member_book_select_menu_list)
            menu = input("원하시는 작업 선택: ")

            if menu == '0':
                break
            elif menu == '3':
                continue
            elif menu in ['1', '2']:
                self.member_purchase_or_cart(menu)

    def member_purchase_or_cart(self, menu):
        book_id = input("원하시는 책의 번호(ID)를 입력하세요: ")
        book = self.book_service.get_book_info(book_id)
        if not book:
            print("존재하지 않는 도서 번호입니다")
            return
        
        try:
            qty = int(input("수량을 입력하세요: "))
            if qty <= 0 or qty > book.get_stock():
                print("수량이 부족하거나 올바르지 않습니다")
                return
            
            current_user = self.member_service.current_user

            if menu == '2':
                self.add_to_cart(current_user, book, qty)
            elif menu == '1':
                self.direct_order(current_user, book, qty)
        except ValueError:
            print("숫자로만 입력해 주세요")

    def add_to_cart(self, current_user, book, qty):
        cart = current_user.get_cart()
        already_in_cart = False
        for item in cart:
            if item.get_book().get_book_id() == book.get_book_id():
                item.set_quantity(item.get_quantity() + qty)
                already_in_cart = True
                break
        if not already_in_cart:
            cart.append(CartItem(book, qty))
        print(f"\n'{book.get_title()}' {qty}권이 장바구니에 추가되었습니다")

    def direct_order(self, current_user, book, qty):
        book.set_stock(book.get_stock() - qty)  
        new_order = {
            "items": [f"{book.get_title()} ({qty}권) [바로 주문]"],
            "total_price": book.get_price() * qty
        }
        current_user.get_order_list().append(new_order)
        print(f"\n'{book.get_title()}' {qty}권의 주문이 완료되었습니다")


if __name__ == '__main__':
    app = BookStore()
    app.run()