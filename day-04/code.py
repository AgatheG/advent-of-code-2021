import numpy as np

class Board(object):
    BOARD_SIDE = 5
    MARKED = -1
    NO_WIN = 0

    def __init__(self, grid):
        self.values = grid.copy()
        self.cols = [0]*self.BOARD_SIDE
        self.rows = [0]*self.BOARD_SIDE

    def check(self, value):
        i, j = np.where(self.values == value)
        self.values[i, j] = self.MARKED

        if self.values[:,j].sum() == self.MARKED*self.BOARD_SIDE:
            return self.values[self.values != self.MARKED].sum() * value
        if self.values[i,:].sum() == self.MARKED*self.BOARD_SIDE:
            return self.values[self.values != self.MARKED].sum() * value
        return self.NO_WIN


with open("input.txt", "r") as file:
    drawn_numbers, *grids = file.read().split("\n\n")
    drawn_numbers = np.fromstring(drawn_numbers, dtype=int, sep=',')
    for i, grid in enumerate(grids):
        grid = grid.split('\n')
        grids[i] = np.array([row.lstrip().split(" ") for row in grid], dtype=int)


# PART 1
boards = set(Board(grid) for grid in grids)
for nr in drawn_numbers:
    for board in boards:
        score = board.check(nr)
        winning = score != Board.NO_WIN
        if winning:
            break
    if winning:
            break
print("PART 1: " + str(score))

# PART 2
boards, winners = set(Board(grid) for grid in grids), set()
for nr in drawn_numbers:
    for board in boards:
        score = board.check(nr)
        winning = score != Board.NO_WIN
        if winning:
            if len(boards) == 1:
                break
            else:
                winners.add(board)
                winning = False
    if winning:
        break
    boards -= winners
print("PART 2: " + str(score))