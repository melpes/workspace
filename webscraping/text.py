from datetime import datetime, timedelta
from logging import exception
import time

from selenium import webdriver

browser = webdriver.Chrome() # 괄호 속엔 위치

browser.get("https://www.youtube.com/watch?v=aN6P2N0r5qM&ab_channel=%EB%82%98%EB%8A%94%EB%B9%A1%EB%B9%A1%EC%9D%B4%EB%8B%A4")

today = datetime.today()

start = datetime(2021, 7, 9, 22, 00)

timedel = today - start
print(timedel)
day = datetime(1, 1, 1) + timedel
pp = day.strftime("%m 개월 %d 일 %H 시간 %M 분 %S 초")

browser.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer').click()

browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys("vegakangtaehui")
browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()

while True:
    try:
        browser.find_element_by_id('input').send_keys(f"시작일로부터 지난 시간 : {pp}")
        break
    except Exception:
        print("again")
        time.sleep(1)