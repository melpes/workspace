import re

p = re.compile("ca.e")
# . (ca.e): 하나의 문자를 의미 ex) care, cafe, case
# ^ (^de): 문자열의 시작 ex) desk, destination
# $ (se$): 문자열의 끝 ex) case, base

def print_match(m):
    if m:
        print(m.group()) # 일치하는 문자열만 반환
        print(m.string) # 입력받은 문자열 반환
        print(m.start()) # 일치하는 문자열의 시작 인덱스
        print(m.end()) # 일치하는 문자열의 끝 인덱스
        print(m.span()) # 일치하는 문자열의 시작과 끝 인덱스
    else:
        print("실패")

# m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 한 번 확인
# print_match(m)

# m = p.search("good care service") # search : 주어진 문자열 중 일치하는게 있는지 앞에서부터 하나 확인
# print_match(m)

# list = p.findall("careless cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
# print(list)

# 정규식 작성 방법
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열")
# 3. m = p.search("비교할 문자열")
# 4. list = p.findall("비교할 문자열")

# 원하는 형태 작성 방법
# . : 하나의 문자 칸
# ^ : 문자열이 무엇으로 시작하는지 전치수식
# $ : 문자열이 무엇으로 끝나는지 후치수식