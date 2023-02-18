import numpy as np
import pandas as pd

line = np.arange(9).reshape((3, 3))
print(line)
line = line.reshape(9)
print(line)

marker = pd.Series({i:0 for i in range(line.size)})
df = {
    "info" : line,
    "score level" : marker,
    "empty level" : marker,
    "is blocked" : False
}

dfa = pd.DataFrame({i:marker for i in range(3)})
print(dfa.shape)