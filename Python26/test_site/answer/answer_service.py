from Python26.test_site.main import Answer

class AnswerService:
    def __init__(self, answer_dao):
        self.__answer_dao = answer_dao

    def register_answer(self, question_id, solution):
        new_answer = Answer(question_id, solution)
        return self.__answer_dao.insert_answer(new_answer)

    def get_answer_by_question(self, question_id):
        return self.__answer_dao.select_answer_by_question_id(question_id)

    def remove_answer(self, question_id):
        self.__answer_dao.delete_answer_by_question_id(question_id)