# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import re
import urllib.request
import json
from selenium import webdriver
import time
import sys

class Encode:
    def __init__(self, stdout, enc):
        self.stdout = stdout
        self.encoding = enc
    def write(self, s):
        self.stdout.write(s.encode(self.encoding))

#youtubeapi를 사용하여 구독자수, 총 비디오 수, 총 비디오 재생 수 순으로 리스트를 반환
# [0] : numSubs, [1] : numVideo, [2] : numViews
def getYoutubeAPIInfo(id):
    name = id
    baseUrl= "https://www.googleapis.com/youtube/v3/channels?part=statistics&id="

    keys="AIzaSyArix5Hip3vzJ37-lMxPGShAz71ON76fiA"

    url = baseUrl + name + "&key=" + keys

    print(url)

    data = urllib.request.urlopen(url).read()
    numSubs=json.loads(data)['items'][0]['statistics']['subscriberCount']
    numVideo= json.loads(data)['items'][0]['statistics']['videoCount']
    numViews = json.loads(data)['items'][0]['statistics']['viewCount']
    
    Info = []
    Info.append(int(numSubs))
    Info.append(int(numVideo))
    Info.append(int(numViews))
    
    return Info
 

#주어진 url값으로 BeautifulSoup 객체를 생성하여 반환해준다.
def setbsObj(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj

#생성된 bsObj값을 이용하여 youtube 메인페이지에 있는 채널들의 url값을
#중복되지 않게 list에 저장하여 반환해준다. 
def getChannelList(bsObj):
    channelList = []
    for link in bsObj.findAll("a", href=re.compile("^(/channel)")):
        if link.attrs['href'] is not None:
            temp = "https://www.youtube.com" + link.attrs['href']
            if temp not in channelList:
                #print(temp)
                channelList.append(temp)
    return channelList

#youtube channel명 크롤링
def getTitle(url):
    bsObj = setbsObj(url)
    title = bsObj.select_one("h1 > span > span> span >a").attrs['title']
    return title

def getVideoTitles(url):
    driver = webdriver.Chrome("D:/1_source/webscraping/chromedriver")
    driver.get(url)
    num_of_pagedowns = 20
    
    #body = driver.find_element_by_tag_name("body")
    #binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
    #browser = webdriver.Firefox(executable_path='D:/geckodriver.exe', firefox_binary=binary)
    #browser.get(url)
    time.sleep(2)
    
    height = 4000
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select("h3 > a")
    
    while num_of_pagedowns:
        #body.send_keys(Keys.PAGE_DOWN)
        driver.execute_script("window.scrollTo(0, " + str(height)+");")
        time.sleep(0.5)
        height += 10000
        print(height)
        num_of_pagedowns -= 1
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        #print(soup.select("h3>a"))
        titles = soup.select("h3 > a")
        
    
    
    titleList = []
    for title in titles:
        #print(title.get_text())
        titleList.append(title.get_text())
    driver.close()
    
    return titleList
    
    

def writeChannelInfo(url):
    csvFile = open("./data/youtube.csv", "a", encoding="utf-8")
    temp_link = url.split("/")
    temp_id = temp_link[len(temp_link)-1]
    temp_info = getYoutubeAPIInfo(temp_id)
    video_url = url + "/videos"
    
    titleList = getVideoTitles(video_url)

    flag = True
    for i in range(3):
        if temp_info[i] == 0:
                flag = False
                break

    if flag:
        temp_title = getTitle(url)
        temp_info.insert(0, temp_title)
        temp_string=""
		
        for i , info in enumerate(temp_info):
            temp_string = temp_string+str(info) +","
        csvFile.write(temp_string)
        temp_title =""
        for i, title in enumerate(titleList):
            if i == len(titleList) -1:
                temp_title = temp_title + title
                print(title+"\n")
                csvFile.write(title+"\n")
            else:
                temp_title = temp_title + title + ","
                print(title+",")
                csvFile.write(title+",")
        print("temp_title:", temp_title)
    csvFile.close()
    
def isBlank(myString):
    return not (myString and myString.strip())

if __name__ == '__main__':
    sys.stdout = Encode(sys.stdout, 'utf-8')

    writeChannelInfo("https://www.youtube.com/channel/UCBIoXzDldCnpbM_7uyG0_Tg")
        
    #print(bsObj.select("a.star-avatar"))
    #writeChannelInfo("https://www.youtube.com/channel/UC0TMdsyB2cpzDQ9BqdZjs4Q")
    
    
                    
    