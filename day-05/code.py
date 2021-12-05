import numpy as np
from argparse import ArgumentParser


# To easily switch to input/test files
parser = ArgumentParser()
parser.add_argument("-i", "-input", default="input.txt", dest="file")
args = parser.parse_args()

ARROW_SEPARATOR = ' -> '

board_side, segments = 0, []
with open(args.file, "r") as file:
    lines = file.read().split("\n")
    for line in lines:
        line = line.split(ARROW_SEPARATOR)
        beginning = np.fromstring(line[0], dtype=int, sep=",")
        end = np.fromstring(line[1], dtype=int, sep=",")
        segments.append([*beginning, *end])
        board_side = max(board_side, *beginning, *end) + 1

without_diags = np.zeros((board_side, board_side))
diagonals = np.zeros((board_side, board_side))

for x1, y1, x2, y2 in segments:
    if x1 == x2:  # VERTICAL LINES
        first_row, col = min(y1, y2), x1
        length = abs(y1 - y2) + 1
        without_diags[first_row : first_row + length, col] += 1

    elif y1 == y2:  # HORIZONTAL LINES
        row, first_col = y1, min(x1, x2)
        length = abs(x1 - x2) + 1
        without_diags[row, first_col : first_col + length] += 1

    else:  # DIAGONALS
        length = abs(y1 - y2) + 1
        first_row, first_col = min(y1, y2), min(x1, x2)
        last_row, last_col = first_row + length, first_col + length

        is_top_left_to_bot_right = (y2 - y1) / (x2 - x1) > 0
        if is_top_left_to_bot_right:
            diagonals[first_row : last_row, first_col : last_col] += np.eye(length)
        else:
            diagonals[first_row : last_row, first_col : last_col] += np.fliplr(np.eye(length))

print("Part 1", without_diags[without_diags > 1].size)

with_diags = diagonals + without_diags
print("Part 2", with_diags[with_diags > 1].size)
