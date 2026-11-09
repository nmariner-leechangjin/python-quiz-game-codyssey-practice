import json
import random
import shutil
from pathlib import Path

from quiz import Quiz


class QuizGame:
    def __init__(self, quizzes):
        self.default_quizzes = list(quizzes)
        self.quizzes = list(quizzes)
        self.best_score = 0
        self.has_played = False
        self.state_file = Path("state.json")
        self.backup_file = Path("state.backup.json")

    def play_quiz(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        score = 0
        shuffled_quizzes = self.quizzes.copy()
        random.shuffle(shuffled_quizzes)

        for number, quiz in enumerate(shuffled_quizzes, start=1):
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
        self.has_played = True

        if score > self.best_score:
            self.best_score = score
            print("최고 점수를 갱신했습니다.")

        self.save_state()

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

        self.quizzes.append(Quiz(question, choices, answer))
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
            "best_score": self.best_score,
            "has_played": self.has_played
        }

        try:
            if self.state_file.exists():
                shutil.copy2(self.state_file, self.backup_file)

            with open(self.state_file, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)

            print("데이터를 저장했습니다.")

        except OSError:
            print("데이터 저장 중 오류가 발생했습니다.")

    def load_state(self):
        if not self.state_file.exists():
            return

        try:
            data = self._read_state(self.state_file)
            self._apply_state(data)
            print("저장된 데이터를 불러왔습니다.")

        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("state.json이 손상되어 기본 데이터를 사용합니다.")
            self._reset_to_defaults()

            if self.backup_file.exists():
                try:
                    backup_data = self._read_state(self.backup_file)
                    self._apply_state(backup_data)
                    print("백업 데이터를 불러왔습니다.")
                except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError):
                    print("백업 데이터도 사용할 수 있어 기본 데이터를 사용합니다.")

    def show_score(self):
        print("\n===== 점수 확인 =====")

        if not self.has_played:
            print("아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"최고 점수: {self.best_score}/{len(self.quizzes)}")

    def _read_state(self, path):
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def _apply_state(self, data):
        quiz_data = data["quizzes"]

        if not isinstance(quiz_data, list):
            raise TypeError("quizzes는 목록이어야 합니다.")

        loaded_quizzes = [Quiz.from_dict(item) for item in quiz_data]

        if any(len(quiz.choices) != 4 for quiz in loaded_quizzes):
            raise ValueError("모든 퀴즈의 선택지는 4개여야 합니다.")

        self.quizzes = loaded_quizzes
        self.best_score = int(data.get("best_score", 0))
        self.has_played = bool(data.get("has_played", False))

    def _reset_to_defaults(self):
        self.quizzes = list(self.default_quizzes)
        self.best_score = 0
        self.has_played = False
