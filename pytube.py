# -*- coding: utf-8 -*-
"""
Created on Tue May 21 22:19:50 2019

@author: 김상민-Shark
"""

import pytube
import os
import subprocess

yt = pytube.YouTube("https://www.youtube.com/watch?v=nEZ_kh20yOc")
videos = yt.streams.all()

for i in range(len(videos)):
    print(i, ' : ', videos[i])
    

cNum = int(input("다운 받을 화질은?(0~21) : "))

down_dir = "D:\Youtube"

videos[cNum].download(down_dir)

newFileName = input("변환 할 mp3 파일명 : ")
oriFileName = videos[cNum].default_filename

subprocess.call(['ffmpeg', '-i',
     os.path.join(down_dir, oriFileName),
os.path.join(down_dir, newFileName)                
 ])

print("동영상 다운로드 및 mp3 변환 완료!")
