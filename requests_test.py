'''
    * requests를 이용한 웹 크롤링
    : 정적 크롤링 -> 데이터를 가져올 페이지가 동적페이지라면 정적 크롤링을 이용해 얻은 데이터와 실제 데이터와 약간 다를 수 있다.
'''

import json
import requests

# get method는 데이터를 가져오는 명령어
data = requests.get("https://www.google.co.kr/")
print(data.text)

