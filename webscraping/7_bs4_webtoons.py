import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
try:
    res.raise_for_status()
except Exception:
    print("응답코드 에러")

soup = BeautifulSoup(res.text, "lxml") # 가져온 html 문서를 lxml를 통해 soup 객체로 만듦

cartoons = soup.find_all("a", attrs={"class":"title"})
for v in cartoons:
    print(v.get_text())