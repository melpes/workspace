import pandas as pd

champions = ['zed', 'kaisa']
basic_ad = [63, 59]

with open("test.csv", "w", encoding="utf-8") as f:
    for i in range(len(champions)):
        f.write(champions[i])
        f.write(',')
        f.write(str(basic_ad[i]))
        f.write('\n')