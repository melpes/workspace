# import numpy as np
# import pandas as pd

# line = np.arange(9).reshape((3, 3))
# print(line)
# line = line.reshape(9)
# print(line)

# marker = pd.Series({i:0 for i in range(line.size)})
# df = {
#     "info" : line,
#     "score level" : marker,
#     "empty level" : marker,
#     "is blocked" : False
# }
index = pd.MultiIndex.from_product([[i for i in range(3)],[i for i in range(3)]], names=['x', 'y'])
columns = ["info"]
line_markers = pd.DataFrame(line, index=index, columns=columns)
print(line_markers)

class A:
    def __init__(self) -> None:
        self.n = 0
    
    def change(self):
        self.n += 1
    
class B:
    def __init__(self, a : A) -> None:
        self.a = a
    def printa(self):
        print(self.a.n)
    def add(self):
        self.a.change()

a = A()
b = B(a)
print(a.n is b.a.n)
