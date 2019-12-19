import requests
from bs4 import BeautifulSoup as bs

url = "https://finance.naver.com/marketindex"

response = requests.get(url).text

soup = bs(response,'html.parser')

exchange = soup.select_one(".market1 span.value")

print(f"현재 원달러 환율은 {exchange.text}원 입니다.")

# 파일 저장
with open('test.txt', 'w', encoding='utf-8') as f: # with 는 안에서만 사용하겠다. 
     f.write(f"현재 원달러 환율은 {exchange.text}원 입니다.")



