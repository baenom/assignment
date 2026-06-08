from book.book_dao import BookDAO

class Book:
    def __init__(self, book_name, book_detail, book_price,publisher,status):
        self.__book_name = book_name
        self.__book_detail = book_detail
        self.__book_price = book_price
        self.__publisher = publisher
        self.__status = status

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
    def set_book_name(self, book_name):
        self.__book_name = book_name

    def set_book_detail(self, book_detail):
        self.__book_detail = book_detail

    def set_book_price(self, book_price):
        self.__book_price = book_price

    def set_publisher(self, publisher):
        self.__publisher = publisher

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return f'{self.__book_name}\t{self.__book_detail}\t{self.__book_price}\t{self.__publisher}\t{self.__status}'

if __name__ == '__main__':
    dao = BookDAO()
    book = Book('Python 프로그래밍','Python 기초 문법',20000,'한빛미디어',True)
    dao.insert_book(book)
    print(dao.is_exist('Python 프로그래밍'))

    books = dao.get_all_books()
    for book in books:
        print(book)
    book = dao.get_book_info('Python 프로그래밍')
    if book:
        book.set_book_price(25000)
        dao.update_book_info('Python 프로그래밍',book)

    books = dao.get_all_books()
    for book in books:
        print(book)