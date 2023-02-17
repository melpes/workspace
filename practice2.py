import numpy as np
import pandas as pd

nda = np.array([i**2 for i in range(4)]).reshape((2,2))
print(nda, type(nda))
for i in nda:
    print(i, type(i))