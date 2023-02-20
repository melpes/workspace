import numpy as np
import pandas as pd

nda = np.arange(100).reshape((10, 10))
print(nda)

def line_range(nda):
    size = nda.shape[0]
    for i in np.arange(0, size):
        yield nda[0:1+i, size-1-i:size].diagonal(), '1'
    for i in np.arange(size-2, -1, -1):
        yield nda.T[0:1+i, size-1-i:size].diagonal(), '2'

lst = np.zeros((10, 10), int)
for i, (line, dir) in enumerate(line_range(nda)):
    print(line)
    i %= nda.shape[0]
    for j in range(line.size):
        if dir == '1':
            index = (j, nda.shape[0] + j - (i + 1))
        elif dir == '2':
            index = (i + j + 1, j)
        
        lst[index] = line[j]
        # print(dir, '\t', np.where(nda == line[j])[0][0], np.where(nda == line[j])[1][0], end=' ')
        # print(index, end='')
        # print((np.where(nda == line[j])[0][0], np.where(nda == line[j])[1][0]) == index)
print(lst)