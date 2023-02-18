import numpy as np
import pandas as pd

line = np.array([0, 0, 1, 1, 1, 0, 1, 0, 1, 0])

marker = pd.Series({i:0 for i in range(line.size)})
df = {
    "info" : line,
    "score level" : marker,
    "empty level" : marker,
    "is blocked" : False
}
line_markers = pd.DataFrame(df)
print(line)
print(line_markers)
for i in range(line_markers.shape[0]):
    # print(i)
    print(line_markers.loc[i, "info"], end='\t')
    print(line_markers["info"][i])