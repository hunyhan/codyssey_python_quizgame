
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