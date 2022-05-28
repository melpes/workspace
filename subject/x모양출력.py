# word = []

# for i in range(10):
#     word.append("")
#     for j in range(10):
#         word[i] += "*" if i == j or i + j == 9 else "-"

# # print(wd)
# for i in range(len(word)):
#     print(word[i])

word = []

for i in range(10):
    word.append("")
    for j in range(10):
        if i == j or i + j == 9:
            word[i] += "*" 
        else:
            word[i] += "-"

# print(word)
for i in range(10):
    print(word[i])