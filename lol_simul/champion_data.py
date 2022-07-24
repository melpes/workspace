from selenium import webdriver
import time
from urllib import parse

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(15)

driver.get("https://namu.wiki/w/%EB%A6%AC%EA%B7%B8%20%EC%98%A4%EB%B8%8C%20%EB%A0%88%EC%A0%84%EB%93%9C/%EC%B1%94%ED%94%BC%EC%96%B8")

hrefs = []
for i in range(2, 19):
    try:
        for j in range(1, 11):
            element = driver.find_element_by_xpath(f'//*[@id="IpEm6iVAz"]/div[2]/div/div/div/div/div/div/div[1]/div[3]/div/div[3]/div/div[15]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/dl/dd/div/div[{i}]/div[{j}]/a')
            hrefs.append(element.get_attribute("href"))
    except:
        break

driver.close()

stat_names = ["체력", "공격력", "공격 속도", "방어력", "마법 저항력"]

with open("lol_simul/champion_stat.csv", "w", encoding="utf-8") as f:
    f.write("챔피언,")
    for i in stat_names:
        f.write(i)
        print(i, end='')
        f.write(',')
        print(',', end='')
    f.write('\n')
    print('\n', end='')

    for v in hrefs:
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(15)
        while True:
            try:
                driver.get(v)
                break
            except:
                continue

        index = 0
        try:
            for i in range(5, 12):
                element = driver.find_element_by_xpath(f'//*[@id="IpEm6iVAz"]/div[2]/div/div/div/div/div/div/div[1]/div[3]/div/div[3]/div/div[15]/div/div/div/div/div/div/div[1]/div/div[{i}]')
                if element.text.find("라이엇 게임즈 제공 챔피언 능력치") != -1:
                    index = i
                    break
        except:
            driver.close()
            continue

        xpath = f'//*[@id="IpEm6iVAz"]/div[2]/div/div/div/div/div/div/div[1]/div[3]/div/div[3]/div/div[15]/div/div/div/div/div/div/div[1]/div/div[{index}]/div[2]/table/tbody'
        try:
            element = driver.find_element_by_xpath(xpath)
        except:
            driver.close()
            continue
        chart_lst = element.text.split("\n")


        f.write(parse.unquote(v[20:]))
        print(parse.unquote(v[20:]), end='')
        f.write(',')
        print(',', end='')
        for i in stat_names:
            f.write(chart_lst[chart_lst.index(i)+1])
            print(chart_lst[chart_lst.index(i)+1], end='')
            f.write(',')
            print(',', end='')
        f.write('\b\n')
        print('\n', end='')
        time.sleep(1)

        driver.close()
        time.sleep(1)