import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:

    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("광고 상품 제외\n")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text()
    price = item.find("strong", attrs={"class":"price-value"}).get_text()
    rate = item.find("em", attrs={"class":"rating"})
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"
    n_rate = item.find("span", attrs={"class":"rating-total-count"})
    if n_rate:
        n_rate = n_rate.get_text()
    else:
        n_rate = "평점 수 없음"
    print(name, price, rate, n_rate,"\n", sep="\n")