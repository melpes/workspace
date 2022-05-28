import requests
url = "http://nadocoding.tistory.com"
# user agent는 접근하려는 사용자의 브라우저 등의 정보를 담고 있으며 
# 없을 시 서버가 차단하여 403오류가 일어날 수 있다.
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
res = requests.get(url, headers)
res.raise_for_status() # 응답코드가 정상(200)을 받지 못하면 에러 발생

print(len(res.text))
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)