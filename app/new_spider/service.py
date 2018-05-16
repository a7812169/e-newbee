from bs4 import BeautifulSoup
from flask import jsonify
import requests,re
from app import get_connection
def getNews():
    url='http://www.scuec.edu.cn/s/1/t/560/main.htm'
    content=requests.get(url).text
    soup=BeautifulSoup(content,'html.parser')
    news=soup.find(class_='cont_yaowen').find_all(name='a')
    zzz=[]
    def get_content(href=None):
        content = requests.get(href).text
        soup = BeautifulSoup(content, 'html.parser')
        text= soup.find(class_='single-header').find(name='p').get_text()
        time=re.search(r'发布时间.*',text).group()
        author=re.search(r'作者.*',text).group()
        content=soup.find(class_='single-content').find_all(name='p')
        o=''
        for i in content:
            text = i.text
            if i.img:
                img = '图略'
            else:
                img = ''
            o = str(o + text + img + "\n")

        return {"time":time,"author":author,"detail":o}
    for link in news:
        href=link.get('href')
        author=get_content(href)['author']
        time=get_content(href)['time']
        detial=get_content(href)['detail']
        title=link.get_text()
        total={"href":href,"author":author,"time":time,"title":title,"content":detial}
        zzz.append(total)
    return zzz