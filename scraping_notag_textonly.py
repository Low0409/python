
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.at-time.com/shop.html"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)



f = open("C:\\Users\\sisido\\Desktop\\Scraping\\test.txt","w",encoding="UTF-8")
f.write(text)

# print(text)