# Chapter11 : 가상 선택자와 클래스



### 가상 선택자

웹 페이지에서 버튼을 누르면 해당 버튼의 색이나 모양이 변한다 버튼을 눌러도 아무런 변화가 없다면 버튼이 눌렸는지 안 눌렸는지 알 수 없을것이고

상태에 따라 변화를 주고 싶을 때 가상 선택자를 사용함

그리고  가상 선택자는 선택한 요소가 특벼한 상태여야 만족할 수 있다.



### 동적 가상 선택자

- active : 클릭시 활성화 되는 가상 클래스

```html
<style>
    a:active {
        color: red;
    }
</style>
```

- visited : 사용자가 이미 방문한 링크를 표시

```html
<style>
    a:visited {
        color: red;
    }
</style>
```

- disabled : 비활성화된 요소를 나타냄 말 그대로 요소를 비활성화

```html
<style>
    input:disabled {
        background: red;
    }
</style>
```

- hover : 가상 클래스는 마우스 커서를 요소에 올려놓았을 떄 선언한 스타일 실행 active가 클릭할 때 반응이라면 hover는 마우스를 올려놓았을 때 반응

```html
<style>
    a:hover {
        color: orange;
    }
</style>
```

- focus : input으로 만든 폼 등 집중(focus)을 받은 요소를 나타낸다. PC에서는 마우스 클릭이나 tab 키를 클릭할 때, 스마트폰에서는 탭을 했을 떄 발동

```html
<style>
    input:focus {
        color:red;
    }
</style>
```

