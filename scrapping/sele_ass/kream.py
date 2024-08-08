from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

header_user = {"User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}

options = Options()
options.add_argument(f"User-Agent = {header_user['User_Agent']}")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome()
url = "https://kream.co.kr/"

driver.get(url)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.search_btn_box').click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.input_search.show_placeholder_on_focus').send_keys('슈프림')
driver.find_element(By.CSS_SELECTOR, '.input_search.show_placeholder_on_focus').send_keys(Keys.ENTER)
time.sleep(1)

for i in range(10):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

wrap = soup.find_all('a', {'class': 'item_inner'})

for i in wrap:
    product_name = i.select_one('.translated_name').text
    if '후드' in product_name:
        category = '상의'
        product_brand = i.select_one('.product_info_brand.brand').text
        product_name_hood = product_name
        product_price = i.select_one('.amount').text

        print(product_brand, product_name_hood, product_price)








