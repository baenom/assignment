import joblib
import os

class AnswerDAO:
    ANSWER_DB_FILE = './db/answerDB.pkl'

    def __init__(self):
        os.makedirs('./db', exist_ok=True)
        self.__answerDB = self.__load_answerDB()

    def __load_answerDB(self):
        try:
            return joblib.load(AnswerDAO.ANSWER_DB_FILE)
        except FileNotFoundError:
            return {}

    def save_answerDB(self):
        joblib.dump(self.__answerDB, AnswerDAO.ANSWER_DB_FILE)

    def insert_answer(self, answer):
        self.__answerDB[answer.get_question_id()] = answer
        self.save_answerDB()
        return True

    def select_answer_by_question_id(self, question_id):
        return self.__answerDB.get(question_id, None)
    
    def delete_answer_by_question_id(self, question_id):
        if question_id in self.__answerDB:
            del self.__answerDB[question_id]
            self.save_answerDB()