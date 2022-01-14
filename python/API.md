# API

## JASON

: JavaScript Object Notation

**데이터만을** 주고 받기 위한 표기법

파이썬의 Dictionary와 List 구조로 쉽게 변환하여 활용할 수 있다.

1. 정보가 있는 API URL을 확인한다
2. URL로 요청을 보낸다
3. 



* url 쪼개 보기
* https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=997
  * http : 
  * www.dhlottery.co.kr : 고유 주소
  * / common.do
  * ? :  뒤에 있는 요청 보낼 값을 같이 보내줘
    * ? key : value & key : value
    * method에 getLottoNumber랑 drwNo=997 을 넣어서 요청 보내줘	

* 서버 관련 에러코드

  ```javasc
  200 // [ OK ] 서버의 Request가 유효하고 성공한 경우
  301 // [ Moved Permanently ] 서버에서 리다이렉트(redirect) 페이지 이동 발생
  401 // [ Unauthorized ] 유효한 인증 정보를 가지지 않는 경우
  403 // [ Forbidden ] 인증이 실패한 경우
  405 // [ Methods Not Allowed ] 서버에 요청한 Methods가 유효하지 않는 경우
  503 // [ Service Unavailable]  서버가 요청을 받을 준비가 되지 않은 경우
  ```

  

### API 불러와서 파이썬에서 쓰기

```python
import requests

url = ''
response = requests.get(url).json()

```





https://www.metaweather.com/api/#locationsearch
