'''
1. requests > naver.com
2. respose > bs4
3. webbrowser
'''

import requests
from bs4 import BeautifulSoup as bs

import webbrowser 

url = "https://www.naver.com/"

response = requests.get(url).text

doc = bs(response,'html.parser') # html.parser >  받아올 형식

# . > class
# # > id를 가져옴
#result = doc.select_one('.ah_k').text # parsing ....
result = doc.select('.ah_k')
#print(result[0])
print(result)

#webbrowser.open(url)

search_url = "https://search.naver.com/search.naver?query="

#webcrawling

for i in range(5):
    webbrowser.open(search_url + result[i].text)
    # print(result[i].text) #text만 불러올때 





