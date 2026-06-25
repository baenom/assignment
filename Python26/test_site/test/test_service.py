from test import Test, Question

class TestService:
    test_id_seq = 100001
    question_id_seq = 500001

    def __init__(self, test_dao, answer_service):
        self.__test_dao = test_dao
        self.__answer_service = answer_service
        
        # 시퀀스 변수가 파일 내부 최댓값을 추적하도록 초기화
        all_tests = self.__test_dao.select_all_tests()
        if all_tests:
            TestService.test_id_seq = max(t.get_test_id() for t in all_tests) + 1

    def create_test(self, title, creator_id, price, raw_questions_and_answers):
        """
        raw_questions_and_answers 예시: [("1번 문제 내용", "1번 정답"), ("2번 문제 내용", "2번 정답")]
        """
        test_id = TestService.test_id_seq
        TestService.test_id_seq += 1
        
        new_test = Test(test_id, title, creator_id, price)
        
        for idx, (content, answer_text) in enumerate(raw_questions_and_answers, start=1):
            q_id = TestService.question_id_seq
            TestService.question_id_seq += 1
            
            # Question 생성 및 추가
            question = Question(q_id, test_id, idx, content)
            self.__test_dao.insert_question(question)
            new_test.add_question_id(q_id)
            
            # 한 세트로 전달받은 Answer 등록 요청
            self.__answer_service.register_answer(q_id, answer_text)
            
        self.__test_dao.insert_test(new_test)
        return new_test

    def get_all_tests(self):
        return self.__test_dao.select_all_tests()

    def get_test_questions(self, test_id):
        """문제지의 '문제 리스트'만 순수하게 가공해 리턴합니다. (정답 제외)"""
        test = self.__test_dao.select_test_by_id(test_id)
        questions = []
        if test:
            for q_id in test.get_question_ids():
                q = self.__test_dao.select_question_by_id(q_id)
                if q: questions.append(q)
        return test, questions

    def delete_test(self, test_id):
        # 삭제 단계에서 연계된 정답 데이터 파일 청소도 트리거링
        test = self.__test_dao.select_test_by_id(test_id)
        if test:
            for q_id in test.get_question_ids():
                self.__answer_service.remove_answer(q_id)
            return self.__test_dao.delete_test(test_id)
        return False