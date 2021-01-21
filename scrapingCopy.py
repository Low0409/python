import requests
from bs4 import BeautifulSoup

#URL = input("URLを入力してください")
f = open("C:\\Users\\81908\OneDrive\\デスクトップ\\test.txt","x",encoding="UTF-8")

url = "https://pad.gungho.jp/member/"
html = requests.get(url)
line = BeautifulSoup(html.content, "html.parser")



for line in line.find_all("li"):#指定したタグのすべてを
    f.write(line.text)

    #print(line.text)            #改行して表示