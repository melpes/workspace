import random, copy

n = int(input())

length = 6 # 1~n을 결정하는 n이다.
numbers = [i for i in range(1, length + 1)]
operators = ['*', '/', '+', '-', '^']

count = 0
while True:
    count += 1
    nums = copy.deepcopy(numbers)
    random.shuffle(nums)

    basic_operators = [random.choice(operators) for _ in range(length - 1)]

    ans = '(' * (length - 1)
    for i in range(length):
        ans += str(nums[i])
        if i != 0:
            ans += ')'
        if i == length - 1:
            break
        ans += basic_operators[i]

        value = nums[0]
        for i in range(1, length):
            try:
                if basic_operators[i - 1] == '*':
                    value *= nums[i]
                elif basic_operators[i - 1] == '/':
                    value /= nums[i]
                elif basic_operators[i - 1] == '+':
                    value += nums[i] 
                elif basic_operators[i - 1] == '-':
                    value -= nums[i]
                elif basic_operators[i - 1] == '^':
                    value **= nums[i]
            except:
                pass

    if value == n:
        print(ans)
        print(count)
        break