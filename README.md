# 즐거운 코디세이 퀴즈 게임

## 프로젝트 개요

Python 기본 문법과 객체 지향 프로그래밍을 연습하기 위해 만든 터미널 퀴즈 게임입니다. 사용자는 퀴즈를 풀고, 새 퀴즈를 추가하고, 퀴즈 목록과 최고 점수를 확인할 수 있습니다. 퀴즈와 점수는 프로젝트 루트의 `state.json`에 저장되어 프로그램을 다시 실행해도 유지됩니다.

## 퀴즈 주제 선정 이유

Python을 학습하면서 배운 자료형, 조건문, 반복문, 함수 등의 내용을 직접 문제로 만들어 복습하기 위해 Python 기초를 주제로 선정했습니다.

## 실행 방법

### 저장소 복제

```powershell
git clone https://github.com/nmariner-leechangjin/python-quiz-game-codyssey-practice.git
cd python-quiz-game-codyssey-practice
```

### 프로그램 실행

```powershell
python main.py
```

Python 3가 설치되어 있어야 합니다.

메뉴 예시:

```text
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
```

## 기능 목록

- 메뉴 출력과 번호 선택
- 퀴즈 랜덤 출제
- 퀴즈 풀기와 정답 판정
- 퀴즈 추가
- 퀴즈 목록 확인
- 최고 점수 확인과 갱신
- 빈 입력, 문자 입력, 범위를 벗어난 숫자 처리
- `Ctrl+C`와 `EOFError` 발생 시 저장 후 안전 종료
- UTF-8 JSON 저장 및 불러오기
- 손상된 `state.json`의 백업 복구 또는 기본 데이터 복구

## 파일 구조

```text
python-quiz-game-codyssey-practice/
├─ main.py
├─ quiz.py
├─ quiz_data.py
├─ quiz_game.py
├─ state.json
├─ README.md
├─ .gitignore
└─ docs/
   └─ screenshots/
```

## 클래스 구조와 책임

| 클래스 | 책임 |
|---|---|
| `Quiz` | 문제, 4개 선택지, 정답을 저장하고 출력·정답 확인·JSON 변환을 담당합니다. |
| `QuizGame` | 메뉴 기능에서 사용하는 퀴즈 목록, 게임 진행, 점수, 저장·불러오기를 담당합니다. |

클래스를 사용한 이유는 문제 하나의 데이터와 동작을 `Quiz`에 모으고, 게임 전체 흐름을 `QuizGame`에 모아 책임을 분리하기 위해서입니다. 함수만 사용하는 방식보다 객체의 상태(`quizzes`, `best_score`)와 관련 메서드를 함께 관리하기 쉽고, 기능별 수정과 테스트 범위를 좁힐 수 있습니다.

## 입력 처리와 데이터 저장을 분리한 이유

입력 처리는 `main.py`와 게임 메서드에서 담당하고, JSON 파일 입출력은 `QuizGame`의 `save_state()`와 `load_state()`가 담당합니다. 이렇게 분리하면 메뉴 흐름을 바꾸지 않고 저장 방식을 수정할 수 있고, 파일 오류를 한 곳에서 처리할 수 있어 테스트와 유지보수가 쉬워집니다.

## 데이터 파일 설명

`state.json`은 프로젝트 루트에 UTF-8 인코딩과 2칸 들여쓰기로 저장됩니다.

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
- `question`: 문제 문자열
- `choices`: 정확히 4개의 선택지
- `answer`: 1부터 4 사이의 정답 번호
- `best_score`: 최고 정답 수
- `has_played`: 한 번이라도 퀴즈를 풀었는지 나타내는 값

파일이 없으면 `quiz_data.py`의 기본 퀴즈를 사용합니다. 파일을 읽을 수 없거나 JSON 형식이 손상되면 기본 데이터를 준비하고, 유효한 `state.backup.json`이 있으면 백업 데이터를 먼저 복구합니다. 저장하기 전 기존 `state.json`은 `state.backup.json`으로 복사되며, 이 백업 파일은 `.gitignore`로 Git에 올리지 않습니다. 수동 초기화가 필요하면 `state.json`을 별도 이름으로 백업한 뒤 삭제하고 프로그램을 다시 실행하면 기본 상태로 시작할 수 있습니다.

## 성능과 확장 한계

현재 방식은 실행할 때 전체 퀴즈 목록을 JSON으로 읽고, 저장할 때 전체 목록을 다시 씁니다. 퀴즈 수가 적은 학습 프로젝트에는 단순하고 충분하지만, 데이터가 수천~수만 개로 커지면 파일 전체를 메모리에 올리고 매번 다시 쓰는 비용이 커집니다. 대규모 서비스로 확장할 때는 SQLite나 PostgreSQL 같은 데이터베이스, 검색용 인덱스, 페이지 단위 조회를 고려해야 합니다.

## 변경 영향 범위

| 변경 요구 | 수정할 파일·메서드 |
|---|---|
| 메뉴 항목 변경 | `main.py`의 `show_menu()`, `main()` |
| 문제 구조 변경 | `quiz.py`의 `Quiz`, `quiz_data.py`의 기본 데이터 |
| 퀴즈 진행 방식 변경 | `quiz_game.py`의 `play_quiz()` |
| 퀴즈 추가·목록 변경 | `quiz_game.py`의 `add_quiz()`, `list_quizzes()` |
| 점수 정책 변경 | `quiz_game.py`의 `play_quiz()`, `show_score()` |
| 저장 스키마 변경 | `Quiz.to_dict()`, `Quiz.from_dict()`, `save_state()`, `load_state()` |

## Git 브랜치 전략과 커밋 규칙

`main`은 병합이 끝난 안정 버전으로 유지하고, 기능은 `feature/기능명` 브랜치에서 작업한 뒤 Pull Request로 병합했습니다. 문서 작업은 `docs/기능명` 브랜치를 사용했습니다.

커밋 메시지는 `type: 짧은 영문 설명` 형식을 사용했습니다.

- `feat`: 기능 추가, 예: `feat: add quiz list feature`
- `docs`: README·증빙 문서 변경, 예: `docs: complete project README`
- `chore`: 저장소 초기 설정, 예: `chore: initialize repository`

최종 검증 전 `main`의 커밋 수는 20개였고, 아래 명령어로 10개 이상임을 확인했습니다. 이후 문서·백업 보완 커밋이 추가되어도 이 기준을 충족합니다.

```powershell
git rev-list --count main
git log --oneline --graph --decorate --all
```

## Clone과 Pull 실습 기록

- 별도 폴더 `python-quiz-game-codyssey-clone`에 저장소를 `clone`했습니다.
- 복제된 저장소의 README를 수정하고 `commit`과 `push`를 수행했습니다.
- 기존 작업 폴더에서 `pull`하여 원격 `main`의 변경 내용을 반영했습니다.
- 관련 화면 증빙은 `docs/screenshots/06_clone_success.png`, `07_clone_commit_push.png`, `08_pull_verified_getcontents.png`에 있습니다.

## 검증 증빙

`docs/screenshots/`에는 PR 병합, `state.json` 영속성, 최고 점수, clone·pull, README 병합, 손상된 JSON 복구를 확인한 화면이 저장되어 있습니다.

손상된 JSON 테스트에서는 오류를 숨기지 않고 사용자에게 안내한 뒤 백업 또는 기본 데이터를 사용하도록 확인했습니다.
