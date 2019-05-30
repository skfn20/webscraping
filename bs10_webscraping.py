from bs4 import BeautifulSoup
import urllib.request as req
#import urllib.parse as rep

url = "https://www.inflearn.com/"
res = req.urlopen(url).read()
#quote = res.quote_plus("추천-강좌")
#이렇게 하면 한글을 유니코드로 변환을 시켜서 url에 추가시켜줄 수 있다.
bsObj = BeautifulSoup(res, "html.parser")

recommends = bsObj.select("div.course_title")

for i, recommend in enumerate(recommends):
    print(i, "--------------------------------")
    print(recommend.getText())
    
