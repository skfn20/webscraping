from bs4 import BeautifulSoup
import urllib.request as req

url ="https://finance.naver.com/sise/"
res = req.urlopen(url).read()
bsObj = BeautifulSoup(res, "html.parser")

top4 = bsObj.select("table#siselist_tab_0 > tr")

i = 1
for e in top4:
    if e.find("a") is not None:
        print(i, e.select_one(".tltle").string) #tr tag안에 a tag 
        i += 1
