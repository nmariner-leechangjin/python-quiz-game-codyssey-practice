from quiz_data import DEFAULT_QUIZZES
from quiz_game import QuizGame


def show_menu():
    print("\n===== 즐거운 코디세이 퀴즈... 짠! =====")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")


def main():
    quiz_game = QuizGame(DEFAULT_QUIZZES)

    while True:
        show_menu()

        try:
            choice = input("메뉴 번호를 선택하세요: ").strip()

            if choice == "":
                print("입력값이 없습니다.")
                continue

            if not choice.isdigit():
                print("숫자를 입력하세요.")
                continue

            choice = int(choice)

            if choice < 1 or choice > 5:
                print("1에서 5 사이의 숫자를 입력하세요.")
            elif choice == 1:
                quiz_game.play_quiz()
            elif choice == 5:
                print("프로그램을 종료합니다.")
                break
            else:
                print(f"{choice}번 기능은 아직 준비 중입니다.")

        except (KeyboardInterrupt, EOFError):
            print("\n안전하게 종료합니다.")
            break


if __name__ == "__main__":
    main()