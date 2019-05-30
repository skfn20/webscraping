# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:29:48 2019

@author: 김상민-Shark
"""

from bs4 import BeautifulSoup

html = """
<html><body>
<div id = "main">
    <h1>강의목록</h1>
    <ul class="lecs">
        <li>Java</li>
        <li>Python</li>
        <li>Python machine learning</li>
        <li>Android</li>
    </ul>
</div>
</body></html>
"""

bsObj = BeautifulSoup(html, "html.parser")
#select는 list값을 배열하므로 반환한 값에 .string을 할 수 없다.
h1 = bsObj.select("div#main > h1")
print('h1', h1)

h1 = bsObj.select_one("div#main > h1")
print('h1', h1)
#select_one은 하나의 값을 반환하므로 .string으로 문자열값을 받을 수 있다.
print(h1.string)

list_li = bsObj.select("div#main > ul.lecs > li")

for li in list_li:
    print(li.string)
    