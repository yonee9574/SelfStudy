# 깃 (Git)--



## 기초 개념--

내가 먼저 이해한 개념부터 나열하자 여러 사람들이 버전 관리를 손 쉽게 하기 위해 만든 시스템이다. 
소스를 수정할려면 클론이라는 과정이 필요한데 즉 모든 소스를 복사하고 
사용자의 컴퓨터로 받아오는것이다.



## Remote / Origin

Remote는 말 그대로 서버 자체 

Origin은 내가 깃을 사용할 때에는 어떤 리모트 서버에 변경 사항을 업로드 할 것인지 정해야 하는데 
반드시! 하나의 리모트 서버로만 사용할 수 있는 것이 아니기 때문에 내가 사용하는 리모트 서버의 이름을
정해줘야한다. 이때 주로 사용하는 관례적인 이름이 바로 Origin이다.

## Repository

저장소라는 뜻 리모트 서버 내에서 구분되는 **프로젝트 단위 정도**라고 생각

## Branch

독립된 작업을 진행하기 위한 작업 공간의 개념
깃을 맨처음 초기화를 하면 기본적으로 Master이라는 브랜치가 생성된다.
이 Master 브랜치는 메인 브랜치 역할을 한다.
그 후 거기서 작업을 한 후 나중에 다시 Master로 합치는것이다.

# **깃 업로드 방법**

토이프로젝트 하던 중 오류발견으로 수정점검중...

# 오류 해결 1



![image-20210828164930817](https://user-images.githubusercontent.com/81904356/131211420-05bc7250-2727-42ea-a13d-8b0d497a6a9e.png)

참고 자료
https://velog.io/@kimiszero/github-src-refspec-master-does-not-match-any-%ED%95%B4%EA%B2%B0%EB%B0%A9%EB%B2%95

방법은 총 2가지

![image-20210828165126094](https://user-images.githubusercontent.com/81904356/131211435-63dff700-6ba9-4f97-8fe4-49ee2efc6308.png)


![image-20210828165135202](https://user-images.githubusercontent.com/81904356/131211436-71346d38-5403-41aa-b811-4e8397332fe6.png)

나는 방법2가 맞았다.  즉 마스터 브런치가 존재하지 않아서 생긴문제 
없던 브런치로 업로드 할려니 당연히 오류가 발생함-

# 오류 해결 2

## main 과 " 다른 브렌치 " 가 merge 가 안될때

![image-20210830010305453](https://user-images.githubusercontent.com/81904356/131257622-49e78a75-d058-4959-a1c0-c9f3a4f94cea.png)


![image-20210830010322213](https://user-images.githubusercontent.com/81904356/131257623-b6764c66-a898-46e2-aaa5-407b487369c1.png)

## 오류가 난 방법

1. 폴더 생성 후 파일 넣기
2. git bash 실행 및 cd [경로] 잡아주기
3. git status 입력 후 파일 상태 보기 Untracked files 확인
4. git add . 입력해 모든파일 (changes to be committed) 상태 만들어주기
5. git commit -m "설명"
6. repository 생성
7. git remote add "test" "repository url"
8. git push test master



-----------------------------------------------------------------------------------------------------------------------------

![image-20210830011734393](https://user-images.githubusercontent.com/81904356/131257624-8791ab5e-1b52-4874-b5b2-df38d502674f.png)

![image-20210830011723778](https://user-images.githubusercontent.com/81904356/131257628-30a89caf-3c68-4f88-8062-7dd4c0073124.png)

## 오류 해결 방법

1. epository 생성
2. git clone "repository url"
3. repository 폴더 안 파일 넣기
4. git status 로 확인
5. git add . 입력해 파일 커밋준비상태 만들어주기
6. git commit -m "설명"
7. git remote add "test" "repository url"
8. git push test master
