class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[{number}번 문제]")
            quiz.show()

            while True:
                answer = input("정답 번호를 입력하세요: ").strip()

                if answer == "":
                    print("입력값이 없습니다.")
                    continue

                if not answer.isdigit():
                    print("숫자를 입력하세요.")
                    continue

                answer = int(answer)

                if answer < 1 or answer > 4:
                    print("1에서 4 사이의 숫자를 입력하세요.")
                    continue

                break

            if quiz.is_correct(answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

        print(f"\n퀴즈가 끝났습니다. 점수: {score}/{len(self.quizzes)}")