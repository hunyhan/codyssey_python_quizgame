# codyssey_python_quizgame

## 프로젝트 개요
터미널에서 실행하는 객관식 퀴즈 게임입니다. 퀴즈를 풀고, 새 퀴즈를 추가하고, 최고 점수를 확인할 수 있습니다. 퀴즈와 최고 점수는 `state.json` 파일에 저장되어 프로그램을 다시 실행해도 남아 있습니다.

- 언어: Python 3 (표준 라이브러리 `json`만 사용)
- 구조: `Quiz` 클래스(퀴즈 한 개), `QuizGame` 클래스(게임 전체)

## 퀴즈 주제와 선정 이유
- 주제: **개발 환경 기초** (터미널 명령, Docker, Git, Python 자료형)
- 이유: 한 번 공부했다고 계속 기억하는 것이 아니어서, 퀴즈를 만들며 한 번 더 복습하려고 골랐습니다. 같은 과정을 공부하는 동료들에게도 도움이 될 것 같습니다.

## 실행 방법
```bash
git clone https://github.com/hunyhan/codyssey_python_quizgame.git
cd codyssey_python_quizgame
python main.py
```
- Python 3.12에서 확인했습니다.
- 프로젝트 폴더에서 실행해야 `state.json`이 같은 폴더에 만들어집니다.

## 기능 목록
| 메뉴 | 기능 |
|---|---|
| 1. 퀴즈 풀기 | 등록된 퀴즈를 차례로 풀고 정답/오답을 알려 줍니다. 끝나면 `맞힌 개수/전체 (백분율)`을 보여 주고, 최고 점수보다 높으면 갱신합니다. |
| 2. 퀴즈 추가 | 문제, 선택지 4개, 정답 번호(1~4)를 입력받아 새 퀴즈를 추가하고 저장합니다. |
| 3. 퀴즈 목록 | 등록된 퀴즈 개수와 문제를 번호와 함께 보여 줍니다. |
| 4. 점수 확인 | 최고 점수를 보여 줍니다. 아직 풀지 않았으면 안내합니다. |
| 5. 종료 | 저장하고 프로그램을 끝냅니다. |

입력 처리
- 앞뒤 공백은 지우고 처리합니다. (` 3 ` → `3`)
- 빈 입력, 숫자가 아닌 입력, 범위 밖 숫자는 안내 후 다시 입력받습니다.
- `Ctrl+C`나 입력 끊김(EOF)이면 저장하고 안전하게 종료합니다.
- 퀴즈가 없을 때 풀기와 목록은 안내 후 메뉴로 돌아갑니다.

## 파일 구조
```
codyssey_python_quizgame/
├── main.py       # Quiz, QuizGame 클래스와 실행 코드
├── README.md
├── .gitignore    # state.json, __pycache__, .env 등 Git에서 제외
├── state.json    # 실행하면 생기는 데이터 파일 (Git에 올리지 않음)
└── docs/         # 수행 증거. 단계별 기록과 화면
    ├── 01~14 *.md
    └── images/   # 캡처 화면
```

## 데이터 파일 (state.json)
- 경로: 프로젝트 폴더의 `state.json` (UTF-8)
- 역할: 퀴즈 목록과 최고 점수를 저장해 다음 실행 때 불러옵니다.
- 저장 시점: 퀴즈를 추가했을 때, 최고 점수가 바뀌었을 때, 종료할 때
- 필드 구조

```json
{
  "quizzes": [
    {
      "question": "문제 글",
      "choices": ["선택지1", "선택지2", "선택지3", "선택지4"],
      "answer": 1
    }
  ],
  "best_score": 100.0
}
```

| 필드 | 뜻 |
|---|---|
| `quizzes` | 퀴즈 목록. 각 퀴즈는 `question`(문제), `choices`(선택지 4개), `answer`(정답 번호 1~4) |
| `best_score` | 최고 점수(%). 아직 안 풀었으면 `null` |

- 파일이 없으면(첫 실행) 기본 퀴즈 5개로 시작합니다.
- 파일이 손상됐으면 안내 후 기본 퀴즈로 복구하고 다시 저장합니다.

## 수행 체크리스트와 증거
각 링크에서 단계별 화면과 터미널 원문을 볼 수 있습니다.

| 완료 | 수행 항목 | 검증 방법 | 증거 |
|---|---|---|---|
| ✅ | 개발 환경 | Python 3.12.10, Git 2.54.0, VSCode Git Bash | [버전 확인](docs/14-final-run.md) · [개발 환경](docs/01-environment.md) |
| ✅ | 최종 실행 화면 | 메뉴, 퀴즈 추가, 목록, 풀기, 점수 | [최종 실행 화면](docs/14-final-run.md) |
| ✅ | 메뉴와 잘못된 입력 처리 | 빈 입력, 숫자 아님, 범위 밖 숫자 다시 묻기 | [메뉴 첫 작성](docs/04-first-drafts.md) · [메뉴 브랜치](docs/06-branch-merge.md) |
| ✅ | Quiz 클래스 | `__init__`, `check_answer`, `display_question` 실행 | [Quiz 클래스](docs/04-first-drafts.md) · [브랜치 병합](docs/06-branch-merge.md) |
| ✅ | 기본 퀴즈 5개 | `len(quiz_list)`가 5 | [과제 저장소](docs/05-new-repo.md) · [PR #1](docs/07-pull-request.md) |
| ✅ | 퀴즈 풀기 | 정답/오답 안내, 총 점수, 빈 목록 안내 | [퀴즈 풀기](docs/08-quiz-play.md) |
| ✅ | 퀴즈 추가 | 문제, 선택지 4개, 정답 번호 입력과 검사 | [퀴즈 추가](docs/09-quiz-add.md) |
| ✅ | 퀴즈 목록, 점수 확인 | 개수와 문제 출력, 최고 점수 갱신 | [목록과 점수](docs/10-quiz-list-score.md) |
| ✅ | QuizGame 클래스 | 메서드로 나눈 뒤 같은 동작, 공백 입력 처리 | [QuizGame 클래스](docs/11-quiz-game-class.md) |
| ✅ | state.json 저장/불러오기 | 다시 실행해도 유지, 손상 복구, `Ctrl+C` 저장 후 종료 | [state.json](docs/12-state-json.md) |
| ✅ | Git 명령 `init`, `add`, `commit`, `push` | 연습 저장소에서 처음부터 설정 | [연습 저장소](docs/02-practice-repo.md) |
| ✅ | Git 명령 `clone`, `checkout`, `merge`, `pull` | 과제 저장소 clone, 기능 브랜치, 병합 | [과제 저장소](docs/05-new-repo.md) · [브랜치와 병합](docs/06-branch-merge.md) |
| ✅ | Pull Request로 기능 합치기 | PR #1~#8, Merge 뒤 브랜치 정리 | [첫 PR](docs/07-pull-request.md) · [PR 화면](docs/08-quiz-play.md) |
| ✅ | 의미 있는 커밋 10개 이상 | `git log --oneline --graph` | [README PR와 그래프](docs/13-readme.md) |

## 개발 과정 기록
| 순서 | 페이지 | 내용 |
|---|---|---|
| 01 | [개발 환경](docs/01-environment.md) | Python 버전과 실행 위치 |
| 02 | [연습 저장소와 Git 기본 명령](docs/02-practice-repo.md) | `git init`, `remote add`, `.gitignore`, 첫 커밋과 푸시 |
| 03 | [Python 입력과 예외 처리 연습](docs/03-python-basics.md) | `input`, `int`, `ValueError`, `while`/`continue`/`break` |
| 04 | [메뉴와 Quiz 클래스 첫 작성](docs/04-first-drafts.md) | 메뉴 코드, `Quiz` 클래스 |
| 05 | [과제 저장소 만들기](docs/05-new-repo.md) | `git clone`, Python용 `.gitignore`, 기본 퀴즈 |
| 06 | [브랜치 만들기와 병합](docs/06-branch-merge.md) | `checkout`, Fast-forward, `--no-ff` |
| 07 | [첫 Pull Request와 브랜치 정리](docs/07-pull-request.md) | PR #1, 브랜치 삭제 |
| 08 | [퀴즈 풀기](docs/08-quiz-play.md) | PR #2, 다시 묻기 |
| 09 | [퀴즈 추가](docs/09-quiz-add.md) | PR #3, 입력 검사 순서 |
| 10 | [퀴즈 목록과 점수 확인](docs/10-quiz-list-score.md) | PR #4, #5 |
| 11 | [QuizGame 클래스로 구조 정리](docs/11-quiz-game-class.md) | PR #6, 리팩터링 |
| 12 | [state.json 저장/불러오기](docs/12-state-json.md) | PR #7 |
| 13 | [README 작성](docs/13-readme.md) | PR #8 |
| 14 | [최종 실행 화면](docs/14-final-run.md) | 개발 환경 버전, 메뉴·추가·목록·풀기·점수 |

## 트러블슈팅
| 문제 | 원인 | 해결 | 기록 |
|---|---|---|---|
| 퀴즈 목록에서 `(`가 닫히지 않았다는 오류 | 문자열 안에 같은 따옴표를 그대로 씀 | 바깥 따옴표를 바꿈 | [05](docs/05-new-repo.md) |
| 정답 입력이 틀려도 다시 묻지 않거나, 맞아도 또 물음 | `while`, `break`, 확인 줄의 들여쓰기 위치 | `break`를 `if`와 같은 칸, 확인 줄을 `for` 안으로 | [08](docs/08-quiz-play.md) |
| 빈 칸 입력이 "숫자를 입력"으로 안내됨 | 빈 칸 검사를 `int()` 뒤에 둠 | 입력 받기 → 빈 칸 검사 → `int()` 순서 | [09](docs/09-quiz-add.md) |
| 스페이스만 쳐도 입력이 통과함 | `input()`에 `.strip()`이 없음 | `input(message).strip()` | [11](docs/11-quiz-game-class.md) |
| `git branch -d`에서 "not yet merged to HEAD" 경고 | `git pull` 전에 브랜치를 지움 | `pull` → `branch -d` 순서 | [11](docs/11-quiz-game-class.md) |
| 종료해도 `state.json`이 생기지 않음 | 메뉴 5번에 `self.save()`가 빠짐 | 종료 전에 저장 | [12](docs/12-state-json.md) |
| 지운 원격 브랜치가 `git pull`에 다시 나옴 | PR 화면에서 Restore branch를 누름 | `git push origin --delete 브랜치` | [13](docs/13-readme.md) |
