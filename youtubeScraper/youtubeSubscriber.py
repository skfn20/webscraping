import urllib.request
import json

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
    
    Info = {"numSubs" : int(numSubs), "numVideo" : int(numVideo), "numViews" : int(numViews)}
    
    return Info
    
if __name__ == '__main__':      
    name = "UCcn-6MiGdq4Sw1IWtENFEaA"
    
    YoutubeInfo = getYoutubeAPIInfo(name)
    print(YoutubeInfo)
