import numpy as np
with open("input.txt", "r") as file:
    depths = np.array(file.read().split("\n"), dtype=int)

# PART 1
counter = 0
for i in range(1, len(depths)):
    if depths[i] > depths[i-1]:
        counter += 1
print(counter)

#PART 2
counter = 0
for i in range(len(depths) - 3):
    if depths[i] < depths[i+3]:
        counter += 1
print(counter)