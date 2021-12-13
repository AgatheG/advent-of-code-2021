import numpy as np
from collections import deque
from argparse import ArgumentParser


# To easily switch to input/test files
parser = ArgumentParser()
parser.add_argument("-i", "-input", default="input.txt", dest="file")
args = parser.parse_args()

with open(args.file, "r") as file:
    energy_levels = file.read().split("\n")
    energy_levels = np.array([list(e) for e in energy_levels], dtype=int)
GRID_SIZE = energy_levels.shape[0]

# PARTS 1 & 2

def propagate_flash(row, col, flashing_octopuses, already_flashed):
    energy_levels[row, col] += 1
    if energy_levels[row, col] > 9:
        already_flashed.add((row, col))
        flashing_octopuses.append((row, col))

step, first_step_with_sync = 0, None
flashes = 0
while step < 100 or not first_step_with_sync:
    energy_levels += 1
    flashing_octopuses = np.argwhere(energy_levels > 9).tolist()
    already_flashed = set([(row, col) for row, col in flashing_octopuses])

    flashes_in_step = 0
    while flashing_octopuses:
        row, col = flashing_octopuses.pop()
        flashes_in_step += 1
        energy_levels[row, col] = 0

        if row > 0:
            if (row-1,col) not in already_flashed:
                propagate_flash(row - 1, col, flashing_octopuses, already_flashed)
            if col > 0 and (row - 1,col - 1) not in already_flashed:
                propagate_flash(row - 1, col - 1, flashing_octopuses, already_flashed)
            if col < GRID_SIZE-1 and (row - 1,col + 1) not in already_flashed:
                propagate_flash(row - 1, col + 1, flashing_octopuses, already_flashed)

        if col > 0 and (row,col-1) not in already_flashed:
            propagate_flash(row, col-1, flashing_octopuses, already_flashed)

        if row < GRID_SIZE-1:
            if (row+1,col) not in already_flashed:
                propagate_flash(row + 1, col, flashing_octopuses, already_flashed)
            if col > 0 and (row + 1,col - 1) not in already_flashed:
                propagate_flash(row + 1, col - 1, flashing_octopuses, already_flashed)
            if col < GRID_SIZE-1 and (row + 1,col + 1) not in already_flashed:
                propagate_flash(row + 1, col + 1, flashing_octopuses, already_flashed)

        if col < GRID_SIZE-1 and (row,col+1) not in already_flashed:
            propagate_flash(row, col+1, flashing_octopuses, already_flashed)

    flashes += flashes_in_step
    step += 1
    if step == 100:
        nr_flashes_after_100_step = flashes
    if flashes_in_step == GRID_SIZE*GRID_SIZE:
        first_step_with_sync = step

print("PART 1: After 100 steps, there have been {} flashes".format(nr_flashes_after_100_step))
print("PART 2: The octopuses flash together for the first time at step {}".format(first_step_with_sync))
