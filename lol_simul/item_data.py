from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(15)

url = "https://namu.wiki/w/%EB%A6%AC%EA%B7%B8%20%EC%98%A4%EB%B8%8C%20%EB%A0%88%EC%A0%84%EB%93%9C/%EC%95%84%EC%9D%B4%ED%85%9C/%EC%8B%A0%ED%99%94"
driver.get(url)

stat_names = [
    "공격력", "체력", "스킬 가속", "모든 피해 흡혈", "공격 속도", "치명타 확률",
    "생명력 흡수", "물리 관통력", "주문력", "마나", "마법 관통력", "방어력", "마법 저항력",
    "기본 마나 재생"
]

item_index = [9, 10, 11, 12,
 14, 15, 16, 
 18, 19, 20, 
 22, 23, 24, 25, 26, 27, 28, 
 30, 31, 32, 
 34, 35, 36, 37, 38]

with open("lol_simul/item_stat.csv", "w", encoding="utf-8") as f:
    f.write("아이템,")
    for i in stat_names:
        f.write(i)
        print(i, end='')
        f.write(',')
        print(',', end='')
    f.write('\n')
    print('\n', end='')

    for i in range(len(item_index)):
        element = driver.find_element_by_xpath(f'//*[@id="cPBeQHzkh"]/div[2]/div/div/div/div/div/div/div[1]/div[3]/div/div[3]/div/div[15]/div/div/div/div/div/div/div[1]/div/h4[{i+1}]')
        index = element.text.find('(')
        print(element.text[7:index])
        f.write(element.text[7:index])
        f.write(',')
        element = driver.find_element_by_xpath(f'//*[@id="cPBeQHzkh"]/div[2]/div/div/div/div/div/div/div[1]/div[3]/div/div[3]/div/div[15]/div/div/div/div/div/div/div[1]/div/div[{item_index[i]}]/div[1]/table/tbody/tr[2]/td/div/span/ul/li[2]/div')
        parts = element.text.split(',')
        parts_dict = {}
        for j in parts:
            name, stat = j.split('+').strip()
            parts_dict[name] = stat

        for j in range(len(stat_names)):
            pass
            
        f.write('\n')

driver.close()