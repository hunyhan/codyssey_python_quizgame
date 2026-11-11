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

quiz_list = [
    Quiz("지금 위치가 /home/user/project 일 때 cd .. 을 실행하면 이동하는 곳은?", ["/", "/home/user", "/home", "/home/user/project"], 2),
    Quiz("Docker 이미지와 컨테이너의 관계로 옳은 것은?", ["컨테이너를 지우면 그 이미지도 함께 지워진다", "이미지는 지금 실행 중인 프로그램이다", "이미지 하나로 컨테이너를 여러 개 실행할 수 있다", "컨테이너는 이미지를 만들 때만 쓴다"], 3),
    Quiz("내 컴퓨터에서 바꾼 파일을 GitHub에 올리기까지의 순서로 옳은 것은?", ["push → add → commit", "commit → add → push", "add → push → commit", "add → commit → push"], 4),
    Quiz(".gitignore 파일의 역할로 옳은 것은?", ["Git이 추적하지 않을 파일 이름을 적어 둔다", "저장소에서 지울 파일 이름을 적어 둔다", "GitHub 로그인 정보를 저장한다", "커밋 메시지를 모아 둔다"], 1),
    Quiz('"age = input("나이: ")" 를 실행하고 20을 입력하면 age의 자료형은?', ["int", "float", "str", "bool"], 3)
    ]


while True:
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

    try:
        user_input = input("원하는 메뉴를 선택해 주세요: ")
        if user_input == "":
            print("입력이 없습니다. 다시 입력해 주세요.")
            continue
        n = int(user_input)

        if 1 <= n <= 5:
            if n == 1:
                print("1. 퀴즈 풀기")
                print("준비 중인 기능 입니다.")
            elif n == 2:
                print("2. 퀴즈 추가")
                print("준비 중인 기능 입니다.")
            elif n == 3:
                print("3. 퀴즈 목록")
                print("준비 중인 기능 입니다.")
            elif n == 4:
                print("4. 점수 확인")
                print("준비 중인 기능 입니다.")
            elif n == 5:
                print("5. 종료")
                print("프로그램을 종료합니다.")
                break
        else:
            print("1에서 5사이 숫자를 입력하세요.")

    except ValueError:
        print("숫자가 아닙니다. 다시 입력해 주세요.")