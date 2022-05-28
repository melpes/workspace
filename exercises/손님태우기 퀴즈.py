from random import *
pa_list = {}
pa_checking = {}
numberofO = 0

for i in range(1,51):
    pa_list[i] = randint(5,50)


for i in range(1,51):
    if (pa_list[i] >= 5) and (pa_list[i] <= 15):
        pa_checking[i] = "O"
        numberofO += 1
    else :
        pa_checking[i] = " "

for i in range(1,51):
    print(f"[{pa_checking[i]}] {i}번째 손님 (소요시간 : {pa_list[i]}분)")

print()
print(f"총 탑승 승객 : {numberofO} 명")