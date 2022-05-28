def main():
    ip = 1
    sum = 0
    try:
        ip = int(input("숫자를 입력하십시오.(종료하려면 9999를 입력하십시오) : "))
    except:
        print("정수를 입력하십시오")
        return

    if ip == 9999:
        return True

    for i in range(1, ip + 1, 2):
        # print(i)
        sum += i

    print(sum)

while True:
    isclose = main()

    if isclose:
        break

# while True:
#     ip = 1
#     sum = 0
#     ip = int(input("숫자를 입력하십시오.(종료하려면 9999를 입력하십시오) : "))
#     print("정수를 입력하십시오")
    
#     if ip == 9999:
#         break

#     for i in range(1, ip + 1, 2):
#         # print(i)
#         sum += i

#     print(sum)