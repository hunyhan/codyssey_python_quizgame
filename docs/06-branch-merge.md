# 브랜치 만들기와 병합

[← README로 돌아가기](../README.md)

연습 폴더에서 브랜치를 바꾸면 폴더 내용이 바뀌는 것을 확인한 뒤, 과제 저장소에서 `feature/menu`(Fast-forward 병합)와 `feature/quiz-class`(`--no-ff` 병합)를 만들었습니다.

## 브랜치 연습: checkout과 merge

### 연습 폴더에서 브랜치 바꿔 보기

<details>
<summary>터미널 원문 (핵심 부분)</summary>

```text
[main (root-commit) 157a4be] a 추가
...
$ git checkout -b test
Switched to a new branch 'test'
...
[test 6196c29] b 추가
...
hyjyj@HJH MINGW64 ~/py_practice/branch_test (test)
$ ls
a.txt  b.txt

hyjyj@HJH MINGW64 ~/py_practice/branch_test (test)
$ git checkout main
Switched to branch 'main'

hyjyj@HJH MINGW64 ~/py_practice/branch_test (main)
$ ls
a.txt
```

</details>

![main 브랜치일 때 윈도우 탐색기의 branch_test 폴더. a.txt 1개 항목](images/34-branch-test-main-explorer.png)

*main 브랜치일 때 윈도우 탐색기의 branch_test 폴더. a.txt 1개 항목*

![test 브랜치일 때 같은 폴더. a.txt, b.txt 2개 항목](images/34-branch-test-test-explorer.png)

*test 브랜치일 때 같은 폴더. a.txt, b.txt 2개 항목*

### 보기만 하려면

![git checkout test 뒤 ls에 a.txt b.txt가 나온다](images/34-checkout-test-ls.png)

*git checkout test 뒤 ls에 a.txt b.txt가 나온다*

### 연습 폴더에서 병합하기

![git merge test 결과 Updating 157a4be..6196c29, Fast-forward, b.txt 추가. ls에 a.txt b.txt](images/34-merge-test-fast-forward.png)

*git merge test 결과 Updating 157a4be..6196c29, Fast-forward, b.txt 추가. ls에 a.txt b.txt*

![git log --oneline에 6196c29 (HEAD -> main, test) b 추가, 157a4be a 추가](images/34-merge-log-oneline.png)

*git log --oneline에 6196c29 (HEAD -> main, test) b 추가, 157a4be a 추가*

## 메뉴 기능 브랜치와 병합

### 브랜치 이름과 만들기 전 확인

![과제 저장소 폴더, 프롬프트 (main)](images/35-repo-prompt-main.png)

*과제 저장소 폴더, 프롬프트 (main)*

### feature/menu 브랜치 만들기

![git status에 Untracked files: main.py, git pull은 Already up to date, git checkout -b featuer/menu(오타), git branch에 * featuer/menu와 main](images/35-checkout-featuer-menu.png)

*git status에 Untracked files: main.py, git pull은 Already up to date, git checkout -b featuer/menu(오타), git branch에 * featuer/menu와 main*

### 브랜치 이름 고치기

![git branch -m feature/menu 뒤 프롬프트 (feature/menu), git branch에 * feature/menu와 main](images/35-branch-rename.png)

*git branch -m feature/menu 뒤 프롬프트 (feature/menu), git branch에 * feature/menu와 main*

### 메뉴 코드 다시 쓰기

![1, 2 입력 → 각 기능 준비 중 안내 뒤 메뉴 다시](images/35-menu-run-1-2.png)

*1, 2 입력 → 각 기능 준비 중 안내 뒤 메뉴 다시*

![3 입력 → 퀴즈 목록 준비 중](images/35-menu-run-3.png)

*3 입력 → 퀴즈 목록 준비 중*

![4 입력 → 점수 확인 준비 중, 5 입력 → 프로그램을 종료합니다.](images/35-menu-run-4-5.png)

*4 입력 → 점수 확인 준비 중, 5 입력 → 프로그램을 종료합니다.*

![그냥 Enter → 입력이 없습니다, abc → 숫자가 아닙니다](images/35-menu-run-empty-abc.png)

*그냥 Enter → 입력이 없습니다, abc → 숫자가 아닙니다*

![6, 0 → 1에서 5사이 숫자를 입력하세요.](images/35-menu-run-6-0.png)

*6, 0 → 1에서 5사이 숫자를 입력하세요.*

### feature/menu에서 커밋하기

![VSCode 에디터. main.py U ● 탭, 2번째 줄 while(True):, 맨 위 빈 줄 하나](images/35-menu-code-unsaved.webp)

*VSCode 에디터. main.py U ● 탭, 2번째 줄 while(True):, 맨 위 빈 줄 하나*

![c8122ab (HEAD -> feature/menu) Feat: 메뉴 출력과 입력, 예회 처리 구현, 394c45b (origin/main, origin/HEAD, main) Initial commit](images/35-menu-commit-log.png)

*c8122ab (HEAD -> feature/menu) Feat: 메뉴 출력과 입력, 예회 처리 구현, 394c45b (origin/main, origin/HEAD, main) Initial commit*

### 마지막 커밋 고치기

![amend 뒤 a643000 Feat: 메뉴 출력과 입력, 예외 처리 구현, working tree clean](images/35-commit-amend.png)

*amend 뒤 a643000 Feat: 메뉴 출력과 입력, 예외 처리 구현, working tree clean*

### main에 병합하고 올리기

![git merge feature/menu → Updating 394c45b..a643000 Fast-forward, push 결과 394c45b..a643000 main -> main](images/35-merge-push.png)

*git merge feature/menu → Updating 394c45b..a643000 Fast-forward, push 결과 394c45b..a643000 main -> main*

![push 뒤 a643000 (HEAD -> main, origin/main, origin/HEAD, feature/menu)](images/35-log-after-push.png)

*push 뒤 a643000 (HEAD -> main, origin/main, origin/HEAD, feature/menu)*

![GitHub 저장소에 main.py, 2 Commits, 1 Branch](images/35-github-main-py.png)

*GitHub 저장소에 main.py, 2 Commits, 1 Branch*

### 지금 그래프 확인하기

![git log --oneline --graph에 * a643000, * 394c45b 세로 한 줄](images/35-log-graph-linear.png)

*git log --oneline --graph에 * a643000, * 394c45b 세로 한 줄*

## Quiz 클래스 브랜치와 --no-ff 병합

### 브랜치 만들고 Quiz 클래스 다시 쓰기

![main.py 1~13번째 줄에 Quiz 클래스, 18~20번째 줄에 확인용 세 줄](images/36-quiz-class-with-test.webp)

*main.py 1~13번째 줄에 Quiz 클래스, 18~20번째 줄에 확인용 세 줄*

![확인용 실행: 1 + 1 = ?, 1. 1 ~ 4. 4, True False 뒤 메뉴](images/36-quiz-class-test-run.png)

*확인용 실행: 1 + 1 = ?, 1. 1 ~ 4. 4, True False 뒤 메뉴*

![확인용 세 줄을 지운 에디터. 탭이 main.py M ●](images/36-quiz-class-test-removed.webp)

*확인용 세 줄을 지운 에디터. 탭이 main.py M ●*

### 저장하고 커밋하기

![저장된 에디터(● 없음), git status에 modified: main.py, 커밋 1ae5f89 Feat: Quiz 클래스 추가 14 insertions, 그래프는 아직 한 줄](images/36-quiz-class-commit.webp)

*저장된 에디터(● 없음), git status에 modified: main.py, 커밋 1ae5f89 Feat: Quiz 클래스 추가 14 insertions, 그래프는 아직 한 줄*

### --no-ff로 합치고 그래프 보기

![Merge made by the 'ort' strategy, 그래프에 86e52cc Merge branch 'feature/quiz-class'와 갈라진 줄의 1ae5f89, push a643000..86e52cc main -> main](images/36-merge-no-ff-push.png)

*Merge made by the 'ort' strategy, 그래프에 86e52cc Merge branch 'feature/quiz-class'와 갈라진 줄의 1ae5f89, push a643000..86e52cc main -> main*

![push 뒤 86e52cc (HEAD -> main, origin/main, origin/HEAD), git status working tree clean](images/36-graph-after-push.png)

*push 뒤 86e52cc (HEAD -> main, origin/main, origin/HEAD), git status working tree clean*

![VSCode 하단 브랜치 main, 터미널에 같은 그래프](images/36-vscode-main-clean.webp)

*VSCode 하단 브랜치 main, 터미널에 같은 그래프*
