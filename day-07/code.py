import numpy as np
from argparse import ArgumentParser


# To easily switch to input/test files
parser = ArgumentParser()
parser.add_argument("-i", "-input", default="input.txt", dest="file")
args = parser.parse_args()

with open(args.file, "r") as file:
    positions = np.fromstring(file.read(), dtype=int, sep=',')

# PART 1

alignment_position = int(np.median(positions))
amount_fuel = sum(np.abs(positions - alignment_position))

print("PART 1", amount_fuel)

# PART 2 LOCAL SEARCH

def f(o):
    return sum(range(o+1))

position_left, position_right = alignment_position - 1, alignment_position + 1
prev_fuel_amount_left = sum(map(f, np.abs(positions - alignment_position)))
prev_fuel_amount_right = prev_fuel_amount_left
try_left, try_right = True, True
while try_left or try_right:
    if try_right:
        current_amount = sum(map(f, np.abs(positions - position_right)))
        if prev_fuel_amount_right < current_amount:
            if not try_left:
                break
            try_right = False
        else:
            prev_fuel_amount_right = current_amount
            position_right += 1

    if position_left >= 0 and try_left:
        current_amount = sum(map(f, np.abs(positions - position_left)))
        if prev_fuel_amount_left < current_amount:
            if not try_right:
                break
            try_left = False
        else:
            prev_fuel_amount_left = current_amount
            position_left -= 1    

print("PART 2", min(prev_fuel_amount_left, prev_fuel_amount_right)) # 98119739
