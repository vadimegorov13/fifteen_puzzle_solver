from random import randint, seed
from copy import deepcopy

MAX_INDEX = 4
BOARD = [["1 ", "2 ", "3 ", "4 "], ["5 ", "6 ", "7 ", "8 "],
         ["9 ", "10", "11", "12"], ["13", "14", "15", "__"]]
SHUFFLE = 20

class FP:
    # constructor
    def __init__(self):
        self.goal = deepcopy(BOARD)
        self.board = deepcopy(BOARD)
        self.e_tile = [MAX_INDEX - 1, MAX_INDEX - 1]
        self.shifts = {0: self.shift_up, 1: self.shift_down,
                       2: self.shift_left, 3: self.shift_right}

    def set_start(self, start):
        self.board = start
        for i in range(MAX_INDEX):
            for j in range(MAX_INDEX):
                if self.board[i][j] == "__":
                    self.e_tile = [i, j]

    def display(self):
        for i in range(MAX_INDEX):
            for j in range(MAX_INDEX):
                print(self.board[i][j], end=" ")
            print()
        print()

    def shuffle_puzzle(self):
        # shuffle the puzzle
        seed()
        for _ in range(SHUFFLE):
            shift_num = randint(0, 3)
            self.shifts[shift_num](self.board, self.e_tile)

    def shift(self, board, e_tile, x, y):
        # check if shift is legal
        if not self.legal_shift(e_tile, x, y):
            return board, e_tile

        # Swap empty tile with a number tile
        board[e_tile[0]][e_tile[1]], board[e_tile[0] + x][e_tile[1] + y] \
            = board[e_tile[0] + x][e_tile[1] + y], board[e_tile[0]][e_tile[1]]

        # Update coordinates of an empty tile
        e_tile[0], e_tile[1] =  e_tile[0] + x, e_tile[1] + y
        return board, e_tile

    def shift_up(self, board, e_tile):
        return self.shift(board, e_tile, -1, 0)

    def shift_down(self, board, e_tile):
        return self.shift(board, e_tile, 1, 0)

    def shift_left(self, board, e_tile):
        return self.shift(board, e_tile, 0, -1)

    def shift_right(self, board, e_tile):
        return self.shift(board, e_tile, 0, 1)

    # Check if shift is not going out of bounds of a board
    def legal_shift(self, e_tile, x, y):
        if e_tile[0] + x < 0 :
            return False
        if e_tile[0] + x > 3 :
            return False
        if e_tile[1] + y < 0:
            return False
        if e_tile[1] + y > 3:
            return False
        return True