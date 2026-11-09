# 즐거운 코디세이 퀴즈 게임

## 프로젝트 개요

Python 기본 문법과 객체 지향 프로그래밍을 연습하기 위해 만든 콘솔 퀴즈 게임입니다.

사용자는 퀴즈를 풀고, 새로운 퀴즈를 추가하고, 퀴즈 목록과 최고 점수를 확인할 수 있습니다. 퀴즈와 점수는 `state.json`에 저장되어 프로그램을 다시 실행해도 유지됩니다.

## 퀴즈 주제 선정 이유

Python을 학습하면서 배운 자료형, 조건문, 반복문, 함수 등의 내용을 직접 문제로 만들어 복습하기 위해 Python 기초를 주제로 선정했습니다.

## 실행 방법

### 1. 저장소 복제

```powershell
git clone https://github.com/nmariner-leechangjin/python-quiz-game-codyssey-practice.git
```

### 2. 프로젝트 폴더로 이동

```powershell
cd python-quiz-game-codyssey-practice
```

### 3. 프로그램 실행

```powershell
python main.py
```

Python이 설치되어 있어야 합니다.

## 기능 목록

- 메뉴 출력
- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 목록 확인
- 최고 점수 확인
- 잘못된 입력 처리
- 빈 입력 처리
- 숫자가 아닌 입력 처리
- 허용 범위를 벗어난 숫자 처리
- `Ctrl+C` 및 `EOFError` 안전 종료
- 퀴즈 데이터 저장 및 불러오기
- 최고 점수 저장 및 불러오기
- 손상된 JSON 파일 예외 처리

## 파일 구조

```text
python-quiz-game-codyssey-practice/
├─ main.py
├─ quiz.py
├─ quiz_data.py
├─ quiz_game.py
├─ state.json
├─ README.md
└─ .gitignore
```

## 클래스 구조

### Quiz 클래스

`Quiz` 클래스는 개별 퀴즈를 관리합니다.

- 문제
- 선택지 4개
- 정답 번호
- 퀴즈 출력
- 정답 확인
- JSON 저장용 데이터 변환

### QuizGame 클래스

`QuizGame` 클래스는 게임 전체를 관리합니다.

- 메뉴 출력
- 퀴즈 풀기
- 퀴즈 추가
- 퀴즈 목록 확인
- 최고 점수 확인
- 데이터 저장
- 데이터 불러오기

## 데이터 파일 설명

`state.json`은 프로젝트 루트에 저장됩니다.

이 파일에는 사용자가 추가한 퀴즈와 최고 점수가 저장됩니다.

```json
{
  "quizzes": [
    {
      "question": "문제 내용",
      "choices": [
        "선택지 1",
        "선택지 2",
        "선택지 3",
        "선택지 4"
      ],
      "answer": 1
    }
  ],
  "best_score": 0,
  "has_played": false
}
```

- `quizzes`: 기본 퀴즈와 사용자가 추가한 퀴즈 목록
- `question`: 퀴즈 문제
- `choices`: 4개의 선택지
- `answer`: 정답 번호
- `best_score`: 최고 점수
- `has_played`: 사용자가 퀴즈를 풀었는지 여부

`state.json`이 없으면 기본 퀴즈 데이터를 사용합니다. JSON 파일이 손상되면 안내 메시지를 출력하고 기본 데이터를 사용합니다.

## Git 학습 기록

이 프로젝트를 기능별로 나누어 커밋하고 브랜치에서 작업했습니다.

- 저장소 초기화
- 첫 번째 커밋과 `push`
- 메뉴 기능 구현
- `Quiz` 클래스와 기본 퀴즈 작성
- 퀴즈 풀기 브랜치 생성 및 병합
- 퀴즈 추가 기능 브랜치 생성 및 병합
- 퀴즈 목록 기능 브랜치 생성 및 병합
- `state.json` 저장 기능 브랜치 생성 및 병합
- 점수 기능 브랜치 생성 및 병합
- README 작성
- `clone`과 `pull` 실습

## Git 명령어 학습

- `git init`: 로컬 Git 저장소를 생성합니다.
- `git add`: 변경 파일을 커밋 대상으로 등록합니다.
- `git commit`: 변경 내용을 Git 기록으로 저장합니다.
- `git push`: 로컬 커밋을 GitHub에 업로드합니다.
- `git pull`: GitHub의 최신 내용을 로컬로 가져옵니다.
- `git checkout`: 다른 브랜치로 이동합니다.
- `git checkout -b`: 새 브랜치를 만들고 이동합니다.
- `git clone`: GitHub 저장소를 새로운 로컬 폴더로 복제합니다.
- `git merge`: 다른 브랜치의 변경 내용을 현재 브랜치에 합칩니다.