import pandas as pd
import numpy as np

class Board:
    BLANK, BLACK, WHITE, BLOCKED = 0, 1, 2, -1
    n_of_board = 0

    def __init__(self, board_size) -> None:
        Board.n_of_board += 1
        self.board_size = board_size
        self.stone_info = np.zeros(self.board_size, dtype=int)