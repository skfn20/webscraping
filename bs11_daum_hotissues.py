from bs4 import BeautifulSoup
import urllib.request as req

url ="https://www.daum.net/"
res = req.urlopen(url).read()
bsObj = BeautifulSoup(res, "html.parser")

hotIssue = bsObj.select("ol.list_hotissue.issue_row.list_mini")[0]

Issue_list = hotIssue.select("span.txt_issue > a")

for idx, issue in enumerate(Issue_list, 1):
   if 'href' in issue.attrs:
       print(idx, "위 : ", issue.string, "\n", issue.attrs['href']) 
