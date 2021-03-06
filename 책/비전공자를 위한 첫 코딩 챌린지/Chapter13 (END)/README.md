# Chapter13 : 깃/깃허브 배우기



### 깃 이란?

문서나 소스 코드 같은 파일의 변경 이력을 관리해주는 시스템

파일 내용을 수정,저장 해도 필요하면 수정 전 내용을 언제든 다시 확인하거나 복원할 수 있다.

이런 시스템을 "버전 관리 시스템 ( Version - control system)" 이라고 함



### 버전 관리 시스템이 필요한 이유

아주 간단한 예로 버전 업그레이드를 하다가 오류가 발생하여 이전 버전으로 되돌려야 하는 상황이 있으면 깃을 사용하게 된다면

코드를 이전 상태로 되돌릴 뿐만 아니라 시간 경과에 따른 변경 사항을 비교하고, 문제를 일으킨 항목을 마지막으로 수정한 사람, 시기 등을 확인할 수 있다.



- 깃은 저장소에 등록된 코드에 발생한 모든 수정 사항을 추적할 수 있음
- 빠르고 편리하게 작업을 할 수 있게 만들어줌 
- 협업 및 혼자 개발할 때에도 개발 시간을 줄이고 깃허브 등으로 배포하는 데 도움



### 깃허브가 필요한 이유

우리가 만든 코드를 저장을 항상 한다 이유는 간단하다 코드를 날리면 안되기 때문이다.

혼자 작업할 때 자신의 PC에 코드를 저장을 해도 되지만 협업할 때 팀원들이 코드를 각자의 PC에 따로따로 관리하면 서로의 코드를 확인하기 어렵다.

이럴 때 깃허브를 공동 저장소를 사용하면 유용하다



### 다른 깃과 깃허브의 차이

깃허브는 SaaS(싸스) 형태로 제공

SaaS는 서비스 소프트웨어 ( Software as a Service )를 의미

가장 완성된 형태의 클라우드 서비스로, 소프트웨어 형태로 서비스를 제공 / 대표적인 예 : 구글 드라이브 , 네이버 N드라이브 Saas에 해당하는 서비스



깃은 코드 버전관리 소프트웨어 / 깃허브는 깃 소프트웨어를 기반으로 구축된 클라우드 플랫폼 

결론 -> 깃을 웹에서 더 쉽게 사용할 수 있도록 만든 것이 깃허브



### 깃 / 깃허브 핵심 개념

- Repositoried ( 저장소 ) : 저장하는 공간을 의미 / 저장소에 폴더 및 모든 유형의 파일 (HTML  , CSS , Javascript , 문서, 데이터 , 이미지) 을 저장 할 수 있다.

- Branch ( 브렌치 ) : 나무가지 라는 의미 처럼 여러 갈래로 버전을 분기 및 통합하며 개발하는 데 사용 

  ##### 여러 버전이 생기는 이유 

  간단한 예로 처음에 한 개발자가 저장소를 만들었다고 가정을 하면 이후 다른 개발자들까지 각각 맡은 기능을 구현해 웹 서비스를 하기로 했다 근데 거기서 저장소를 각 개발자가 브렌치로 분기하여 기능을 구현하고 중간중간 각자 개발한 기능을 병합하여 전체 서비스가 원활하게 돌아가도록 확인 하는데 이떄 처음 저장소를 main branch , 각 개발자가 분기한 소스를 sub branch라고 함

  - sub branch 는 main branch 에 병합하기 전까지 sub branch에 수정한 내용은 main branch 에 영향을 주지 않음 ( 사용자가 웹 페이지를 이용 중인데 수정 중인 화면을 보여주면 안 되기 때문 )

- Clone ( 클론 ) : 깃허브 저장소에 있는 파일들을 로컬 컴퓨터로 복사본을 만드는 작업 (깃허브에서 생성한 저장소에 있는 파일은 배포된 파일)

  ​						클론은 파일을 받는 과정 

### add -> commit -> push

커밋과정은 add ( 추가 )  -> commit ( 저지르고 ) -> push( 밀어 ) 마무리



### Pull

"당기다" 라는 의미 깃허브 저장소에 있는 파일을 가져오는 작업



### clone 과 pull 의 차이

clone은 처음 코드를 다운로드할 때 사용 ( clone을 하게 되면 자동으로 깃허브에 있는 main 브렌치의 변경 내용을 추적 )

pull은 그 이후 사용 ( pull은 변경 내용만 내려받을 수 있다. )

**최종적으로**

클론 후 다른 PC에서 커밋한 코드를 자신의 PC에서 불러오려면 클론이 아닌 풀을 해야한다
