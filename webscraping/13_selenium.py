import time

from selenium import webdriver

browser = webdriver.Chrome() # 괄호 속엔 위치


browser.get("http://pixiv.net")


browser.find_element_by_class_name("signup-form__submit--login").click()

browser.find_element_by_xpath("//*[@id=\"LoginComponent\"]/form/div[1]/div[1]/input").send_keys("melpes")
browser.find_element_by_xpath("//*[@id=\"LoginComponent\"]/form/div[1]/div[2]/input").send_keys("kang2028")

browser.find_element_by_xpath("//*[@id=\"LoginComponent\"]/form/button").click()

while True:
    try:
        browser.find_element_by_xpath("//*[@id=\"root\"]/div[2]/div[2]/div[1]/div[1]/div/div[3]/div[1]/div[4]/div/button").click()
        break
    except Exception:
        time.sleep(1)


browser.find_element_by_xpath("/html/body/div[5]/div/div/div/div/ul/li[3]").click()

# 첫 번째 사진 클릭
while True:
    try:
        browser.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/section/div[3]/div/ul/li[1]/div/div[2]/a').click()
        break
    except Exception:
        print("일시 정지됨")
        time.sleep(1)


# 모두 보기
# browser.find_element_by_xpath("//*[@id=\"root\"]/div[2]/div[3]/div/div[1]/main/section/div[1]/div/div[4]/div/div[2]/button").click()


time.sleep(10)

browser.quit()