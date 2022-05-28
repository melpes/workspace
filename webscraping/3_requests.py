import requests
# from requests.api import request
res = requests.get("http://google.com")
res.raise_for_status() # 응답코드가 정상(200)을 받지 못하면 에러 발생
# print("응답코드 :", res.status_code)

# if res.status_code == requests.codes.ok:
#     print("정상")
# else:
#     print("문제 발생 [에러코드 ,", res.status_code, "]")

# res.raise_for_status()
# print("정상")

print(len(res.text))
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)