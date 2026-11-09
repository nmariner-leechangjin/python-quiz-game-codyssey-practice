import json
from pathlib import Path
from quiz import Quiz
class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.best_score = 0
        self.state_file = Path("state.json")

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
           
    def add_quiz(self):
        print("\n===== 퀴즈 추가 =====")

        while True:
            question = input("문제를 입력하세요: ").strip()

            if question:
                break

            print("문제를 입력해야 합니다.")

        choices = []

        for number in range(1, 5):
            while True:
                choice = input(f"{number}번 선택지를 입력하세요: ").strip()

                if choice:
                    choices.append(choice)
                    break

                print("선택지를 입력해야 합니다.")

        while True:
            answer = input("정답 번호를 입력하세요(1~4): ").strip()

            if answer.isdigit() and 1 <= int(answer) <= 4:
                answer = int(answer)
                break

            print("1에서 4 사이의 숫자를 입력하세요.")

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        print("퀴즈가 추가되었습니다.")

    def list_quizzes(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print("\n===== 퀴즈 목록 =====")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"{number}. {quiz.question}")

    def save_state(self):
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score
        }

        try:
            with open(self.state_file, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)

            print("데이터를 저장했습니다.")

        except OSError:
            print("데이터 저장 중 오류가 발생했습니다.")

    def load_state(self):
        if not self.state_file.exists():
            return

        try:
            with open(self.state_file, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.quizzes = [
                Quiz.from_dict(item)
                for item in data["quizzes"]
            ]
            self.best_score = data.get("best_score", 0)

            print("저장된 데이터를 불러왔습니다.")

        except (OSError, json.JSONDecodeError, KeyError, TypeError):
            print("state.json이 손상되어 기본 데이터를 사용합니다.")            