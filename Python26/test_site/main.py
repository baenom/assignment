from member.member_dao import MemberDAO
from member.member_service import MemberService
from test.test_dao import TestDAO
from answer.answer_dao import AnswerDAO
from answer.answer_service import AnswerService
from test.test_service import TestService
from member import Member

class TestPlatform:
    def __init__(self):
        self.m_dao = MemberDAO()
        self.msv = MemberService(self.m_dao)
        
        self.a_dao = AnswerDAO()
        self.asv = AnswerService(self.a_dao)
        
        self.t_dao = TestDAO()
        self.tsv = TestService(self.t_dao, self.asv)

    def run_test(self):
        print("=== 1. 회원가입 및 로그인 테스트 ===")
        user_id, user_pw = "baenom", "pass123"
        if self.msv.join(Member(user_id, user_pw, "배의진")):
            print("회원가입 완료!")
        
        logged_in = self.msv.login(user_id, user_pw)
        if logged_in:
            print(f"로그인 성공: {logged_in.get_name()}님 환영합니다.")

        print("\n=== 2. 문제지 및 다중 문항 출제 테스트 ===")
        qa_package = [
            ("파이썬에서 리스트 뒤에 요소를 추가하는 함수는?", "append() 입니다."),
            ("잡립(joblib) 라이브러리의 주요 용도는?", "객체의 직렬화 및 로컬 저장을 통한 데이터 영속성 관리입니다.")
        ]
        
        new_test = self.tsv.create_test(
            title="의진이의 파이썬 알고리즘 모의고사",
            creator_id=self.msv.current_user.get_id(),
            price=5000,
            raw_questions_and_answers=qa_package
        )
        print(f"신규 문제지 등록 성공 -> {new_test}")

        print("\n=== 3. 문제지 리스트 조회 및 문항 표출 (정답 비공개) ===")
        all_tests = self.tsv.get_all_tests()
        for t in all_tests:
            print(t)
            test, q_list = self.tsv.get_test_questions(t.get_test_id())
            for q in q_list:
                print(q)  # 문제 내용만 출력됨

        print("\n=== 4. 정답 및 해설 분리 표출 테스트 ===")
        # 사용자가 문제를 다 풀었거나 구매를 확정한 상태라고 가정한 뒤 정답을 별도로 가져옴
        print(f"--- '{test.get_title()}' 의 정답 및 해설지 조회 ---")
        for q in q_list:
            print(f"문항 번호 [{q.get_question_no()}번]")
            answer = self.asv.get_answer_by_question(q.get_question_id())
            print(answer)

if __name__ == '__main__':
    platform = TestPlatform()
    platform.run_test()