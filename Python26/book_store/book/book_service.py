from book.book_dao import BookDAO
from book.book import Book


class BookService:
    book_no_seq = 1
    def __init__(self,book_dao):
        self.__dao = book_dao

    def admin_create_book(self,book):

        book.set_book_no(str(BookService.book_no_seq))
        BookService.book_no_seq += 1

        return self.__dao.insert_book(book)

    def get_all_books(self):
        return self.__dao.select_all_books()
    
    def get_book_by_no(self,book_no):
        return self.__dao.select_book_by_book_no(book_no)
    
    def admin_delete_book(self,book_no):
        book = self.__dao.select_book_by_book_no(book_no)
        if not book:
            return False
        return self.__dao.delete_book(book_no)
    def admin_update_book_info(self,book_no):
        book = self.__dao.select_book_by_book_no(book_no)
        if book:
            return book
        return None