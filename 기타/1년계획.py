from datetime import datetime
import time

timecount = 119
while True:
    time.sleep(1)
    timecount += 1
    if timecount != 120:
        continue
    timecount = 0
    print("")

    today = datetime.today()

    start = datetime(2021, 7, 9, 22, 00)

    timedel = today - start

    day = datetime(1, 1, 1) + timedel
    (month, day, hour, minute, second) = (day.month, day.day, day.hour, day.minute, day.second)
    month -= 1
    day -= 1

    with open("1년계획.txt", "w") as f:
        f.write(f"[시작일로부터 지난 시간 : {month} 개월 {day} 일 {hour} 시간 {minute} 분]    \n")
        f.write(f"[현재시간 : {today}]\n")
    print(f"[시작일로부터 지난 시간 : {month} 개월 {day} 일 {hour} 시간 {minute} 분]    \n")
    print(f"[현재시간 : {today}]\n")