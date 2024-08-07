import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = '유산균'

url = base_url + keyword
req = requests.get(url, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")
wrap = soup.select(".view_wrap")

for i in wrap:
    if not i.select_one('.spblog.ico_ad'):
        title = i.select(".title_link")
        author = i.select(".name")
        print(f"검색 키워드 : {keyword}")
        print(f"블로그 제목 : {title[0].text}")
        print(f"블로그 작성자 : {author[0].text} \n")
