# requests 불러오기
import requests

# requests 사용해서 로또 api에 데이터 요청
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=997'
response = requests.get(url).json()
# requests가 가지고 있는 get함수에 url을 집어 넣어서 결과물을 response에 넣을 건데
# 그 전에 json 함수를 써서 파이썬 문법으로 바꿔줘

# 요청 보내서 응답 받은 문서를 출력
# print(response)
# print(response['drwtNo6'])
# print(response['drwtNo5'])
# print(response['drwtNo4'])
# print(response['drwtNo3'])
# print(response['drwtNo2'])
# print(response['drwtNo1'])
# print(response['drwtNo 까지 똑같으니까 숫자를 변수로 하면 코드 중복 줄일 수 있다

# 요청 보내서 응답 받은 문서를 출력
print(response)
# 당첨 번호 정보를 리스트에 담아보자
winners = []
# 1~7까지 반복
for num in range(1, 7):
    print(response[f'drwtNo{num}'])
    # winners 리스트에 당첨번호 추가
    winners.append(response[f'drwtNo{num}'])
print(winners)
