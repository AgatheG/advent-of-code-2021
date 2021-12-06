import numpy as np
from argparse import ArgumentParser


# To easily switch to input/test files
parser = ArgumentParser()
parser.add_argument("-i", "-input", default="input.txt", dest="file")
parser.add_argument("-d", "-days", default="80", dest="days", type=int)
args = parser.parse_args()

with open(args.file, "r") as file:
    lanternfishes = np.fromstring(file.read(), dtype=int, sep=',')

NEW_BORN_BIRTH_CYCLE_LENGTH = 8
BIRTH_CYCLE_LENGTH = 6
MAX_TIMER_VALUE = max(BIRTH_CYCLE_LENGTH, NEW_BORN_BIRTH_CYCLE_LENGTH)

lanternfishes_per_timer = np.zeros(MAX_TIMER_VALUE + 1)
idx, counts = np.unique(lanternfishes, return_counts=True)
lanternfishes_per_timer[idx] = counts

DAYS = args.days
# PARTS 1 & 2
for i in range(DAYS):
    new_ones = lanternfishes_per_timer[0]
    lanternfishes_per_timer[: MAX_TIMER_VALUE] = lanternfishes_per_timer[1: ]
    lanternfishes_per_timer[MAX_TIMER_VALUE] = new_ones
    lanternfishes_per_timer[BIRTH_CYCLE_LENGTH] += new_ones

print("There would be {} lanternfishes after {} days.".format(sum(lanternfishes_per_timer), DAYS))
