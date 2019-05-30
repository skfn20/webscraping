from bs4 import BeautifulSoup
import re #regex

html = """
<html><body>
    <ul>
        <li><a id='naver' href="http://www.naver.com">naver</a></li>
        <li><a href="https://www.daum.net">daum</a></li>
        <li><a href="https://www.google.com">google</a></li>
        <li><a href="http://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""

bsObj = BeautifulSoup(html, 'html.parser')

test = bsObj.find('a', string='naver')

li = bsObj.find_all(href=re.compile(r"^https://"))

for element in li:
    print(element.attrs['href'])
    
li = bsObj.find_all(href=re.compile(r"da"))
print(li)
