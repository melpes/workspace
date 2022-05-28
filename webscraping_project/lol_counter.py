from selenium import webdriver
import time

your_champ = input("상대할 픽 : ")
browser = webdriver.Chrome()
browser.get("https://www.op.gg/champion/statistics")
time.sleep(3)

champs = browser.find_elements_by_css_selector()