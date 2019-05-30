# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:20:51 2019

@author: 김상민-Shark
"""
from bs4 import BeautifulSoup

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
        <li><a href="http://www.google.com">google</a></li>
        <li><a href="http://www.tistory.com">tistory</a></li>
    </ul>
</body></html>
"""

bsObj = BeautifulSoup(html, "html.parser")

links = bsObj.find_all('a')
print('links', type(links))

for a in links:
    #print('a', type(a), a)       
    href = a.attrs['href']
    txt = a.string
    print('txt >> ', txt, ' href >> ', href)
    
#find_all, find에서 사용할 수 있는 제한 조건 
a = bsObj.find_all("a", string='daum')
print('a', a)

b = bsObj.find("a")
print('b', b)

c = bsObj.find_all('a', limit = 2) #제한을 걸어둘 수 있다.
print('c', c)

d = bsObj.find_all(string=['naver', 'google'])
print('d', d)
