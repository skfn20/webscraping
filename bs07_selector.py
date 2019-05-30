# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:26:06 2019

@author: 김상민-Shark
"""

from bs4 import BeautifulSoup

def car_func(bsObj, selector):
    print("car_func", bsObj.select_one(selector).string)

cars = """
    <ul id ="cars">
        <li id="ge">Genesis</li>
        <li id="av">Avante</li>
        <li id="so">Sonata</li>
        <li id="gr">Grandeur</li>
        <li id="tu">Tucson</li>
    </ul>
"""

bsObj = BeautifulSoup(cars, "html.parser")
car_func(bsObj, '#gr')
car_func(bsObj, '#ge')
car_func(bsObj, "ul > li#gr")
car_func(bsObj, "ul#cars > li#tu")
car_func(bsObj, "li[id='gr']")

car_lambda = lambda q : print("car_lambda", bsObj.select_one(q).string)

car_lambda("#gr")