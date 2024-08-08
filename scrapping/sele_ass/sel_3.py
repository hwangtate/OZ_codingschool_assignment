import time
from selenium import webdriver
from bs4 import BeautifulSoup


header_user = {"User-Agent": "Mozilla/5.0"}

base_url = 'https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query='
keyword = input('Enter keyword: ')

url = base_url + keyword

driver = webdriver.Chrome()
driver.get(url)

for i in range(6):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

wrap = soup.select(".view_wrap")

for i in wrap:
    if not i.select_one(".spblog.ico_ad"):
        title = i.select(".title_link")
        author = i.select(".name")
        print(keyword,title[0].text,author[0].text)
