from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "htmls.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

if __name__ == "main":
    title = getTitle("http://www.pythonscraping.com/pages/page1.html")
    
    if title == None:
        print("Title could not be found")
    else:
        print(title) 
