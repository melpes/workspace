import numpy as np

def main() -> None:
    node = np.zeros((3, 3))
    print_node(node)
    x_bridge = np.zeros(())
    y_bridge = np.zeros(())


def print_node(node : np) -> None:
    for y in range(node.shape[1]):
        for x in range(node.shape[0]):
            print(node[x][y], end="\t")
        print()

if __name__ == "__main__":
    main()