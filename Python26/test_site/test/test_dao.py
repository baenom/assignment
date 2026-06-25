import joblib
import os

class TestDAO:
    TEST_DB_FILE = './db/testDB.pkl'
    QUESTION_DB_FILE = './db/questionDB.pkl'

    def __init__(self):
        os.makedirs('./db', exist_ok=True)
        self.__testDB = self.__load_db(TestDAO.TEST_DB_FILE)
        self.__questionDB = self.__load_db(TestDAO.QUESTION_DB_FILE)

    def __load_db(self, file_path):
        try:
            return joblib.load(file_path)
        except FileNotFoundError:
            return {}

    def save_all(self):
        joblib.dump(self.__testDB, TestDAO.TEST_DB_FILE)
        joblib.dump(self.__questionDB, TestDAO.QUESTION_DB_FILE)

    def insert_test(self, test):
        if test.get_test_id() in self.__testDB:
            return False
        self.__testDB[test.get_test_id()] = test
        self.save_all()
        return True

    def insert_question(self, question):
        self.__questionDB[question.get_question_id()] = question
        self.save_all()
        return True

    def select_test_by_id(self, test_id):
        return self.__testDB.get(test_id, None)

    def select_question_by_id(self, question_id):
        return self.__questionDB.get(question_id, None)

    def select_all_tests(self):
        return list(self.__testDB.values())

    def delete_test(self, test_id):
        if test_id in self.__testDB:
            test = self.__testDB[test_id]
            # 해당 문제지에 묶여있던 문항 데이터도 정교하게 함께 삭제
            for q_id in test.get_question_ids():
                if q_id in self.__questionDB:
                    del self.__questionDB[q_id]
            del self.__testDB[test_id]
            self.save_all()
            return True
        return False