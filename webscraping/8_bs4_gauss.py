import requests
from bs4 import BeautifulSoup

total_rates = 0
n = 0

for i in range(89, 92):
    url = f"https://comic.naver.com/webtoon/list.nhn?titleId=675554&page={i}"
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception:
        print("응답코드 에러")

    soup = BeautifulSoup(res.text, "lxml") # 가져온 html 문서를 lxml를 통해 soup 객체로 만듦

    cartoons = soup.find_all("td", attrs={"class":"title"})
    rates = soup.find_all("div", attrs={"class":"rating_type"})


    for title, r in zip(cartoons, rates):
        rate = (float)(r.find("strong").get_text())
        print(title.get_text())
        print("https://comic.naver.com"+ title.a["href"])
        print("별점 : " + str(rate))
        total_rates += rate
        n += 1

print(total_rates / n)