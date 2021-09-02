# Chapter05 : HTML 특징 정복

## 태그의 부모 자식 관계

![image-20210902143134268](https://github.com/yonee9574/save-image-repo.git/img/image-20210902143134268.png)

웹페이지는 '트리구조' 로 구성되어 보인다.

트리구조는 하나 이상의 요소에 연결되는 데이터 구조 유형

```html
<ol>
    <li>Coffee</li>
    <li>Tea</li>
    <li>Milk</li>
</ol>
/* 예제 1 */
```

ol = 부모 / li = 자식
이 구조를 알아야 되는 이유 : 부모는 자식에게 영향을 주기 때문 

예제 1에서 coffee 지우면 Tea가 1번 Milk가 2번이 된다.

무엇이 중요한가 하면 태그가 1000개 이상 존재하면 항목을 지우고 모든 항목에서 순번 숫자를 일일이 바꿔야 한다면

여간 번거로운 일이 아닐것이다. 하지만 ol 태그는 자동으로 자식 태그에 순서대로 번호를 붙여주니 좋은것이다.

## 검색엔진

웹 사이트나 웹페이지 등을 검색해주는 시스템이나 프로그램 등을 통칭

## 검색엔진 동작 원리

사용자가 검색을 했을 때 원하는 결과를 빠르게 보여주려고 방대한 정보들을 미리 정리

이 과정을 자동으로 데이터베이스화 시키는 프로그램을 봇(bot) 또는 크롤러 (crawler) 라고 함

검색 엔진은 봇이 주기적으로 웹사이트들을 방문하여 쌓은 정보를 정리한 후, 데이터베이스에 저장

이 정보는 사용자가 검색할 때 결과를 빠르고 정확하게 보여주는데 사용

## ![image-20210902144836431](https://github.com/yonee9574/save-image-repo.git/img/image-20210902144836431.png)

## 검색 엔진 최적화

Search Engine Optimization 의 약자 SEO 라고도 부른다.

검색이 잘 되도록 설계하는 일을 말한다.

검색 엔진을 최적화 하는 두 가지 방법

- 메타 태그 : 검색 엔진에 정보를 제공할 목적의 태그
- 시맨틱 태그 : 웹 페이지 구조를 구성하는 태그

## 메타 태그

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" /> /* 1번 */
        <meta
              name="Description"
              content="Author: 임효성, Category: 책, Price 10,000원, Length: 784페이지"
              /> /* 2번 */
        <title>코딩의 ㅋ자도 모르는 코린이를 위한 코딩 입문서</title>
    </head>
</html>
```

/* 1번 */charset = utf-8 로 설정하면 모든 언어를 지원

/* 2번 */meta 태그에 이름과 요소를 작성해 웹 페이지를 설명

## 시맨틱 태그

시맨틱 태그에서 Semantic 에는 "의미론적인" 이란 뜻이 있다.

시맨틱 태그는 의미 있는 태그라고 해석하면 편하다.

검색 엔진은 HTML 코드만으로 의미를 인식해야 한다.

이때 시맨틱 태그 안의 요소(Semantic element)를 해석하게 된다.

시맨틱 요소로 구성된 웹 페이지는 검색 엔진에 문서 정보를 더 의미 있게 전달할 수 있고 검색 엔진 또한 시맨틱 요소를 

이용하여 정보를 더 효과적으로 불러오고 읽을 수 있습니다.

![image-20210902150441595](https://github.com/yonee9574/save-image-repo.git/img/image-20210902150441595.png)



- header : 소개 요소 또는 탐색 링크를 나타냄
- nav : 탐색 링크를 정의 주로 메뉴를 구현
- section : 본문 내용을 포함하는 공간
- article : 독립적인 요소 그 자체로 의미가 있어 독립적으로 배포할 수 있어야 한다.
- aside : 사이드바처럼 좌우에 위치하는 공간
- footer : 문서의 하단을 정의 보통 카테고리를 요약하거나 저작권을 명시하는 용도

section / article / aside 는 중앙에 위치한 만큼 요소를 보기 좋게 표현하는데 사용

이 영역에서 많이 사용하는 시멘틱 태그는 다음과 같음

- h1,h2,h3,h4,h5,h6

- ol , ul

- li

- p

- img

- table

- head

- body

- foot

- r, d

- form

- fieldset

- label

- input

- textarea

- a

  

