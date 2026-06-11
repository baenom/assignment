from book.book import Book
import joblib
class BookDAO:
    BOOK_DB_FILE = './db/bookDB.pkl'
    def __init__(self):
        self.__book_insert_counter = 1
        self.__bookDB = self.__load_bookDB(BookDAO.BOOK_DB_FILE)

    def __load_bookDB(self):
        try:
            self.__bookDB = joblib.load(BookDAO.BOOK_DB_FILE)
        except FileNotFoundError:
            self.__bookDB = {}
        
    def save_bookDB(self):
        if self.__bookDB:
            joblib.dump(self.__bookDB,BookDAO.BOOK_DB_FILE)

    def update_bookDB(self):
        self.save_bookDB()
        self.__load_bookDB()

    def insert_book(self, book):
        if self.is_exist(book.get_book_id()):
            return False
        self.__bookDB[book.get_book_id()] = book
        self.__book_insert_counter += 1
        return True

    def is_exist(self, book_id):
        return book_id in self.__bookDB

    def get_book_info(self, book_id):
        return self.__bookDB.get(book_id)

    def get_all_books(self):
        return self.__bookDB

    def update_book(self, updated_book):
        if self.is_exist(updated_book.get_book_id()):
            self.__bookDB[updated_book.get_book_id()] = updated_book
            return True
        return False

    def delete_book(self, book_id):
        if self.is_exist(book_id):
            del self.__bookDB[book_id]
            return True
        return False