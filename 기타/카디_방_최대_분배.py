import random
import numpy as np

NODES_SIZE = {'x':3, 'y':3}

def main() -> None:
    nodes = fill_new_nodes(NODES_SIZE)

    set_nodes_dir(nodes)
    
    set_nodes_value(nodes)

    while True:
        print_node(nodes)
        move(nodes)
        # input()

class Node:
    def __init__(self, coor : tuple) -> None:
        self.to_dir = {}
        self.node_num = coor
        self._values = list()
        self.pre_values = list()
    
    @property
    def values(self):
        self.check()
        return self._values

    @values.setter
    def values(self, v):
        self._valus = v

    def check(self):
        assert sum(self.to_dir.values()) == 1, "\
\   \   NoneConservation : sum of Node.to_dir.keys() is not 1."
            
class Unit:
    def __init__(self) -> None:
        self.last_visited_node = None

    def cal_coor(self, to_dir) -> tuple:
        key = random.random()
        for coor, percent in to_dir.items():
            key -= percent
            if key <= 0:
                return coor

def fill_new_nodes(nodes_size) -> list:
    nodes = np.full((list(nodes_size.values())), None)
    for x in range(nodes_size['x']):
        for y in range(nodes_size['y']):
            nodes[x, y] = Node((x, y))
    return nodes

def set_nodes_dir(nodes) -> None:
    nodes[0, 0].to_dir[0+1, 0+1] = 1

    nodes[1, 0].to_dir[1-1, 0] = 1
    
    nodes[2, 0].to_dir[2-1, 0] = 1

    nodes[0, 1].to_dir[0, 1+1] = 1
    

    nodes[1, 1].to_dir[1, 1] = 1
    
    nodes[2, 1].to_dir[2, 1-1] = 1
    
    nodes[0, 2].to_dir[0+1, 2] = 1

    nodes[1, 2].to_dir[1+1, 2] = 1

    nodes[2, 2].to_dir[2-1, 2-1] = 1

def set_nodes_value(nodes) -> None:
    nodes[0, 1].values.append(Unit())
    nodes[2, 1].values.append(Unit())

def print_node(node : np) -> None:
    for y in range(node.shape[1]):
        for x in range(node.shape[0]):
            print(len(node[x][y].values), end="\t")
        print()

def move(nodes) -> None:
    dim = nodes.shape
    for x in range(dim[0]):
        for y in range(dim[1]):
            nodes[x, y].pre_values = list()

    for x in range(dim[0]):
        for y in range(dim[1]):
            for unit in nodes[x, y].values:
                coor = unit.cal_coor(nodes[x, y].to_dir)
                nodes[coor].pre_values = unit

    for x in range(dim[0]):
        for y in range(dim[1]):
            nodes[x, y].values = nodes[x, y].pre_values
            print(f"{x, y}", nodes[x, y].values)
            print(nodes[x, y].pre_values)

if __name__ == "__main__":
    main()