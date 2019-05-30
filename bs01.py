# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:02:16 2019

@author: 김상민-Shark
"""

from urllib.parse import urljoin

baseUrl = "http://test.com/html/a.html"

print(">>", urljoin(baseUrl, "b.html"))
print(">>", urljoin(baseUrl, "sub/b.html"))
print(">>", urljoin(baseUrl, "../index.html"))
print(">>", urljoin(baseUrl, "../img/img.jpg"))
print(">>", urljoin(baseUrl, "../css/imgm/css"))