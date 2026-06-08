import jolib
class BookDAO:

    BOOK_DB_FILE = './db/bookDB.pkl'
    def __init__(self):
        self.__bookDB = self.__load_bookDB(BookDAO.BOOK_DB_FILE)

    def __load_bookDB(self):
        try:
            self.__bookDB = jolib.load(BookDAO.BOOK_DB_FILE)
        except FileNotFoundError:
            self.__bookDB = {}
        
    def save_bookDB(self):
        if self.__bookDB:
            jolib.dump(self.__bookDB,BookDAO.BOOK_DB_FILE)

    def update_bookDB(self):
        self.save_bookDB()
        self.__load_bookDB()
    def insert_book(self, book):
        if self.is_exist(book.get_book_name()):
            return False
        self.__bookDB[book.get_book_name()] = book
        self.save_bookDB()
        return True

    def is_exist(self, id):
        if id in self.__bookDB.keys() : return True
        return False

    def get_book_info(self, id):
        if self.is_exist(id):
            return self.__bookDB[id]
        else:
            return None

    def get_all_books(self):
        if self.__bookDB:
            return list(self.__bookDB.values())
        return []
    
    def update_book_info(self, id, new_title, new_author):
        book = self.get_book_info(id)
        if book:
            book.set_title(new_title)
            book.set_author(new_author)
            self.save_bookDB()
            return True
        return False

    def delete_book(self, id):
        if self.is_exist(id):
            del self.__bookDB[id]
            self.save_bookDB()
            return True
        return False
    
    def update_book_price(self, id, new_price):
        book = self.get_book_info(id)
        if book:
            book.set_price(new_price)
            self.save_bookDB()
            return True
        return False

    def update_book_info(self, id, new_title, new_author):
        book = self.get_book_info(id)
        if book:
            book.set_title(new_title)
            book.set_author(new_author)
            self.save_bookDB()
            return True
        return False

    def delete_book(self, id):
        if self.is_exist(id):
            del self.__bookDB[id]
            self.save_bookDB()
            return True
        return False


