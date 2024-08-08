import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
url = 'https://section.cafe.naver.com/ca-fe/home'

req = requests.get(url)
print(req.text)
