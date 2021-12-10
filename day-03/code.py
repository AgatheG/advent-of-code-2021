import numpy as np
with open("input.txt", "r") as file:
    bit_numbers = file.read().split("\n")
    REPORT = np.array([list(b) for b in bit_numbers], dtype=int)

#bits = np.array([2**i for i in range(REPORT.shape[1]-1, -1, -1)])
#def convert_to_decimal(array):
#    return (bits*array).sum()

# Smarter conversion?
def convert_to_decimal(array):
    return int("".join(array.astype(str)), 2)

def most_common_bit(array):
    length = array.shape[0]
    return array.sum(axis=0) // (length/2)

# PART 1
most_common_bits = most_common_bit(REPORT).astype(int)
gamma, eps = convert_to_decimal(most_common_bits), convert_to_decimal(1 - most_common_bits)
print("PART 1 : The power consumption is {:.0f}".format(gamma * eps))

# PART2
oxygen_ratings, co2_ratings = REPORT, REPORT
for i in range(REPORT.shape[1]):
    if len(oxygen_ratings) > 1:
        indices_to_keep = oxygen_ratings[:,i] == most_common_bit(oxygen_ratings[:,i])
        oxygen_ratings = oxygen_ratings[indices_to_keep]
    if len(co2_ratings) > 1:
        indices_to_keep = co2_ratings[:,i] == (1 - most_common_bit(co2_ratings[:,i]))
        co2_ratings = co2_ratings[indices_to_keep]

    if len(oxygen_ratings) * len(co2_ratings) == 1:
        # early abort
        break

life_support = convert_to_decimal(oxygen_ratings[0]) * convert_to_decimal(co2_ratings[0])
print("PART 2 : The life support rating is {:.0f}".format(life_support))
