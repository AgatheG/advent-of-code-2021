import numpy as np
from collections import deque
from argparse import ArgumentParser

# To easily switch to input/test files
parser = ArgumentParser()
parser.add_argument("-i", "-input", default="input.txt", dest="file")
args = parser.parse_args()

with open(args.file, "r") as file:
    lines = file.read().split('\n')
    heightmap = np.array([list(line) for line in lines], dtype=int)

LIMIT_VALUE = 9
HEIGHT, WIDTH = heightmap.shape

# PART 1
low_points = []
sum_low_point_heights = 0
for row in range(HEIGHT):
    for col in range(WIDTH):
        current = heightmap[row,col]
        is_low_point = (col ==0 or current < heightmap[row, col-1]) \
            and (col == WIDTH - 1 or current < heightmap[row, col+1]) \
            and (row == 0 or current < heightmap[row-1, col]) \
            and (row == HEIGHT - 1 or current < heightmap[row+1, col])

        if is_low_point:
            low_points.append((row, col))
            sum_low_point_heights += heightmap[row, col]+1

print("PART 1", sum_low_point_heights)

# PART 2: Naive edition (DPS)
cluster_sizes, clusters = [], heightmap != LIMIT_VALUE

for row, col in low_points:
    neighbors, already_seen = deque([(row,col)]), set()
    cluster_sizes.append(0)

    while neighbors:
        row, col = neighbors.popleft()
        if (row, col) in already_seen:
            continue

        cluster_sizes[-1] += 1
        already_seen.add((row,col))

        if col > 0 and clusters[row, col-1]:
            neighbors.appendleft((row, col-1))
        if col < WIDTH - 1 and clusters[row, col+1]:
            neighbors.appendleft((row, col+1))
        if row > 0 and clusters[row-1, col]:
            neighbors.appendleft((row-1, col))
        if row < HEIGHT - 1 and clusters[row+1, col]:
            neighbors.appendleft((row+1, col))

third_largest_size, second_largest_size, largest_size = sorted(cluster_sizes)[-3:]
print("PART 2", third_largest_size*second_largest_size*largest_size)

# PART 2: Sexier edition?
import scipy.ndimage.measurements as mnts

clusters, nr_clusters = mnts.label(clusters)
cluster_sizes = [clusters[clusters == cluster].size for cluster in range(1, nr_clusters+1)]

third_largest_size, second_largest_size, largest_size = sorted(cluster_sizes)[-3:]
print("PART 2", third_largest_size*second_largest_size*largest_size)
