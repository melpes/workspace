import random

n = int(input())
maximum = 8

numbers = [i for i in range(1, maximum + 1)]
operators = ['*', '/', '+', '-', '^']

# 숫자 나열 및 붙임 처리(미완)
def set_nums(numbers) -> list:
    nums = random.sample(numbers, len(numbers))
    random.shuffle(nums)
    return nums

# 연산 순서 괄호 처리
def set_brackets(length) -> list:
    bracket_value = [0 for _ in range(length)]
    bracket_index = [i for i in range(length)]

    while len(bracket_index) > 1:
        pusher = random.randint(0, len(bracket_index) - 2)
        bracket_value[bracket_index[pusher]] += 1

        if bracket_value[bracket_index[pusher + 1]] == 0:
            bracket_value[bracket_index[pusher + 1]] -= 1
            del bracket_index[pusher + 1]
            continue

        if pusher + 2 < len(bracket_index):
            bracket_value[bracket_index[pusher + 2] - 1] -= 1
            del bracket_index[pusher + 1]
            continue

        bracket_value[-1] -= 1
        del bracket_index[pusher + 1]
    return bracket_value

# 사칙연산+제곱 처리
def set_basic_operator(length) -> list:
    basic_operator = [random.choice(operators) for _ in range(length - 1)]
    return basic_operator

# 루트, 팩토리얼 처리
def set_rf_operator(length, bracket_value):
    i = sum(filter(lambda x:x>0, bracket_value)) + length
    root_operator = [random.randint(0, 1) for _ in range(i)]
    facto_operator = [random.randint(0, 1) for _ in range(i)]
    return root_operator, facto_operator

# 최종 식 문자열로 표기
def assemble_expression(length, nums, bracket_value):
    ans = ''

    for i in range(length):
        if bracket_value[i] > 0:
            ans += '(' * bracket_value[i]
            ans += str(nums[i])
        else:
            ans += str(nums[i])
            ans += ')' * -bracket_value[i]
    return ans

length = len(numbers)
count = 0
while True:
    count += 1

    nums = set_nums(numbers=numbers)
    bracket_value = set_brackets(length=length)
    basic_operator = set_basic_operator(length=length)

    expression = assemble_expression(length=length, nums=nums, bracket_value=bracket_value)

    print(expression)
    if count == 10:
        break