from argparse import ArgumentParser
from collections import defaultdict

# To easily switch to input/test files
parser = ArgumentParser()
parser.add_argument("-i", "-input", default="input.txt", dest="file")
parser.add_argument("-s", "-steps", default="10", dest="steps", type=int)
args = parser.parse_args()

with open(args.file, "r") as file:
    template, instructions = file.read().split('\n\n')

# Parse input
SEPARATOR = ' -> '
NR_STEPS = args.steps

pair_occurrences, polymer_occurrences = defaultdict(int), defaultdict(int)
for idx in range(len(template) - 1):
    pair_occurrences[template[idx] + template[idx + 1]] += 1
    polymer_occurrences[template[idx]] += 1
polymer_occurrences[template[-1]] += 1

instructions = instructions.split('\n')
instructions = dict([instruction.split(SEPARATOR) for instruction in instructions])

# PARTS 1 & 2
for step in range(NR_STEPS):
    new_letter_occurrences = defaultdict(int)
    while pair_occurrences:
        pair, occurrences = pair_occurrences.popitem()
        elem = instructions[pair]

        new_letter_occurrences[pair[0] + elem] += occurrences
        new_letter_occurrences[elem + pair[1]] += occurrences
        polymer_occurrences[elem] += occurrences

    pair_occurrences = new_letter_occurrences

quantities = polymer_occurrences.values()
print(max(quantities) - min(quantities))
