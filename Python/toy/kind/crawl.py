import os
print(os.getcwd())
print(os.listdir(os.getcwd()))

# selenium 불러오기
from selenium import webdriver
import time


# chrome창(웹드라이버) 열기
driver = webdriver.Chrome("./chromedriver")

#kind 접속
driver.get("https://kind.krx.co.kr/corpgeneral/corpList.do?method=loadInitPage")

# 1초간
driver.implicitly_wait(1)


# 페이지 번호 copyed xpath
x = driver.find_element_by_xpath('//*[@id="main-contents"]/section[2]/div[1]')
divTag = driver.find_elements_by_css_selector("div em")
print(divTag[0].text)




