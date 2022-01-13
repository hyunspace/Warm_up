# branch

## git branch 명령어

#### 브랜치 `생성`, `삭제`, `조회` 

```bash
# 브랜치 조회
$ git branch

# 원격 저장소의 브랜치 목록 확인
$ git branch -r

# 브랜치 생성
$ git branch {brnach name}
# *이름 중복 안 됨

# 브랜치 삭제
# 병합된(수정내역을 합친) 후에 삭제 가능
$ git branch -d {branch name} 
# **주의** 병합되지 않은 브랜치 강제 삭제
$ git branch -D {branch name}
```



#### git switch

- 현재 브랜치에서 다른 브랜치로 `HEAD` 를 이동시키는 명령어
- `HEAD` : 현재 작업중인 브랜치를 가리키는 포인터

```bash
# 다른 브랜치로 이동
$ git switch {이동할 브랜치 이름}

# 브랜치를 새로 생성하고 동시에 이동
$ git switch -c {새로 생성하고 이동할 브랜치 이름}
```



- **주의사항**

  git switch 하기 전에 commit 하셨나요?



### git merge branch

* master에 없는, dev에만 있는 파일 dev.txt를 가지고 오려고 할 때! >> **master에서 dev의 파일을 가져와야 함**

```bash
$ git merge dev
```

* master와 dev를 합쳐서 새로운 버전 만드는 것 X
* 이전 버전에 있던 master를 fast forward(빨리 감기)를 통해 옮겨오는 것

