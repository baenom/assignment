class Test:
    def __init__(self, test_id, title, creator_id, price):
        self.__test_id = test_id          # 문제지 고유 고유번호 (자동 생성)
        self.__title = title              # 문제지 제목
        self.__creator_id = creator_id    # 출제자 ID
        self.__price = price              # 가격
        self.__question_ids = []          # 문제지에 포함된 문제 ID 리스트 (1:N 관계 매핑)

    def get_test_id(self): return self.__test_id
    def get_title(self): return self.__title
    def get_creator_id(self): return self.__creator_id
    def get_price(self): return self.__price
    def get_question_ids(self): return self.__question_ids

    def add_question_id(self, question_id):
        if question_id not in self.__question_ids:
            self.__question_ids.append(question_id)

    def __str__(self):
        return f'[{self.__test_id}] 제목: {self.__title} | 출제자: {self.__creator_id} | 가격: {self.__price:,}원'


class Question:
    def __init__(self, question_id, test_id, question_no, content):
        self.__question_id = question_id  # 문제 고유 고유번호
        self.__test_id = test_id          # 소속된 문제지 번호
        self.__question_no = question_no  # 문제 번호 (예: 1번, 2번)
        self.__content = content          # 문제 내용

    def get_question_id(self): return self.__question_id
    def get_test_id(self): return self.__test_id
    def get_question_no(self): return self.__question_no
    def get_content(self): return self.__content

    def __str__(self):
        return f' Q{self.__question_no}. {self.__content}'


class Answer:
    def __init__(self, question_id, solution):
        self.__question_id = question_id  # 매핑되는 문제 고유 고유번호
        self.__solution = solution        # 정답 및 해설 내용

    def get_question_id(self): return self.__question_id
    def get_solution(self): return self.__solution

    def __str__(self):
        return f' [정답/해설] {self.__solution}'