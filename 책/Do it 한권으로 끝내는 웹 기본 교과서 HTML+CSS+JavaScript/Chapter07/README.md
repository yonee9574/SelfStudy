# Chapter 07 : 텍스트를 표현하는 다양한 스타일

## 기본형 기호

1.  | 는 나열한 옵션 중 하나가 값이 되어야 한다.

```html
font-size: 값1 | 값2 | 값3
```

2.  속성값을 나열할 때 키워드(약속한 값)는 그대로 나열

```html
font-variant: normal | small-caps
```

3. 속성값을 나열할 때 값이 아니라 유형이라면 <> 로 묶는다.
   다른 속성을 유형처럼 쓸수 있다.

```html
font-size: <절대크기> | <상대크기> | <크기> | <n %>
```

```html
font: <font-style><font-variant><font-weight>
```

## 표 스타일

표 제목의 위치 

캡션은 기본적으로 표 위쪽에 표시된다.
caption-side 속성을 사용하면 표 아래쪽으로 옮길 수 있다.

```html
caption-size: top|bottom
```

## 표 테두리

표 테두리는 border 속성을 사용한다. 
표 바깥 테두리와 셀 테두리를 각각 지정할수 있다.

표 뿐만 아니라 html 레이아웃 구성이 어떻게 되있는지 궁금할때
스타일에 넣어 쓸때도 유용했다.
물론 바탕색을 넣어도 됐었다.

```html
<style><
table {
	caption-side: bottom; /* 표 캡션 위치 아래 */
	border: 1px solid black; /* 표 테두리는 검은색 실선으로 */
}

td, th{
    border: 1px dotted black; /* 셀 테두리는 검은색 점선으로 */
    padding: 10px;	/* 셀 테두리와 내용 사이의 여백 */
    text-align: center; /* 셀 내용 정렬 방법 */
    }
/style>
```

