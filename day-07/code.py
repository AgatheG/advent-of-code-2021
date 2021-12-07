import numpy as np
from argparse import ArgumentParser


# To easily switch to input/test files
parser = ArgumentParser()
parser.add_argument("-i", "-input", default="input.txt", dest="file")
args = parser.parse_args()

with open(args.file, "r") as file:
    positions = np.fromstring(file.read(), dtype=int, sep=',')

unique_positions = np.unique(positions)
lowest_amount_fuel = float('inf')
for horizontal_position in unique_positions:
    amount_fuel = sum(np.abs(positions - horizontal_position))

    if amount_fuel < lowest_amount_fuel:
        lowest_amount_fuel = amount_fuel
        alignment_position = horizontal_position

print("PART 1", lowest_amount_fuel)

