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
