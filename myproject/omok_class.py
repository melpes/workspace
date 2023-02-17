import pandas as pd
import numpy as np

def main() -> None:
    board = Board(10)
    for i in range(5):
        board.put_stone((i+3, -i+8))
    board.print()
    board.check_winner()


class Board:
    BLANK, BLACK, WHITE, BLOCKED = 0, 1, -1, 2
    color_dict = {
        BLANK : "BLANK",
        BLACK : "BLACK",
        WHITE : "WHITE",
        BLOCKED : "BLOCKED"
    }
    n_of_board = 0

    def __init__(self, board_width : int) -> None:
        Board.n_of_board += 1
        self.size_of_board = board_width
        self.stone_info = np.zeros((self.size_of_board, ) * 2, dtype=int)
        self.turn = Board.BLACK

    def put_stone(self, pos : tuple) -> None:
        for i in range(len(pos)):
            assert self.size_of_board > pos[i] and pos[i] >= 0, "pos : index error"
        assert self.stone_info[pos] == Board.BLANK, "돌을 놓으려는 위치가 빈칸이 아닙니다!"
        self.stone_info[pos] = self.turn

    def check_winner(self) -> int:
        for color in (Board.BLACK, Board.WHITE):
            for line in self.line_range():
                stack = 0
                for space in line:
                    if space == color:
                        stack += 1
                    else:
                        if stack == 5:
                            print(f"{Board.color_dict[color]} WIN!")
                            return color
                        stack = 0
            if stack == 5:
                print(f"{Board.color_dict[color]} WIN!")
                return color
        return Board.BLANK

    def change_turn(self) -> None:
        self.turn *= -1

    def line_range(self) -> list:
        size = self.size_of_board
        for v in self.stone_info:
            yield v
        
        for v in self.stone_info.T:
            yield v

        for i in np.arange(0, size):
            yield self.stone_info[0:1+i, size-1-i:size].diagonal()
        for i in np.arange(size-2, -1, -1):
            yield self.stone_info.T[0:1+i, size-1-i:size].diagonal()
            
        for i in np.arange(0, size):
            yield self.stone_info[:,::-1][0:1+i, size-1-i:size].diagonal()
        for i in np.arange(size-2, -1, -1):
            yield self.stone_info.T[::-1][0:1+i, size-1-i:size].diagonal()

    def print(self) -> None:
        visualized = self.stone_info.copy().astype(str)
        visualized[np.where(visualized == '-1')] = '○'
        visualized[np.where(visualized == '1')] = '●'
        visualized[np.where(visualized == '0')] = ' '
        for y in range(self.size_of_board):
            for x in range(self.size_of_board):
                print(visualized[x, y], end=' ')
            print()

class Ai:
    def __init__(self) -> None:
        pass

    def update_board(self, stone_info):
        self.stone_info = stone_info
    
    def judgment(self):
        

if __name__ == "__main__":
    main()