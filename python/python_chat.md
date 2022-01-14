# python으로 챗봇 만들기

### python 기본 문법

* `=` : 할당한다
* `==` : 같다
* `ctrl + /` == 내가 지정한 영역 주석 처리



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




3.  반복

* While

  * ~ 하는 동안
  * 조건을 함께 제시

  * while에 해당하는 조건이 종료 될 때까지 **계속** 반복

  * **종료 조건이 반드시 필요**

    ```python
    while True:
        print('계속해주세요.')
    ```

    ```python
    n = 0
    while n < 3:
        print('출력')
        n = n + 1
    ```

    [결과]

    ```python
    출력
    출력
    출력
    ```

  

* for 

  * 정해진 박스내에서의 반복시 사용
  * 가지고 있는 모든 것을 꺼낸다

  * for 변수명 in 범위

    ```python
    dust = [59, 24, 102]
    for i in dust:
        print(i)
    ```

    [결과]

    ```python
    59
    24
    102
    ```

    

* 실습

  * while

    ```python
    count = 0
    while count <4:
        # 조건을 만족하는 동안
        # 아래 코드 실행
        count = count + 1
        print(greeting)
    ```

    (참고)

    ```python
    count = 0
    while count <4:
        print(greeting)
    # 종료 조건이 없으므로 계속 출력
    ```

  * for

    ```python
    # 정해진 범위 안에서 반복 실행
    # 범위는... 어디서 구하지?
    for i in range(4):
        print(greeting)
    ```





## Python 함수

1. Built-in Functions
2. Non-built-in-Functions



### python 내장함수

* import 는 해당 라인 이후로 활용할 코드를 가져오는 것이므로 
  **항상 최 상단에 작성**하도록 한다.
* 코드를 쓰다가 필요할 때 import!



1. Python Module - random

* 실습6 : random 모듈 활용

  * ramdom.choice

    ```python
    #1. 함수가 포함된 코드를 불러온다
    import random
    
    #2. 점심 메뉴 리스트를 만든다
    menu = ['맥도날드', '버거킹', '쉑쉑']
    ```

    

* 실습7 : random + 리스트

  * ramdon.sampe(리스트, 개수)

  * 리스트에서 특정 수의 요소를 임의적(ramdomly)으로 비복원추출(sample

    ```python
    # 1~45 중에 6개만 뽑아서 리스트에 담아서 출력
    # random 불러오기
    import random
    
    # 1~45 숫자 범위 만들기
    # range(시작값, 끝나는 지점(미포함), [step])
    # 리스트로 만들기 list()
    numbers = list(range(1,46))
    
    # 비복원 추출로 6개 뽑기
    lotto = random.sample(numbers, 6)
    print(lotto)
    ```

