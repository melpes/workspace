import random

n = int(input())

maximum = 8
numbers = [i for i in range(1, maximum + 1)]
calculars = ['*', '/', '+', '-', '^']


length = len(numbers)
count = 0
while True:
    count += 1
    nums = random.sample(numbers, length)
    random.shuffle(nums)

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

    ans = ''
    for i in range(length):
        if bracket_value[i] > 0:
            ans += '(' * bracket_value[i]
            ans += str(nums[i])
        else:
            ans += str(nums[i])
            ans += ')' * -bracket_value[i]

    print(ans)
    if count == 10:
        break