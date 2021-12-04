import numpy as np

class Board(object):
    BOARD_SIDE = 5
    MARKED = -1
    NO_WIN = 0

    def __init__(self, grid):
        self.values = grid

    def check(self, value):
        i, j = np.where(self.values == value)
        if not i.size: #  Value is not in the board
            return self.NO_WIN

        self.values[i, j] = self.MARKED

        if self.values[:, j].sum() == self.MARKED * self.BOARD_SIDE or\
            self.values[i, :].sum() == self.MARKED * self.BOARD_SIDE:
            return self.values[self.values != self.MARKED].sum() * value
        return self.NO_WIN


boards = set()
with open("input.txt", "r") as file:
    drawn_numbers, *grids = file.read().split("\n\n")
    drawn_numbers = np.fromstring(drawn_numbers, dtype=int, sep=',')
    for grid in grids:
        grid = grid.split('\n')
        grid = np.array([row.lstrip().split(" ") for row in grid], dtype=int)
        boards.add(Board(grid))

# PARTS 1 & 2
winners = set()
for number in drawn_numbers:
    for board in boards:
        score = board.check(number)
        if score != Board.NO_WIN:
            if not winners:
                print("Part 1: The first board to win has a score of {}".format(score))
            winners.add(board)
    boards -= winners
    if not boards:
        break

print("Part 2: The last board to win has a score of {}".format(score))
