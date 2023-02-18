import pandas as pd
import numpy as np

def main() -> None:
    board = Board(10)
    for i in range(5):
        board.put_stone((i+3, -i+8))
    board.print()
    board.check_winner()

    ai = Ai(board)
    ai.marking(np.array([0, 0, 1, -1, 1, 0, 1, 0, 1, 0]))


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
        self.stone_info = np.zeros([self.size_of_board] * 2, dtype=int)
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
            yield self.stone_info[0:1 + i, size - (1+i):size].diagonal()
        for i in np.arange(size-2, -1, -1):
            yield self.stone_info.T[0:1+i, size - (1+i):size].diagonal()
            
        for i in np.arange(0, size):
            yield self.stone_info[:,::-1][0:1+i, size - (1+i):size].diagonal()
        for i in np.arange(size-2, -1, -1):
            yield self.stone_info.T[::-1][0:1+i, size - (1+i):size].diagonal()

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
    BLANK, BLACK, WHITE, BLOCKED = 0, 1, -1, 2
    color_dict = {
        BLANK : "BLANK",
        BLACK : "BLACK",
        WHITE : "WHITE",
        BLOCKED : "BLOCKED"
    }

    def __init__(self, board) -> None:
        self.board : Board = board
    
    def judgment(self):
        # 한 줄씩 따로 생각한다.
        # 각 줄마다 alpha, beta, charlie, delta 및 각각의 마킹에 원형, blanked, blocked의 변형 위치를 기록

        for i, line in enumerate(self.line_range()):
            i %= self.board.size_of_board
            if line.size == 0:
                continue
            self.marking(line)
            # for j, info in enumerate(line_info):
            #     if dir == 'x':
            #         index = i, j
            #     elif dir == 'y':
            #         index = j, i
            #     elif dir == 'xy1':
            #         index = j, size+j - (i+1)
            #     elif dir == 'xy2':
            #         index = i+j+1, j
            #     elif dir == '-xy1':
            #         index = j, i-j
            #     elif dir == '-xy2':
            #         index = i+1, size - (j+1)

    def marking(self, line):
        marker = pd.Series({i:0 for i in range(line.size)})
        df = {
            "info" : line,
            "score level" : marker,
            "empty level" : marker,
            "is blocked" : False
        }
        line_markers = pd.DataFrame(df)
        print(line)
        print(line_markers)

        for i in range(line_markers.shape[0]):
            if line_markers.loc[i, "info"] == -1 * self.board.turn:
                for dir in [-1, 1]:
                    self.spreading_blocked(line_markers, i, dir)
        print("marking is blocekd")
        print(line_markers)

        stack = 0
        for i in range(line_markers.shape[0]):
            if line_markers.loc[i, "info"] == self.board.turn:
                stack += 1
            elif stack != 0:
                is_blocked = line_markers.loc[i-1, "is blocked"]
                print(i-1, is_blocked)
                self.spreading_level(line_markers, i, stack, is_blocked)
                stack = 0
        print("marking levels")
        print(line_markers)



    def spreading_level(self, line_markers, i, stack, is_blocked, dir=0, blank_entry=0):
        # self.turn에 해당하는 칸 앞뒤 두칸씩 score level을 stack만큼 올립니다.
        # 이때 self.turn에 해당하는 칸과 score level을 올리는 칸 사이 거리만큼 empty level을 올립니다.
        # 또한 score level을 올리기 전 BLOCKED를 만나면 그 칸을 포함해 그 방향으로는 모든 level을 올리지 않으며
        # self.turn을 만나면 그 칸을 건너뛰고 다음 칸의 level을 올립니다.
        # ex) __OO_OX__에 대해 score level : 23OO3X__, empty level : 11OO_OX__

        for blank in range(2):
            idx = i + blank
            if dir == -1:
                break
            if blank_entry > blank:
                continue
            if i + blank >= line_markers.shape[0]:
                break
            if line_markers.loc[idx, "info"] == -1 * self.board.turn:
                break
            if line_markers.loc[idx, "info"] == self.board.turn:
                self.spreading_level(line_markers, i + 1, stack, is_blocked, dir=1, blank_entry=blank)
                break
            line_markers.loc[idx, "score level"] += stack
            line_markers.loc[idx, "empty level"] += blank
            if is_blocked == True:
                line_markers.loc[idx, "is blocked"] = True
            print(i, stack, is_blocked)

        for blank in range(2):
            idx = (i - 1 - stack) - blank
            if dir == 1:
                break
            if blank_entry > blank:
                continue
            if (i - 1 - stack) - blank < 0:
                break
            if line_markers.loc[idx, "info"] == -1 * self.board.turn:
                break
            if line_markers.loc[idx, "info"] == self.board.turn:
                self.spreading_level(line_markers, i - 1, stack, is_blocked, dir=-1, blank_entry=blank)
                break
            line_markers.loc[idx, "empty level"] += blank
            line_markers.loc[idx, "score level"] += stack
            if is_blocked == True:
                line_markers.loc[idx, "is blocked"] = True
            print(i - 1 - stack, blank_entry, is_blocked)

    def spreading_blocked(self, line_markers, i, dir):
        if line_markers.loc[i + dir, "info"] != self.board.turn:
            return
        line_markers.loc[i + dir, "is blocked"] = True
        self.spreading_blocked(line_markers, i + dir, dir)

    def line_range(self) -> list:
        size = self.board.size_of_board
        for v in self.board.stone_info:
            yield v
        
        for v in self.board.stone_info.T:
            yield v

        for i in np.arange(0, size):
            yield self.board.stone_info[0:1+i, size-1-i:size].diagonal()
        for i in np.arange(size-2, -1, -1):
            yield self.board.stone_info.T[0:1+i, size-1-i:size].diagonal()
        yield np.array([])
            
        for i in np.arange(0, size):
            yield self.board.stone_info[:,::-1][0:1+i, size-1-i:size].diagonal()
        for i in np.arange(size-2, -1, -1):
            yield self.board.stone_info.T[::-1][0:1+i, size-1-i:size].diagonal()
        yield np.array([])

if __name__ == "__main__":
    main()