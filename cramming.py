daily = int(input("하루 공부 시간 : "))

n_subj = int(input("과목 수 : "))

subj_lst = [[] for _ in range(n_subj)]
lst = input("과목명 : ").split()
for i in range(n_subj):
    subj_lst[i].append(lst[i])

print("해당 과목을 얼마나 중요하게 생각하는지 1~5의 숫자로 입력하세요.")

for i in range(n_subj):
    subj_lst[i].append(int(input(f"{subj_lst[i][0]} : ")))

print("해당 과목을 얼마나 공부했는지 1~5의 숫자로 입력하세요.")

for i in range(n_subj):
    subj_lst[i].append(int(input(f"{subj_lst[i][0]} : ")))

print("해당 과목은 시험까지 며칠 남았는지 입력하세요.")

for i in range(n_subj):
    subj_lst[i].append(int(input(f"{subj_lst[i][0]} : ")))

sum_prior = 0
for i in range(n_subj):
    sum_prior += subj_lst[i][1] - subj_lst[i][2]

def priority(prior : int):
    return (prior - sum_prior / n_subj + 5) * 20 / n_subj

print("분할 비율은 다음과 같습니다.")

for i in range(n_subj):
    print(f"{subj_lst[i][0]} : {priority(subj_lst[i][1] - subj_lst[i][2])}%")



input()
print("해당 과목의 1일, 2일, 3일차 공부량은 다음과 같습니다.")

for i in range(n_subj):
    imp = subj_lst[i][3] * priority(subj_lst[i][1] - subj_lst[i][2]) / (5 - subj_lst[i][2])
    d1 = (5 - subj_lst[i][2]) * imp / 4.45
    print(f"{subj_lst[i][0]} : {round(daily/100*d1, 2)}h, {round(daily/100*0.8*d1, 2)}h, {round(daily/100*0.8**2*d1, 2)}h")