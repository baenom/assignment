from book.book_dao import BookDAO
from book.book import Book

class BookService:
    def __init__(self, bookDAO):
        self.ADMIN_ID = 'admin'
        self.ADMIN_PASSWORD = '1234'
        self.current_user = None
        self.__DAO = bookDAO
        self.join(Book(self.ADMIN_ID, self.ADMIN_PASSWORD, self.ADMIN_ID))

    def join(self, book):
        # book.set_id(book.get_id().lower())
        if not self.is_valid_id(book.get_id()):
            return False
        if self.__DAO.is_exist(book.get_id()):
            return False
        return self.__DAO.insert_book(book)

    def is_valid_id(self, id):
        if id.isalpha(): return True

    def login(self, id, password):
        book = self.__DAO.get_book_info(id)
        if book:
            if password == book.get_password():
                return id
        return None

    def list_book(self):
        return self.__DAO.get_all_books()

    def view_book_info(self, id):
        return self.__DAO.get_book_info(id)

    def update_book_info(self, id, new_title, new_author):
        return self.__DAO.update_book_info(id, new_title, new_author)

    def delete_book(self, id):
        if self.current_user == id or self.current_user == self.ADMIN_ID:
            return self.__DAO.delete_book(id)

    
if __name__ == '__main__':
    bs = BookService(BookDAO())
    bs.join(Book('Euijin','1234','BaeEuijin'))
    books = bs.list_book()
    for book in books:
        print(book)
    current_user = bs.login('Euijin','1234')
    print(current_user)
    bs.login('Euijin','1234')
    print(current_user)

