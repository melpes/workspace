import re

w = input()
lss = map(str, w.split())
lst = ''
for i in lss:
    lst += i

for j in range(len(lst)-1):
    st = ''
    for i in range(len(lst)):
        st += lst[i]
        if i == j:
            st += ' '

    print(st)

re.match(r"[을를이가와과로도의]", st)
