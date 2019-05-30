import urllib.request as req
import json
from fake_useragent import UserAgent

ua = UserAgent()

headers = {
        'User-Agent' : ua.ie,
        'referer' : 'https://finance.daum.net/'
}

url = "https://finance.daum.net/api/search/ranks?limit=10"

res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')

rank_json = json.loads(res)['data']

for elm in rank_json:
    print('순위 : {}, 금액 : {}, 회사명 : {}'.format(elm['rank'], elm['tradePrice'], elm['name']), )
