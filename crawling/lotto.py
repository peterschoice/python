import random #내장모듈(파이썬 공식문서)
import json #내장모듈

import requests #외장모듈 => 설치해야 
from bs4 import BeautifulSoup as bs #외장모듀 => 설치해야 
# import webbrower


numbers = random.sample(range(1,46),6)
url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=836"
#json 형태의 자료는 dictionary와 같지만 동일하게 쓸 수 없어서 json 형태로 바꿔줘야 한다. 
print(numbers) 
response = requests.get(url)
print(type(response.text))

lotto = json.loads(response.text)
print(type(lotto))

print(lotto["drwtNo6"]) # key 값이 없을 때 에러 발생 => 쓰지 마라
print(lotto.get("drwtNo6")) # 위에 거와 동일 

winner = []

for i in range(1,7):# 1부터 7 앞까지 데이타를 뽑겠다. 
    winner.append(lotto.get(f"drwtNo{i}"))

print(winner)
print(type(winner))

#python 함수

def pickLotto():
    picked = sorted(random.sample(range(1,46), 6))
    matched = len(set(winner) & set(picked)) # 같은 숫자를 뽑는다. 
    # set 은 중복값 없애주고, 자료를 빠르게 찾는다. 

    if matched == 6:
        print("1등")
    elif matched == 5:
        print("3등")
    elif matched == 4:
        print("4등")
    elif matched == 3:
        print("5등")
    else:
        print("꽝")

pickLotto()

# numbers.sort(reverse=True)
# print(numbers)

# webbrower.open("http://search.naver.com")

# import requests
# response = requests.get("https://www.naver.com").text
# print(response)