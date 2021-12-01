import numpy as np
with open("input.txt", "r") as file:
    depths = np.array(file.read().split("\n"), dtype=int)

# First (naive) method: for loops
# PART 1
counter = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        counter += 1

#PART 2
counter = 0
for i in range(len(depths) - 3):
    if depths[i] < depths[i+3]:
        counter += 1

# Second method: using numpy
# PART 1
short = np.zeros(len(depths))
short[:-1] = depths[1:]
print("Part 1 : %s" % np.count_nonzero(short > depths))

# PART 2
left, right = depths[:-3], depths[3:]
print("Part 2 : %s" % np.count_nonzero(right > left))
