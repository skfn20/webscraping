from bs4 import BeautifulSoup

fp = open("food-list.html", encoding="utf-8")

bsObj = BeautifulSoup(fp, "html.parser")

print("1) ", bsObj.select_one("li:nth-of-type(4)"))
print("2) ", bsObj.select_one("#ac-list > li:nth-of-type(4)").string)
print("3) ", bsObj.select("#ac-list > li[data-lo='cn']")[0].string)
print("4) ", bsObj.select("#ac-list > li.alcohol.high")[0].string)

#dictonary 형태의 자료형을 전달인수 값으로 넘겨줄 수 있다.     
param = {"data-lo":"cn", "class":"alcohol"}

print("5) ", bsObj.find("li", param).string)
print("6) ", bsObj.find(id="ac-list").find("li", param).string)

for ac in bsObj.find_all("li"):
    if ac['data-lo'] == 'us':
        print('data-lo == us', ac.string)
