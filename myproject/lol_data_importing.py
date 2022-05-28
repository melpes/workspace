import requests
# from requests.api import request

res = requests.get("https://namu.wiki/w/%EB%A6%AC%EA%B7%B8%20%EC%98%A4%EB%B8%8C%20%EB%A0%88%EC%A0%84%EB%93%9C/%EC%B1%94%ED%94%BC%EC%96%B8")
res.raise_for_status() # 응답코드가 정상(200)을 받지 못하면 에러 발생
# print("응답코드 :", res.status_code)

# if res.status_code == requests.codes.ok:
#     print("정상")
# else:
#     print("문제 발생 [에러코드 ,", res.status_code, "]")

# res.raise_for_status()
# print("정상")

