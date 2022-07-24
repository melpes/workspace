import numpy as np

def main() -> None:
    nodes = np.full((3, 3), None)
    for x in range(3):
        for y in range(3):
            nodes[x, y] = Node((x, y))

    set_nodes_dir(nodes)
    
    set_nodes_value(nodes)

    while True:
        print_node(nodes)
        move(nodes)
        input()

def print_node(node : np) -> None:
    for y in range(node.shape[1]):
        for x in range(node.shape[0]):
            print(node[x][y].value, end="\t")
        print()

class NoneConservation(Exception):
    pass

class Node:
    def __init__(self, coor : tuple) -> None:
        self.to_dir = {}
        self.node_num = coor
        self._value = 0
        self.pre_value = 0
    
    @property
    def value(self):
        self.check()
        return self._value

    @value.setter
    def value(self, v):
        self._value = v

    def check(self):
        if sum(self.to_dir.values()) != 1:
            print("todir", self.to_dir.values())
            raise NoneConservation # assert로 바꾸기
            
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

def set_nodes_value(nodes):
    nodes[0, 1].value = 1
    nodes[2, 1].value = 1


def move(nodes):
    dim = nodes.shape
    for x in range(dim[0]):
        for y in range(dim[1]):
            nodes[x, y].pre_value = 0

    for x in range(dim[0]):
        for y in range(dim[1]):
            for coor, percent in nodes[x, y].to_dir.items():
                nodes[coor].pre_value += nodes[x, y].value * percent

    for x in range(dim[0]):
        for y in range(dim[1]):
            nodes[x, y].value = round(nodes[x, y].pre_value, 3)
            
    

if __name__ == "__main__":
    main()