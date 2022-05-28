n = input()
plan = list(map(str, input().split()))

x, y = 1, 1

for i in range(len(plan)):
    if x == 1 and plan[i] == "L":
        continue
    if x == n and plan[i] == "R":
        continue
    if y == 1 and plan[i] == "U":
        continue
    if y == n and plan[i] == "D":
        continue
    if plan[i] == "L":
        x -= 1
    if plan[i] == "R":
        x += 1
    if plan[i] == "U":
        y -= 1
    if plan[i] == "D":
        y += 1
print(y, x)