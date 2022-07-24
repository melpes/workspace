# 2x3 노드가 있고 
# xx
# xx
# xx
# 1, 2 항목으로 투입되는 양에 대해
# 각 x로 어디든지 퍼져나갈 수 있고 그 확률이 각각 다르다고 하면
# 각 노드에 항목이 존재하는 평균 비율은 어떻게 되는가
import copy

node = [
    [0, 0, 0], 
    [0, 0, 0]
]

node_percent = [
    [None, None, None], 
    [None, None, None]
]

a, a0 = 1/3, 0.2
b, b0 = (1 - a) / 2, 0
c, c0 = 1 - b0, 0
d, d0 = 1 - c0, 0
e = 1 - a0 - 2*d0

print(a + 2*b, b0 + c, c0 + d, a0 + 2*d0, a0 + 2*d0 + e)
print(a, b, c, d, e)
print(a0, b0, c0, d0)
assert a + 2*b or b0 + c or c0 + d or a0 + 2*d0 + e, "분배 합 오류"

node_connecting_list = [[
    [c, b0, None, None], 
    [a, b, None, b],
    [c, None, None, b0]
], [
    [None, d, c0, None],
    [None, d0, a0, d0],
    [None, None, c0, d]
]
]

for x in range(2):
    for y in range(3):
        node_percent[x][y] = {
            (1, 0) : node_connecting_list[x][y][0],
            (0, 1) : node_connecting_list[x][y][1],
            (-1, 0) : node_connecting_list[x][y][2],
            (0, -1) : node_connecting_list[x][y][3],
            (0, 0) : None, 
            (-1, -1) : None, 
            (-1, 1) : None, 
            (1, -1) : None, 
            (1, 1) : None
        }
node_percent[1][1][0, 0] = e


def move(x, y, node, node_percent):
    nd = [
    [0, 0, 0], 
    [0, 0, 0]
]
    nd[x][y] = node[x][y]

    value = nd[x][y]
    nd[x][y] = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not node_percent[x][y][i, j]:
                continue
            nd[x+i][y+j] += round(node_percent[x][y][i, j] * value, 3)
    return nd

print('---------------')
node[0][1] = 1
print(node[0][2], node[1][2], sep='\t')
print(node[0][1], node[1][1], sep='\t')
print(node[0][0], node[1][0], sep='\t')
count = 0
print('---------------')
while True:
    future_node = [
        [0, 0, 0], 
        [0, 0, 0]
]
    count += 1
    for x in range(2):
        for y in range(3):
            nd = move(x, y, node, node_percent)
            for i in range(2):
                for j in range(3):
                    future_node[i][j] += nd[i][j]
    node = future_node

    print(node[0][2], node[1][2], sep='\t')
    print(node[0][1], node[1][1], sep='\t')
    print(node[0][0], node[1][0], sep='\t')
    input(str(count) + '--------------')