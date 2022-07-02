# 극초반부 521같은 세자리이용
# 500후반 3!! 이랑 4!^2이런거쓰고
# 600~800초쯤엔 3!!
# 800후반~999는 진짜 개절망


import random

n = int(input())

# +-*/() ^!

# 규칙
# 1. ( 이후엔 반드시 )
# 2. ()!를 제외하고는 기호 연속 불가
# 3. 숫자 연속 불가
# 4. ! 앞에는 반드시 )나 숫자

numbers = [i for i in range(1, 11)]
calculars = ['*', '/', '+', '-', '^']

count = 0
while True:
    for length in range(1, len(numbers) + 1):
        count += 1
        length = len(numbers)
        nums = random.sample(numbers, length)
        random.shuffle(nums)

        cals = [random.choice(calculars) for _ in range(length - 1)]

        ans = '(' * (length - 1)
        for i in range(length):
            ans += str(nums[i])
            if i != 0:
                ans += ')'
            if i == length - 1:
                break
            ans += cals[i]

        value = nums[0]
        for i in range(1, length):
            try:
                if cals[i - 1] == '*':
                    value *= nums[i]
                elif cals[i - 1] == '/':
                    value /= nums[i]
                elif cals[i - 1] == '+':
                    value += nums[i]
                elif cals[i - 1] == '-':
                    value -= nums[i]
                elif cals[i - 1] == '^':
                    value **= nums[i]
            except:
                pass
        
        # print(f"{ans} = {value}")
        # print(count, value)
        if value == n:
            # print(ans)
            # print(f"{ans} = {value}")
            break

    if value == n:
        print(ans)
        print(count)
        break