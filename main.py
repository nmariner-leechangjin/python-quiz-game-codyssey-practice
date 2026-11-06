def show_menu():
    print("자기주도 동료학습 코디세이 퀴즈 메뉴")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 퀴즈 확인")
    print("5. 종료")


def main():
    while True:
        show_menu()

        try:
            choice = input("메뉴 번호를 선택하세요: ").strip()

            if choice == "":
                print("입력값이 없습니다.")
            elif not choice.isdigit():
                print("숫자를 입력하세요.")
            elif int(choice) < 1 or int(choice) > 5:
                print("1에서 5 사이의 숫자를 입력하세요.")
            elif choice == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print(f"{choice}번 기능은 아직 준비 중입니다.")

        except (KeyboardInterrupt, EOFError):
            print("\n안전하게 종료합니다.")
            break


if __name__ == "__main__":
    main()