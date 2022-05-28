import time
n, m = map(int, input().split())
max_value = 0

start = time.time()
for i in range(n):
    n_list = list(map(int, input().split()))
    n_list.sort()
    if max_value < n_list[0]:
        max_value = n_list[0]
print(max_value)
end = time.time()
print(end-start)