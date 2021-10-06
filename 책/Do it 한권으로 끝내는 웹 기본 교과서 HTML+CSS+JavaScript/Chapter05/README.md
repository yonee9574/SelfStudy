# Chapter05 : **입력 양식 작성하기**

### **폼**

웹사이트 정보를 보 낼 수 있는 요소는 모두 폼

### **기본 폼 태그 형식**

```HTML
<form [속성="속성값"]>여러 폼 요소</form>
```

### **input 태그의 type 속성**

![image-20210826222220990](https://user-images.githubusercontent.com/81904356/130972949-22be9e9f-0533-4af5-b892-c14c01526762.png)

### **토이 프로젝트를 하면서 기억에 남았던 태그 은근히 유용했던 태그**



```html
<input type="ID">
<input type="password">
```

```html
<button tpye="submit">내용</button>
<button tpye="reset">내용</button>
<button tpye="button">내용</button>
```

```html
<input type="ID" placeholder="아이디를 입력하세요">
```

```html
<input type=" " required>
```

```html
<textarea> 내용 </textarea> 
cols = 텍스트 영역의 가로 너비 문자 단위로 지정
rows = 텍스트 영역의 세로 길이를 줄 단위로 지정
```

## 공부하면서 중요하다고 생각한 태그

물론 자바스크립트로 확인하는 과정으로 조금 더 깔끔하고 정확하게 처리하고 표현할 수 있겠지만

html 로만 표현을 한다고 할때 필요할 꺼같은 태그

- readonly : 읽기 전용 form 상태로는 출력이 되지만 수정은 불가
- required : 필수 필드로 만드는것 필수 필드는 필요한 내용이 들어가야 하는 것 submit 을 했을 때 전송되는 값이 null 인 값을 방지할 수 도 있다.
