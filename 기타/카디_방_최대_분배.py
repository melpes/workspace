import numpy as np

NODES_SIZE = {'x':3, 'y':3}

def main() -> None:
    nodes = fill_new_nodes(NODES_SIZE, nodes)

    set_nodes_dir(nodes)
    
    set_nodes_value(nodes)

    while True:
        print_node(nodes)
        move(nodes)
        input()

def fill_new_nodes(nodes_size) -> list:
    nodes = np.full((nodes_size.keys()), None)
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
    nodes[0, 1].value = 1
    nodes[2, 1].value = 1

def print_node(node : np) -> None:
    for y in range(node.shape[1]):
        for x in range(node.shape[0]):
            print(node[x][y].value, end="\t")
        print()

def move(nodes) -> None:
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
        assert sum(self.to_dir.values()) == 1, "\
    NoneConservation : sum of Node.to_dir.keys() is not 1."
            




            
    

if __name__ == "__main__":
    main()