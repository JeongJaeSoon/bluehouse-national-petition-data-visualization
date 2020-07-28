from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome("./chromedriver")

# Chrome 으로 청와대 국민청원 페이지 get 후 html parsing
for page in range(1, 11):
    driver.get(f"https://www1.president.go.kr/petitions/best?page={page}")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    result_list = []

    for li in soup.select(
            "#cont_view > div.cs_area > div > div > div.board.text > div.b_list.category > div.bl_body > ul > li"):
        print(li.find("div", class_="bl_subject").text[3:].strip())
        result_list.append(li.find("div", class_="bl_subject").text[3:].strip())
    time.sleep(5)

# Chrome 종료
driver.close()
