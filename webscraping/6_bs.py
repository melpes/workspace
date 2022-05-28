import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
try:
    res.raise_for_status()
except Exception:
    print("응답코드 에러")

soup = BeautifulSoup(res.text, "lxml") # 가져온 html 문서를 lxml를 통해 soup 객체로 만듦
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # 가장 먼저 발견되는 a
# print(soup.a.attrs) # a 속성
# print(soup.a["href"]) # 원하는 속성 인덱스로 넣기

# soup 객체 a 태그 속 class 속성이 Nbtn_upload인 것 탐색
# soup.find("a", attrs={"class":"Nbtn_upload"}) 
# soup.find(attrs={"class":"Nbtn_upload"}) 

# rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# # print(rank3.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# print(rank2.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="전지적")
print(webtoon)