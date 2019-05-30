# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:04:45 2019

@author: 김상민-Shark
"""

from bs4 import BeautifulSoup
import sys

html = """
<html>
<body>
    <h1>파이썬 BeautifulSoup 공부</h1>
    <p>태그 선택자</p>
    <p>CSS 선택자</p>
</body>
</html>
"""
print(html)

bsObj = BeautifulSoup(html, "html.parser")
print('bsObj', type(bsObj))

print('prettify', bsObj.prettify())

h1 = bsObj.html.body.h1
print(h1)
print(h1.string)

p1 = bsObj.html.body.p
print(p1)
p2 = p1.next_sibling.next_sibling
#enter, 즉 줄바꿈 문자도 next_sibling으로 인식하기 때문에 그냥 쓰면 출력 x
print('p2 : ', p2)
h1 = p1.previous_sibling.previous_sibling
print(h1)