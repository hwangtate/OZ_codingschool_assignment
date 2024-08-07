import requests
from bs4 import BeautifulSoup

header_user = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"
req = requests.get(url,headers=header_user)
html = req.text
soup = BeautifulSoup(html,"html.parser")

movie = soup.select(".sect-movie-chart")

for item in movie:
    ranking = item.select(".rank")
    title = item.select(".title")
    rate = item.select(".percent")
    open = item.select(".txt-info")

    for rank, title, rate, open in zip(ranking, title, rate, open):
        print(rank.text)
        print(title.text)
        print(rate.text)
        print(open.text.strip())
