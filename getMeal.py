import requests
import json
from datetime import datetime
import dinner

def today():
    month = str(format(datetime.today().strftime("%m")))
    date = str(format(datetime.today().strftime("%d")))
    return '?month='+month+'&date='+date

def getLunch(month=None,date=None):
    SchulList = ["elementary","middle","high"]
    SchulCode = "D100000257"
    if month is None:
        seeDate = today()
        url = 'https://schoolmenukr.ml/api/' + SchulList[2] + '/' + SchulCode + seeDate

    else:
        url = 'https://schoolmenukr.ml/api/'+ SchulList[2]+'/'+SchulCode+'?month='+str(month)+'&date='+str(date)


    response = requests.get(url)
    school_menu = json.loads(response.text)
    #print(school_menu["menu"][0]["lunch"]) #점심 메뉴 불러오기
    text = "\n".join(school_menu["menu"][0]["lunch"])
    if(text == ""):
        text = "오늘은 점심이 없네요 ㅠ_ㅠ"
    printLunch = "```"+ text +"\n```"
    return printLunch

def dateInfo():
    date=[str(format(datetime.today().strftime("%m"))),str(format(datetime.today().strftime("%d")))]
    info = "/".join(date)
    return str(info)

def getDinner():
    return dinner.dinner()

#석식은 dinner.py에서 불러옴
#print(dateInfo())
# print(getLunch(12,23))
