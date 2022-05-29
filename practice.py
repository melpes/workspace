import random
import time


bugs = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
random.shuffle(bugs)
pointers = [i for i in range(len(bugs))]
random.shuffle(pointers)
lst_number = [i for i in range(len(bugs))]
addings = [-1, 0, 1, 2]
addings_density = [4, 2, 3, 1]
addings_lst = []

for i in range(len(addings)):
    for _ in range(addings_density[i]):
        addings_lst.append(addings[i])


print(pointers)

while True:
    str = "|"
    for v in bugs:
        str += f"{v}|"
    
    lst_number_str = "|"
    for v in lst_number:
        lst_number_str += f"{v}|"
    
    print(lst_number_str)
    print(str)


    n = int(input("enter the index to debug\n"))
    print("버그 수정 중")

    for _ in range(3):
        time.sleep(0.5)
        print(".")

    if bugs[n] == 0:
        bugs[n] = 1
        print("버그를 늘려버렸다...")

    else:
        bugs[n] = 0
        print("디버그 성공!!")
    
    destiny = random.choice(addings_lst)
    if destiny == -1:
        continue
    if destiny >= 0:
        if bugs[pointers[n]] == 1:
            bugs[pointers[n]] = 0
            print("이게 왜 됨?")
        elif bugs[pointers[n]] == 0:
            bugs[pointers[n]] = 1
            print("이건 왜 안됨?")
    if destiny >= 1:
        if bugs[pointers[pointers[n]]] == 1:
            bugs[pointers[pointers[n]]] = 0
            print("이게 왜 됨?????")
        elif bugs[pointers[pointers[n]]] == 0:
            bugs[pointers[pointers[n]]] = 1
            print("이게 왜 안됨?????")
    if destiny == 2:
        if bugs[pointers[pointers[pointers[n]]]] == 1:
            bugs[pointers[pointers[pointers[n]]]] = 0
            print("???????????????")
        elif bugs[pointers[pointers[pointers[n]]]] == 0:
            bugs[pointers[pointers[pointers[n]]]] = 1
            print("ㅅㅂㄹㅇ?")
    print(f"남은 버그 수 : {bugs.count(1)}")
    if bugs.count(1) == 0:
        print("디버깅 완료!")
        break
    elif bugs.count(0) == 0:
        print("프로그램 폐기 처분")
        break