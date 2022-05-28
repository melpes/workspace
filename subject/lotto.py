with open("subject/lotto145.txt", "r") as file:
    number_lst = [0 for _ in range(45)]
    while True:
        lst = list(map(int, file.readline().split()))
        if not lst:
            break
        while lst:
            index = lst.pop() - 1
            number_lst[index] += 1

mean = 0
for i in range(len(number_lst)):
    mean += number_lst[i]

# print(mean / 253 / 7) 개수 일치 확인. 결과가 1이면 일치

with open("subject/lotto_freq.txt", "w") as file:
    for i in range(len(number_lst)):
        file.write("#No {:02d} : {:d}\n".format(i + 1, number_lst[i]))