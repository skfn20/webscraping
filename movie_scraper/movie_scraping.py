from bs4 import BeautifulSoup
from urllib import parse
import urllib.request as req
from urllib.parse import urlencode
import datetime 
import csv
import re
from twitercollect import findingNumofCommentsInTwits

#주어진 url로 beautifulsoup 객체를 만들어준다
def setbsObj(url):
    res = req.urlopen(url).read()
    bsObj = BeautifulSoup(res, "html.parser")
    
    return bsObj;

#네이버 영화에서 별점 정보를 뽑아오는 함수 
def getRatingInfo_Naver(bsObj):
    movieRatings = bsObj.select("div.star_score")
     #RatingList saves the all rating information
    #[관람객 평점, 기자평론가 평점, 네티즌 평점]
    RatingList = []
    
    #movie page에서 별점 정보를 뽑아온다. 
    for i, ratings in enumerate(movieRatings):
        #it saves the three information
        if i < 3:
            movieScore = ratings.select("em")
            Score = ""
            for rating in movieScore:
                Score += rating.string
            RatingList.append(Score)
    
    return RatingList

def clean_text(text):
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                          '', text)
    cleaned_text = cleaned_text.strip()
    return cleaned_text



def decodeSearch(searchTitle):
    query = {
            'query' : searchTitle
    }
    
    search = parse.urlencode(query, encoding='utf-8', doseq=True)
    
    return search

def getMoviepage_Naver(searchTitle):
    search = decodeSearch(searchTitle)
    
    baseUrl = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&"
    
    searchedPage = baseUrl + search
    
    bsObj = setbsObj(searchedPage)
    

    moviePage = bsObj.select_one("h3 > a").attrs['href']
    
    return moviePage

#네이버 영화에서 영화 정보를 list 자료형으로 반환해주는 함수 
def getMovieInfo_Naver(searchTitle):
    movieInfo = {}
    
    movieUrl = getMoviepage_Naver(searchTitle)
    bsObj = setbsObj(movieUrl)
    
    movieTitle = bsObj.select_one("h3.h_movie > a").string
    
    movieInfo['title'] = movieTitle
    
    RatingList = getRatingInfo_Naver(bsObj)
    
    movieInfo['rating'] = RatingList
    
    movieType = bsObj.select("dl.info_spec > dd")
    
    actor = []
    genre = []
    openday = []
    
    for i, Info in enumerate(movieType):
        for element in Info.select("a"):
            if i==0 and element.attrs['href'].startswith('/movie/sdb/browsing/bmovie.nhn?genre'):
                genre.append(element.string)
            elif i==1 and element.attrs['href'].startswith('/movie/bi/pi/basic'):
                movieInfo['director'] = element.string
            elif i==2 and element.attrs['href'].startswith('/movie/bi/pi/basic'):
                actor.append(element.string)
            elif i==3 and element.attrs['href'].startswith('/movie/sdb/browsing/bmovie.nhn?grade'):
                movieInfo['age'] = element.string.split('세')[0]
            elif element.attrs['href'].startswith('/movie/sdb/browsing/bmovie.nhn?open='):
                openday.append(element.string)
                
    if len(openday) >=2:      
        date = openday[1].replace('.', ' ').strip().replace(' ', '-')
        opendate = openday[0].strip() + '-' + date
    
    if opendate :
        movieInfo['opendate'] = opendate
        print("yes")
                
    movieInfo['actor'] = actor
    movieInfo['genre'] = genre
    
    for Info in movieType:
        for element in Info.select("p.count"):
            movieInfo['audience'] = element.getText().split("명")[0]
    
    reviews = naverMovieReview(searchTitle)
    
    movieInfo['reviews'] = reviews
    
    twit_num_comments = findingNumofCommentsInTwits(movieInfo['opendate'], searchTitle)

    movieInfo['twit_comments'] = twit_num_comments
    
    return movieInfo

def naverMovieReview(searchTitle):
    codeUrl = getMoviepage_Naver(searchTitle).split('?')[1]
     
    baseUrl = "https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?" + \
    codeUrl + "&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page="
    
    reviews = [] 
    
    for i in range(10):
        bsObj = setbsObj(baseUrl + str(i+1))
        movieReviews = bsObj.select(".score_reple > p")
        for review in movieReviews:
            reviews.append(clean_text(review.getText()))
            
    #이제 얻은 review에서 가장 많이 등장한 단어 10개를 뽑아서 reviews에 저장하고 movie_info에 저장해준다. 
    return reviews

def naverMovieRanking():
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date='
    dt = datetime.datetime.now()
    
    if dt.month < 10 : 
        month = "0" + str(dt.month)
    else:
        month = str(dt.month)
        
    if dt.day < 10:
        day = "0" + str(dt.day)
    else:
        day = str(dt.day)
        
    today =""+ str(dt.year) + str(month) + str(day)
    
    url = url + today
    
    bsObj = setbsObj(url)
    
    Ranking = bsObj.select("div.tit3 > a")
    
    movieRanking = []
    
    for element in Ranking:
        movieRanking.append(element.string)
        
    return movieRanking



if __name__ == '__main__':
    
   #movieData = []
    
   #movieRanking = naverMovieRanking()
    
   #for movie in movieRanking:
    #    movieData.append(getMovieInfo_Naver(movie))
    
   #print(movieData)
   
   movieInfo = getMovieInfo_Naver("기생충")
   print(movieInfo)
   
    
    
    
    
                