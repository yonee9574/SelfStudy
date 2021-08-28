# 깃 (Git)



## 기초 개념

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

# 깃 업로드 방법



# 오류 해결법



![image-20210828164930817](https://user-images.githubusercontent.com/81904356/131211420-05bc7250-2727-42ea-a13d-8b0d497a6a9e.png)

참고 블로그
https://velog.io/@kimiszero/github-src-refspec-master-does-not-match-any-%ED%95%B4%EA%B2%B0%EB%B0%A9%EB%B2%95

방법은 총 2가지
![image-20210828165126094](https://user-images.githubusercontent.com/81904356/131211435-63dff700-6ba9-4f97-8fe4-49ee2efc6308.png)
![image-20210828165135202](https://user-images.githubusercontent.com/81904356/131211436-71346d38-5403-41aa-b811-4e8397332fe6.png)

나는 방법2가 맞았다.  즉 마스터 브런치가 존재하지 않아서 생긴문제 
없던 브런치로 업로드 할려니 당연히 오류가 발생함-



