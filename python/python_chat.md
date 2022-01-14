# python으로 챗봇 만들기

### python 기본 문법

* `=` : 할당한다
* `==` : 같다



### 1. 저장

* 컴퓨터는 무엇을 인식할 수 있나?

  * 숫자: 현실 세계에 존재하는 모든 **숫자**
  * 글자: 현실 세계에 존재하는 모든 **글자**, **따옴표 `''` `""`**
  * 참/거짓: True, False

  * 실습1

    * 변수 활용하기(hello.py)

      : 공손하게 여러번 인사하는 챗봇

    ```python
    # 변수라는 개념
    dust = 60
    
    greeting = "Hello, World!""
    
    print(greeting)
    ```



#### 어떻게 저장하는가?

#### 변수

1. 변수(variable)

   : 저장된 값을 변경할 수 있는 박스

   * 숫자, 글자, 참거짓을 담을 수 있다.

   ```python
   dust = 50
   dust = 60
   print(dust)
   
   [결과]
   60
   ```

   * print(hello) : hello 변수에 담긴 내용을 출력
   * print('hello') : hello라는 글자를 출력

   

2. 리스트(List)

   : 박스의 리스트

   박스가 순서대로 여러 개가 붙어있는 형태

   ```python
   dust = [58, 40, 70]
   print(dust[1])
   
   [결과]
   40
   ```

* 실습2
  * 리스트 활용하기



3. 딕셔너리(dictionary)

   : 궁극의 박스 dictionary

   "견출지 붙인 박스들의 묶음"

   ```python
   {'문자열(언어)' : 값}
   ```
   
   ```python
   dust = {'서울' : '50', '부산' : '40'}
   
   print(dust)
   
   [결과]
   {'서울' : '50', '부산' : '40'}
   ```

* 실습 3
  * 딕셔너리 활용하기
  * 식당이름 + 전화번호 출력





#### 조건문

1. 조건 if/else

   ```python
   if dust > 50:
       print('50초과') 
   else:
   ^^^^print('50이하') # 앞의 탭/띄어쓰기 4회 매우 중요!**
   
   dust = 60
   [결과]
   50초과
   ```



2. if/elif/else

   : 다양한 조건문.

   ```python
   if dust > 150:
       print('매우나쁨')
   elif 80 < dust <= 150:
       print('나쁨')
   elif 30 < dust <= 80:
       print('보통')
   else:
       print('좋음')
   ```


* 실습 4

  : 미세먼지 정보 알리미

  * f - string

    : 하나의 문자열 안에 

    ```python
    print(f'{dust} 따옴표로 감싸서 사용한다.')
    print('{} 따옴표로 감싸서 사용한다.'.format(dust))
    ```

    



