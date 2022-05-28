f = open("subject/lotto145.txt", "r")
data = f.readlines() # 데이터 리스트로 읽기
freq = [] # 빈도변수 (index = 로또 번호)
for i in range(45):
    freq.append(0) # 빈도변수 초기화
for i in data:
    i = i.split(" ") # 로또 번호별 분리
    for j in range(7): # 각 당첨번호에 대해,
        freq[int(i[j]) - 1] += 1 # 해당 로또번호에 해당하는 빈도변수 값 1 증가
f.close() 
# 빈도 결과물 출력하기
print(freq)
for i in range(1,46):
    print("로또번호." + str(i) +": " + str(freq[i]) + "번")

