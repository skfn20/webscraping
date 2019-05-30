# -*- coding: utf-8 -*-
"""
Created on Mon May 27 00:39:23 2019

@author: 김상민-Shark
"""

from urllib.parse import urljoin

baseUrl = "http://test/com/html/a.html"

print(">>", urljoin(baseUrl, "b.html"))
print(">>", urljoin(baseUrl, "sub/b.html"))
print(">>", urljoin(baseUrl, "../index.html"))

