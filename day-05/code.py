import numpy as np
from argparse import ArgumentParser


# To easily switch to input/test files
parser = ArgumentParser()
parser.add_argument("-i", "-input", default="input.txt", dest="file")
args = parser.parse_args()

segments = []
N = 0
with open(args.file, "r") as file:
    lines = file.read().split("\n")
    for line in lines:
        line = line.split(' -> ')
        x1, y1, x2, y2 = *line[0].split(','), *line[1].split(',')
        segments.append([int(x1), int(y1), int(x2), int(y2)])
        N = max(N, int(x1), int(x2))

A = np.zeros((N+1,N+1))
B = np.zeros((N+1,N+1))
for x1, y1, x2, y2 in segments:
    if x1==x2:
        i1, i2 = min(y1, y2), max(y1, y2)
        A[i1:i2+1,x1] += 1
        B[i1:i2+1,x1] += 1
    elif y1==y2:
        j1, j2 = min(x1, x2), max(x1, x2)
        A[y1,j1:j2+1] += 1
        B[y1,j1:j2+1] += 1
    else:
        i1, i2 = min(y1, y2), max(y1, y2)
        j1, j2 = min(x1, x2), max(x1, x2)
        size = i2 - i1 + 1
        is_left_to_right = (x2 < x1 and y2 < y1) or (y1 < y2 and x1 < x2)
        c = np.eye(size) if is_left_to_right else np.fliplr(np.eye(size))
        B[i1:i2+1, j1:j2+1] += c
print(B[B>1].size, A[A>1].size)
