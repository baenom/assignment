from book.book import Book
import joblib
class BookDAO:

    BOOK_DB_FILE = 'C:/Users/USER/assignment/Python26/console_bank/db/bookDB.pkl'
    def __init__(self):
        self.__bookDB = self.__load_bookDB()

    def __load_bookDB(self):
        try:
            return joblib.load(BookDAO.BOOK_DB_FILE)
        except FileNotFoundError:
            return {}

    def save_bookDB(self):
        if self.__bookDB:
            joblib.dump(self.__bookDB,BookDAO.BOOK_DB_FILE)
    def update_bookDB(self):
        self.save_bookDB()
        self.__load_bookDB()


    

    def insert_book(self,book):
        book_no = book.get_book_no()
        if book_no not in self.__bookDB:
            self.__bookDB[book.get_book_no()] = book
            self.update_bookDB()
            return True
        return False

    def select_book_by_book_no(self,book_no):
        if book_no in self.__bookDB:
            return self.__bookDB[book_no]

    def select_all_books(self):
        book_list = list(self.__bookDB.values())
        if len(book_list):
            return book_list
        return []
    
    def update_book(self,book_no,book):
        if book_no in self.__bookDB:
            self.__bookDB[book_no] = book
            self.update_bookDB()
            return True
        return False

    def delete_book(self,book_no):
        if book_no in self.__bookDB:
            self.__bookDB.pop(book_no)
            self.update_bookDB()
            return True
        return False