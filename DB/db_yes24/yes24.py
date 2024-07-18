from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

ChromeDriverManager().install()

#3페이지까지의 데이터 제목 크롤링
browser = webdriver.Chrome()

link_list = []

for i in range(1,4):
    print("=" * 10,f"현재 {i} 페이지 입니다.", "=" * 10)
    url = f'https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber={i}&pageSize=24'
    browser.get(url)

    # browser.find_element(By.CLASS_NAME, 'gd_name').get_attribute('href')
    datas = browser.find_elements(By.CLASS_NAME, 'gd_name')

    for i in datas:
        # link = i.get_attribute('href')

        # link_list.append(link)
        print(i.text)

    print(f"페이지가 끝났습니다.")

# print(link_list)

