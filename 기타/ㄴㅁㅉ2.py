import random, re, math, copy

while True:
    n = int(input())
    maximum = 6

    numbers = [i for i in range(1, maximum + 1)]
    operators = ['*', '/', '+', '-', '^']

    # 숫자 나열 및 붙임 처리(미완)
    def set_nums(nums, count) -> list:
        if count % 2 == 0:
            while True:
                a, b = random.sample([i for i in range(1, maximum+1)], 2)
                if a in nums and b in nums:
                    del nums[nums.index(a)]
                    del nums[nums.index(b)]
                    break

            nums.append(int(str(a) + str(b)))
        random.shuffle(nums)
        return nums

    def set_nrf(numbers, n, maximum):
        nums = copy.deepcopy(numbers)
        proper = 0
        for i in range(1, maximum):
            if abs(math.factorial(i) - n) < abs(math.factorial(i+1) - n):
                proper = i
        if proper == 0:
            proper = maximum - 1
        idex = nums.index(proper)
        nums[idex] = math.factorial(nums[idex])

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
    def set_basic_operator(length, operators) -> list:
        basic_operator = [random.choice(operators) for _ in range(length - 1)]
        return basic_operator

    # 루트, 팩토리얼 처리
    def set_rf_operator(length, bracket_value):
        i = sum(filter(lambda x:x>0, bracket_value)) + length
        root_operator = [random.randint(0, 0) for _ in range(i)]
        facto_operator = [random.randint(0, 0) for _ in range(i)]
        return root_operator, facto_operator

    # 최종 식 문자열로 표기
    def assemble_expression(length, nums, bracket_value, basic_operator, root_operator, facto_operator):
        ans = []

        for i in range(length):
            if bracket_value[i] > 0:
                ans += ['('] * bracket_value[i]
                ans += [str(nums[i])]
            else:
                ans += [str(nums[i])]
                ans += [')'] * -bracket_value[i]

        k = -1
        for i in range(len(ans)-1, -1, -1):
            if re.match(r"[0-9]", ans[i]):
                j = 1
                while True:
                    if ans[i-j] != '(':
                        break
                    if i-j-1 == -1:
                        break
                    j += 1

                ans.insert(i-j+1, basic_operator[k])
                if -k == len(basic_operator) :
                    break
                k -= 1

        posi_brac_index, nega_brac_index = [], []
        for i in range(len(ans)):
            if ans[i] == '(' or re.match(r"[0-9]", ans[i]):
                posi_brac_index.append(i)

        for i in range(len(posi_brac_index) - 1, -1, -1):
            if root_operator[i]:
                ans.insert(posi_brac_index[i], "r")
        
        for i in range(len(ans)):
            if ans[i] == ')' or re.match(r"[0-9]", ans[i]):
                nega_brac_index.append(i)
        
        for i in range(len(nega_brac_index) - 1, -1, -1):
            if facto_operator[i]:
                ans.insert(nega_brac_index[i] + 1, "!")
        
        return ans

    class Break(Exception): 
        pass

    def to_expression(lst):
        expression = ''
        for i in lst:
            try:
                for j in range(4, maximum+1):
                    if int(i) == math.factorial(j):
                        expression += str(j) + '!'
                        raise Break
                raise ValueError
            except ValueError:
                expression += str(i)
            except Break:
                pass

        return expression

    def calculate(exp_list):
        keep = True
        while keep:
            new_brackests = [0 for i in range(len(exp_list))]
            for i in range(len(exp_list)):
                if exp_list[i] == '(':
                    new_brackests[i] += 1
                elif exp_list[i] == ')':
                    new_brackests[i] -= 1


            posi_list = [i for i, v in enumerate(new_brackests) if v == 1]

            if len(posi_list) == 0:
                break
            
            starter = 0
            ender = new_brackests.index(-1)
            for i in posi_list:
                if i >= ender:
                    break
                starter = i

            sample = [exp_list.pop(i) for i in range(ender-1, starter, -1)]
            sample.reverse()

            cal = 0
            for i in range(len(sample)):
                if type(sample[i]) != str:
                    continue
                if re.match(r"[\*/\+\-\^]", sample[i]):
                    cal = i
                if re.match(r"[0-9]", sample[i]):
                    sample[i] = int(sample[i])

            joint = [sample[:cal], sample[cal+1:]]

            res = [0, 0]
            for i in range(len(joint)):
                if 'r' in joint[i]:
                    if joint[i][1] < 0:
                        # print("root error")
                        keep = False
                        break
                    res[i] = joint[i][1] ** 0.5
                else:
                    res[i] = joint[i][0]

                if '!' in joint[i]:
                    try:
                        res[i] = math.factorial(res[i])
                    except:
                        # print("facto error")
                        keep = False
                        break

            res.append(sample[cal])

            ans = 0
            try:
                if res[0] > 1e3 or res[1] > 1e3:
                    keep = False
                    break
            except:
                keep = False
                break
            try:
                if res[-1] == "*":
                    ans = res[0] * res[1]
                elif res[-1] == "/":
                    ans = res[0] / res[1]
                elif res[-1] == "+":
                    ans = res[0] + res[1]
                elif res[-1] == "-":
                    ans = res[0] - res[1]
                elif res[-1] == "^":
                    ans = res[0] ** res[1]
            except:
                # print("cal error")
                keep = False
                break

            try:
                if ans > 1e5:
                    keep = False
                    break
            except:
                keep = False
                break
            
            exp_list.insert(starter+1, ans)
            del exp_list[starter]
            del exp_list[starter+1]

        if '!' in exp_list:
            try:
                exp_list[-2] = math.factorial(exp_list[-2])
                del exp_list[-1]
            except:
                keep = False
        
        return exp_list, keep

    count = 0
    while True:
        count += 1

        nums = set_nums(set_nrf(numbers, n, maximum), count)
        length = len(nums)
        bracket_value = set_brackets(length)
        basic_operator = set_basic_operator(length, operators)
        root_operator, facto_operator = set_rf_operator(length, bracket_value)

        exp_list = assemble_expression(length, nums, bracket_value, basic_operator, root_operator, facto_operator)

        expression = to_expression(exp_list)
        result, keep = calculate(exp_list)
        ans = to_expression(result)
        
        if keep:
            print(count, ans)

        try:
            if abs(float(ans)) == n:
                print(expression)
                break
        except:
            pass