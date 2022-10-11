import requests
import re
from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone

n = datetime.now(timezone('Asia/Seoul')).weekday() #요일을 자동으로 불러옴

PROXY = {"https":'219.255.197.90:9000',
          "http": '219.255.197.90:9000'}

def getHtml(url):
    html = ""
    resp = requests.get(url,proxies=PROXY)
    if resp.status_code == 200:
        html = resp.text
    return html

if (n==6):
  num = 0
else:
  num = n + 1  #0월1화2수3목4금5토6일

URL = ("http://www.kyungsang.or.kr/user/carte/list.do?menuCd=MCD_000000000000014081")
html = getHtml(URL)
soup = BeautifulSoup(html, 'html.parser')
element = soup.find_all("tr")
element = element[4].find_all('td')

#쓸모없는 부분 정리하기
element = element[num] #num
element = str(element)
element = element.replace('[', '')
element = element.replace(']', '')
element = element.replace('<br/>', '\n')
element = element.replace('<td class="textC last">', '')
element = element.replace('<td class="textC">', '')
element = element.replace('</td>', '')
element = element.replace('(h)', '')
#element = element.replace('.', ',')
element = element.replace('<div class="meals_table_day">', '')
element = element.replace('<dl class="meals_table_day01">', '')
element = element.replace('<dd>', '')
element = element.replace('</dd>', '')
element = element.replace('</dl>', '')
element = element.replace('</div>', '')
element = element.replace("<td>", '')
element = element.replace("ㆍ", '')

element = re.sub(r'.*/dt>', '', element)


element = element.replace("\n\n\n\n", '')
element = element.replace("\n\n\n", '')


#print(element)

def dinner():
    if element == "":
        return "None"
    else:
        return element