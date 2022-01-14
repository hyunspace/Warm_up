# requests 불러오기
# 나이 예측 api 사용
# 특정 이름을 입력했을 때, 무작위 나이를 가져와서
# ~~의 나이는 ~~살 입니다. 라는 문자를 출력

#지현 버전
# import requests
# name = 'kim'
# url = 'https://api.agify.io/?name=' + name
# response = requests.get(url).json()

# print(response['age'])
# print(str(name) + '의 나이는 ' + str(response['age']) + '살 입니다.')


#선생님 버전

# requests 불러오기
import requests
# 나이 예측 api 사용
name = input('이름을 입력해주세요: ')
url = f'https://api.agify.io/?name={name}'
# 특정 이름을 입력 했을때, 무작위 나이를 가져와서
response = requests.get(url).json()

age = response['age']
# ~~의 나이는 ~~살 입니다. 라는 문자를 출력
print(f'{name}의 나이는 {age}살 입니다.')