import sys
import io
import urllib.request as req
from urllib.parse import urlencode

API = "https://www.mois.go.kr/frt/bbs/type013/commonSelectBoardList.do"

values = {
    'bbsld' : 'BBSMSTR_000000000007'
}

print('before', values)

params = urlencode(values)
print('after', params)

url = API + "?" + params

print("요청 url: ", url)

reqData= req.urlopen(url).read().decode('utf-8')

print("출력 : " , reqData)
