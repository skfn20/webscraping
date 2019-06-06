# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import  DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys
import datetime as dt
from urllib import parse
import re

def checkMaxDay(month, year):
    if month ==2:
        if year % 4 ==0 and year % 100 != 0:
            return 29
        else:
            return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31
 
    
def clean_text(text):
    cleaned_text = re.sub('[\n\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$&\\\=\(\'\"]',
                          '', text)
    cleaned_text = cleaned_text.strip()
    return cleaned_text

def findingNumofCommentsInTwits(opendate, searchTitle):
    binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
    browser = webdriver.Firefox(executable_path='D:/geckodriver.exe', firefox_binary=binary)
    
    date = opendate.split('-')
    
    day = 0
    month = 0
    year = 0
    
    if len(date) == 2:
        day = 1
        month = int(date[1])
        year = int(date[0])
    else:
        day = int(date[2])
        month = int(date[1])
        year = int(date[0])
         
    
    #setting the date 
    startdate = dt.date(year=year, month=month, day=day)
    
    if day + 5 < checkMaxDay(month, year):
        untildate = dt.date(year=year, month=month, day=day+1)
        enddate = dt.date(year=year, month=month, day=day+5)     
    elif month < 12:
        if day + 1 <= checkMaxDay(month, year):
            untildate = dt.date(year=year, month=month, day=day+1)
            enddate = dt.date(year=year, month=month+1, day = day - checkMaxDay(month, year) + 5)
        else:
            untildate = dt.date(year=year, month=month+1, day=day+1 - checkMaxDay(month, year))
            enddate = dt.date(year=year, month=month+1, day = day- checkMaxDay(month, year) + 5)
    elif month == 12:
        if day + 1 <= checkMaxDay(month, year):
            untildate = dt.date(year=year, month=month, day=day+1)
            enddate = dt.date(year=year+1, month=1, day = day - checkMaxDay(month, year) + 5)
        else:
            untildate = dt.date(year=year+1, month=1, day=day - checkMaxDay(month, year) +1)
            enddate = dt.date(year=year+1, month=1, day = day- checkMaxDay(month, year) + 5)
            
            
    
    query = {
            "q" : searchTitle
            }
    search = parse.urlencode(query, encoding='utf-8', doseq=True)
    
    totalfreq=[]
    while startdate < enddate:
        url= 'https://twitter.com/search?' + search + \
        '%20since%3A'+str(startdate)+ \
        '%20until%3A'+str(untildate)+'&src=typd'
        
        browser.get(url)
        html = browser.page_source
        soup= BeautifulSoup(html, 'html.parser')
        
        lastHeight = browser.execute_script("return document.body.scrollHeight")
        
        pageNumber = 0
        while pageNumber < 2:
            dailyfreq = {'Date' : startdate}
            wordfreq = 0
            reviews = [] 
            tweets = soup.find_all("p", {"class" : "TweetTextSize"})
            wordfreq += len(tweets)
            
            for tweet in tweets:
                reviews.append(clean_text(tweet.getText()))
            print(reviews)
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            
            newHeight = browser.execute_script("return document.body.scrollHeight")
            
            print(newHeight)
            if newHeight != lastHeight:
                html = browser.page_source
                soup = BeautifulSoup(html, 'html.parser')
                tweets = soup.find_all("p", {"class" : "TweetTextSize"})
                wordfreq = len(tweets)
                for tweet in tweets:
                    reviews.append(clean_text(tweet.getText()))
                print(reviews)
            else:
                dailyfreq['Frequency']=wordfreq
                dailyfreq['twit-reviews']=reviews
                wordfreq=0
                totalfreq.append(dailyfreq)
                startdate = untildate
                untildate += dt.timedelta(days=1)
                dailyfreq={}
                reviews = [] 
                break
            pageNumber +=1
            lastHeight = newHeight
    
    return totalfreq

if __name__ == '__main__':
    binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
    browser = webdriver.Firefox(executable_path='D:/geckodriver.exe', firefox_binary=binary)
    
    startdate = dt.date(year=2015, month=2, day=6)
    untildate = dt.date(year=2015, month=2, day=7)
    enddate=dt.date(year=2015, month=5, day=7)
    
    
    totalfreq=[]
    while not enddate==startdate:
        url= 'https://twitter.com/search?q=Blockchain%20since%3A'+str(startdate)+ \
        '%20until%3A'+str(untildate)+'&amp;amp;amp;amp;amp;amp;lang=eg'
            
        browser.get(url)
        html = browser.page_source
        soup= BeautifulSoup(html, 'html.parser')
            
        lastHeight = browser.execute_script("return document.body.scrollHeight")
            
        pageNumber = 0
        while pageNumber < 100:
            dailyfreq = {'Date' : startdate}
            wordfreq = 0
            tweets = soup.find_all("p", {"class" : "TweetSize"})
            wordfreq += len(tweets)
                
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
            
            newHeight = browser.execute_script("return document.body.scrollHeight")
                
            print(newHeight)
            if newHeight != lastHeight:
                html = browser.page_source
                soup = BeautifulSoup(html, 'html.parser')
                tweets = soup.find_all("p", {"class" : "TweetTextSize"})
                wordfreq = len(tweets)
            else:
                dailyfreq['Frequency']=wordfreq
                wordfreq = 0
                totalfreq.append(dailyfreq)
                startdate = untildate
                untildate += dt.timedelta(days=1)
                dailyfreq={}
                break
            pageNumber +=1
            lastHeight = newHeight
     
    print(totalfreq)