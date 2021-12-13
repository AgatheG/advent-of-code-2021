from argparse import ArgumentParser
import numpy as np

# To easily switch to input/test files
parser = ArgumentParser()
parser.add_argument("-i", "-input", default="input.txt", dest="file")
args = parser.parse_args()

with open(args.file, "r") as file:
    dots, instructions = file.read().split('\n\n')
    dots, instructions = dots.split('\n'), instructions.split('\n')

last_row, last_col = 0, 0
for i, dot in enumerate(dots):
    col, row = dot.split(',')
    col, row = int(col), int(row)
    dots[i] = [row, col]
    last_row, last_col = max(last_row, row), max(last_col, col)

paper = np.zeros((last_row+1, last_col+1))
for row, col in dots:
    paper[row, col] = 1

# PART 1
for i, instruction in enumerate(instructions):
    _, value = instruction.split('=')
    axis, value = _[-1], int(value)
    if axis == 'x':
        left, right = paper[:, :value], np.fliplr(paper[:, value+1:])
        if left.shape[1] < right.shape[1]:
            right[:, -left.shape[1]:] = np.maximum(left, right[:, -left.shape[1]:])
            paper = right
        else:
            left[:, -right.shape[1]:] = np.maximum(right, left[:, -right.shape[1]:])
            paper = left
    elif axis == 'y':
        up, down = paper[:value, :], np.flipud(paper[value+1:, :])
        if up.shape[0] < down.shape[0]:
            down[-up.shape[0]:, :] = np.maximum(up, down[-up.shape[0]:, :])
            paper = down
        else:
            up[-down.shape[0]:, :] = np.maximum(down, up[-down.shape[0]:, :])
            paper = up
    if i == 0:
        print("PART 1", np.count_nonzero(paper))

# PART 2
paper = paper.astype(int).astype(str)
paper[paper=='0'] = '.'
paper[paper=='1'] = '#'
for row in paper:
    print("".join(row))
