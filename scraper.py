from selenium import webdriver
from bs4 import BeautifulSoup
from openpyxl import Workbook
import time

driver = webdriver.Chrome("./chromedriver")
result_list = []

# Chrome 으로 청와대 국민청원 페이지 get 후 html parsing
for page in range(1, 11):
    driver.get(f"https://www1.president.go.kr/petitions/best?page={page}")
    soup = BeautifulSoup(driver.page_source, "html.parser")

    for li in soup.select(
            "#cont_view > div.cs_area > div > div > div.board.text > div.b_list.category > div.bl_body > ul > li"):
        print(li.find("div", class_="bl_subject").text[3:].strip())
        result_list.append(li.find("div", class_="bl_subject").text[3:].strip())
    time.sleep(2)

# Chrome 종료
driver.close()

# 엑셀파일에 저장
write_workbook = Workbook()
write_cell = write_workbook.active

for i in range(1, len(result_list) + 1):
    write_cell.cell(i, 1, result_list[i - 1])

write_workbook.save("bluehouse.xlsx")
