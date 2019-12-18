import random #내장모듈(파이썬 공식문서)
import webbrower

numbers = random.sample(range(1,46),6)

print(numbers) 
numbers.sort(reverse=True)
print(numbers)

webbrower.open("http://search.naver.com")