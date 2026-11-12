import json

STATE_FILE = "state.json"

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer

    def display_question(self):
        print(self.question)
        for i in range(len(self.choices)):
            print(f"{i + 1}. {self.choices[i]}")

    def to_dict(self):
        return {"question": self.question, "choices": self.choices, "answer": self.answer}


class QuizGame:
    def __init__(self):
        self.quiz_list = []   
        self.best_score = None
        self.load()

    def default_quizzes(self):
        return [
            Quiz("지금 위치가 /home/user/project 일 때 cd .. 을 실행하면 이동하는 곳은?", ["/", "/home/user", "/home", "/home/user/project"], 2),
            Quiz("Docker 이미지와 컨테이너의 관계로 옳은 것은?", ["컨테이너를 지우면 그 이미지도 함께 지워진다", "이미지는 지금 실행 중인 프로그램이다", "이미지 하나로 컨테이너를 여러 개 실행할 수 있다", "컨테이너는 이미지를 만들 때만 쓴다"], 3),
            Quiz("내 컴퓨터에서 바꾼 파일을 GitHub에 올리기까지의 순서로 옳은 것은?", ["push → add → commit", "commit → add → push", "add → push → commit", "add → commit → push"], 4),
            Quiz(".gitignore 파일의 역할로 옳은 것은?", ["Git이 추적하지 않을 파일 이름을 적어 둔다", "저장소에서 지울 파일 이름을 적어 둔다", "GitHub 로그인 정보를 저장한다", "커밋 메시지를 모아 둔다"], 1),
            Quiz('"age = input("나이: ")" 를 실행하고 20을 입력하면 age의 자료형은?', ["int", "float", "str", "bool"], 3)
        ]

    def load(self):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            quiz_list = []
            for q in data["quizzes"]:
                quiz_list.append(Quiz(q["question"], q["choices"], q["answer"]))
            self.quiz_list = quiz_list
            self.best_score = data["best_score"]
        except FileNotFoundError:
            print("저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
            self.quiz_list = self.default_quizzes()
            self.best_score = None
        except (ValueError, KeyError, TypeError):
            print("저장 파일이 손상되어 기본 퀴즈로 복구합니다.")
            self.quiz_list = self.default_quizzes()
            self.best_score = None
            self.save()
        except OSError:
            print("저장 파일을 읽을 수 없어 기본 퀴즈로 시작합니다.")
            self.quiz_list = self.default_quizzes()
            self.best_score = None

    def save(self):
        quizzes = []
        for quiz in self.quiz_list:
            quizzes.append(quiz.to_dict())
        data = {"quizzes": quizzes, "best_score": self.best_score}
        try:
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError:
            print("저장 중 오류가 발생했습니다. 이번 변경은 저장되지 않았습니다.")

    def input_text(self, message):
        while True:
            text = input(message).strip()
            if text == "":
                print("입력이 없습니다. 다시 입력해 주세요.")
                continue
            return text

    def input_number(self, message, low, high):
        while True:
            text = self.input_text(message)
            try:
                number = int(text)
            except ValueError:
                print("잘못된 입력 입니다. 숫자를 입력해 주세요.")
                continue
            if number < low or number > high:
                print(f"{low}~{high} 사이의 숫자를 입력해 주세요.")
                continue
            return number

    def show_menu(self):
        print("================================")
        print("Python Quiz Game")
        print("================================")
        print()
        print("메뉴를 선택해 주세요. 메뉴 번호를 입력해 주세요.")
        print()
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

    def play(self):
        if len(self.quiz_list) == 0:
            print("퀴즈가 없습니다. 퀴즈를 추가해 주세요.")
            return

        score = 0
        for quiz in self.quiz_list:
            quiz.display_question()
            user_answer = self.input_number("정답을 입력해 주세요 (1~4): ", 1, 4)
            if quiz.check_answer(user_answer):
                print("정답입니다!")
                score += 1
            else:
                print("틀렸습니다.")

        check_score = score / len(self.quiz_list) * 100
        print(f"총 점수: {score}/{len(self.quiz_list)} ({check_score:.2f}%)")
        if self.best_score is None or check_score > self.best_score:
            self.best_score = check_score
            self.save()
            print("최고 점수를 갱신했습니다!")

    def add_quiz(self):
        question = self.input_text("문제를 입력해 주세요: ")

        choices = []
        for i in range(4):
            choice = self.input_text(f"{i + 1}번 선택지를 입력해 주세요: ")
            choices.append(choice)

        answer = self.input_number("정답 번호를 입력해 주세요 (1~4): ", 1, 4)

        self.quiz_list.append(Quiz(question, choices, answer))
        self.save()
        print("퀴즈가 추가되었습니다.")

    def show_list(self):
        if len(self.quiz_list) == 0:
            print("등록된 퀴즈가 없습니다. 퀴즈를 추가해 주세요.")
            return

        print(f"등록된 퀴즈: {len(self.quiz_list)}개")
        for i in range(len(self.quiz_list)):
            print(f"{i + 1}. {self.quiz_list[i].question}")

    def show_score(self):
        if self.best_score is None:
            print("아직 퀴즈를 푼 기록이 없습니다. 먼저 퀴즈를 풀어 주세요.")
            return

        print(f"최고 점수: {self.best_score:.2f}%")

    def run(self):
        try:
            while True:
                self.show_menu()
                n = self.input_number("원하는 메뉴를 선택해 주세요: ", 1, 5)

                if n == 1:
                    print("1. 퀴즈 풀기")
                    self.play()
                elif n == 2:
                    print("2. 퀴즈 추가")
                    self.add_quiz()
                elif n == 3:
                    print("3. 퀴즈 목록")
                    self.show_list()
                elif n == 4:
                    print("4. 점수 확인")
                    self.show_score()
                elif n == 5:
                    print("5. 종료")
                    self.save()
                    print("프로그램을 종료합니다.")
                    break

        except (KeyboardInterrupt, EOFError):
            print()
            print("입력이 중단되었습니다. 저장하고 종료합니다.")
            self.save()


game = QuizGame()
game.run()
