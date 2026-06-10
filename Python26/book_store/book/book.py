class Book:
    def __init__(self,book_name,book_detail,book_price,publisher,status,book_details):
        self.__book_name = book_name
        self.__book_detail = book_detail
        self.__book_price = book_price
        self.__publisher = publisher
        self.__status = status
        self.__book_details = book_details
    def get_book_name(self):
        return self.__book_name
    def get_book_detail(self):
        return self.__book_detail
    def get_book_price(self):
        return self.__book_price
    def get_publisher(self):
        return self.__publisher
    def get_status(self):
        return self.__status
    def get_book_details(self):
        return self.__book_details

    def set_book_name(self,book_name):
        self.__book_name = book_name
    def set_book_detail(self,book_detail):
        self.__book_detail = book_detail
    def set_book_price(self,book_price):
        self.__book_price = book_price
    def set_publisher(self,publisher):
        self.__publisher = publisher
    def set_status(self,status):
        self.__status = status
    def set_book_details(self,book_details):
        self.__book_details = book_details

    def __str__(self):
        return f'책제목 = {self.__book_name} 책설명 = {self.__book_detail} 책가격 = {self.__book_price} 출판사 = {self.__publisher} 재고 = {self.__status} 책상세정보 = {self.__book_details}'