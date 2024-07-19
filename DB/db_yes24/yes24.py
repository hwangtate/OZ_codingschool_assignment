from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
ChromeDriverManager().install()

import pymysql
import pymysql.cursors
import re
from datetime import datetime

browser = webdriver.Chrome()

link_list = []

for i in range(1,4):
    print("=" * 10,f"현재 {i} 페이지 입니다.", "=" * 10)
    url = f'https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber={i}&pageSize=24'
    browser.get(url)

    datas = browser.find_elements(By.CLASS_NAME, 'gd_name')

    for i in datas:
        link = i.get_attribute('href')

        link_list.append(link)

    print(f"페이지가 끝났습니다.")


connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '1025',
    db = 'yes24',
    charset= 'utf8mb4',
    cursorclass= pymysql.cursors.DictCursor
)

with connection.cursor() as cursor:
    
    for link in link_list:

        browser.get(link)

        title = browser.find_element(By.CLASS_NAME, 'gd_name').text
        author = browser.find_element(By.CLASS_NAME, 'gd_auth').text
        publisher = browser.find_element(By.CLASS_NAME, 'gd_pub').text

        publishing = browser.find_element(By.CLASS_NAME, 'gd_date').text
        match = re.search(r'(\d+)년 (\d+)월 (\d+)일',  publishing)
        if match:
            year, month, day = match.groups()
            date_obj = datetime(int(year), int(month), int(day))
            publishing = date_obj.strftime("%Y-%m-%d")
        else:
            publishing = '2024-01-01'

        rating = browser.find_element(By.CLASS_NAME, 'yes_b').text.replace(',','')
        if rating == '':
            rating = None
        else:
            rating = float(rating)
            # rating 값이 범위를 초과하는 경우 처리
            if rating < -9.9 or rating > 99.9:
                print(f"Warning: Rating value {rating} is out of range. Adjusting to NULL.")
                rating = None

        try:
            review = browser.find_element(By.CLASS_NAME, 'txC_blue').text
            review = int(review.replace(",", ""))
        except:
            review = 0

        try:
            sales = browser.find_element(By.CLASS_NAME, 'gd_sellNum').text.split(' ')[2]
            sales = int(sales.replace(",", ""))
        except: 
            sales = 0
        
        try:
            price = browser.find_element(By.CLASS_NAME, 'yes_m').text[:-1]
            price = int(price.replace(",", ""))
        except:
            price = 0

        try:
            ranking = browser.find_element(By.CLASS_NAME, 'gd_best').find_element(By.TAG_NAME, 'a').text.split(' ')[-1].split('위')[0]
            ranking_weeks = browser.find_element(By.CLASS_NAME, 'gd_best').text.split(' | ')[1].split(' ')[2].split('주')[0]
            ranking = int(ranking)
            ranking_weeks = int(ranking_weeks)
        except:
            ranking = 0
            ranking_weeks = 0

        sql = """
        INSERT INTO Books(title, author, publisher, publishing, rating, review, sales, price, ranking, ranking_weeks)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (title, author, publisher, publishing, rating, review, sales, price, ranking, ranking_weeks))
        connection.commit()
        print("데이터를 입력했습니다.")

