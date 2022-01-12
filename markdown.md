### 마크다운

#### 마크다운 장점

1. 

#### 마크다운 단점

1. 표준이 없다
2. 처음 학습하는 코스트가 발생한다
3. HTML 모든 마크업 기능을 대신하지는 못한다.

#### 주의사항

1. 마크다운의 본질은 글에게 `역할`을 부여하는 것이다
2. 정해진 역할에 맞는 문법을 사용해야한다.
3. 예를 들어, **글씨의 크기를 키우고 싶다**는 이유로 내용에 제목에 해당하는 역할을 부여해서는 안된다.



# 마크다운 문법

'##' 샾 두개로 작성했습니다. `ctrl+1`



### 리스트 (목록)

1. 순서가 있는 목록(숫자로)

- 순서가 없는 목록 `-`
- 순서가 없는 목록 `*`
- `tab 키`를 사용해서 들여쓰기가 가능하다.
  			- `tab`으로 들여쓰기

   - `shift + tab`으로 들여쓰기 취소 가능
     1. 순서가 없는 목록 앞에 순서가 있는 목록 생성 가능



### 강조

1. **굵게**
   1. 드래그 + ctrl + b
   2. `** 내용 **``
   3. `__ 내용 __`

2. _기울임_
   1. `드래그 + ctrl + i`
   2. `_ 내용 _ `
   3. `* 내용 *`

3. ~~취소~~
   1. `~~ 내용 ~~`
   2. `Alt + Shift + 5`



### 코드 블럭

* 한 줄 코드인 `인라인 코드`와 여러 줄 코드인 블럭코드로 나눌 수 있다

1. 인라인 코드 : 백틱을 사용해서 코드를 감싸줍니다. `inline code`
2. 블럭 코드 : ```python 처럼 백틱을 3번 입력하고 코드의 종류를 작성.

​	print("hello")

```python
print("hello")
for i in range(10):
    print(i)
```

```html
<h1>
    심지어 자동완성도 해줌...
</h1>
```



### 링크

* 젤다 아닙니다.
* `[표시할 글자](이동할 주소)` 형태로 작성합니다.

​		[youtube](youtube.com)

* 이동하려고 할 때는 `ctrl + click`



### 이미지

* `![대체 텍스트](이미지 주소)`
* `대체 택스트`란 , 이미지가 정상적으로 로딩되지 않았을 때 표시 되는 문구.
* typora에는 이미지를 드래그 앤 드랍만으로도 적용시킬 수 있다.

![logo](C:\스타트캠프\싸피드라마\logo.png)

#### 주의사항

1. 이미지 업로드 전 저장하기

![logo](markdown.assets/logo.png)



### 표

* `|`  → 파이프라인

* `ctrl + t` 단축키로 작성( mac `option + cmmand + t` )

* 행을 늘릴 때는 (`ctrl + enter`)

  |      |      |      |
  | ---- | ---- | ---- |
  |      |      |      |
  |      |      |      |
  |      |      |      |



### 구분선

* `---` 하이픈 3개

---

---

---

`ctrl + /`


