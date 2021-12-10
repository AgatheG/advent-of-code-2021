import numpy as np
from argparse import ArgumentParser


# To easily switch to input/test files
parser = ArgumentParser()
parser.add_argument("-i", "-input", default="input.txt", dest="file")
args = parser.parse_args()

with open(args.file, "r") as file:
    lines = file.read().split('\n')
    for idx, line in enumerate(lines):
        signal, output = line.split(' | ')
        lines[idx] = [signal.split(" "), output.split(" ")]

easy_nr_occurrences = 0
for _, output in lines:
    for digit in output:
        if len(digit) in {2, 3, 4, 7}:
            easy_nr_occurrences += 1
print("PART 1: The 'easy' numbers appear {} times".format(easy_nr_occurrences))

SEGMENTS = 'abcdefg'

SEGMENTS_TO_DIGIT = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9'
}

POTENTIAL_SEGMENTS = {
    2: dict(union={'c', 'f'}, intersection={'c', 'f'}),
    3: dict(union={'a', 'c', 'f'}, intersection={'a', 'c', 'f'}),
    4: dict(union={'b', 'c', 'd', 'f'}, intersection={'b', 'c', 'd', 'f'}),
    5: dict(union=set(list(SEGMENTS)), intersection={'a', 'd', 'g'}),
    6: dict(union=set(list(SEGMENTS)), intersection={'a', 'b','f', 'g'})
}

def replace(mapping, string):
    characters = []
    for s in string:
        characters += mapping[s]
    return "".join(sorted(characters))

sum_output_values = 0
for signal, output in lines:
    mapping = { l: set(list(SEGMENTS)) for l in SEGMENTS }
    found = set()
    for letters in [*signal, *output]:
        potential_segments = POTENTIAL_SEGMENTS.get(len(letters), None)
        if potential_segments is None:
            # case of digit 8: useless
            continue

        union, intersection = potential_segments.values()
        for key, charset in mapping.items():
            if len(charset) == 1:
                continue
            charset -= found
            if key in letters:
                charset &= union
            else:
                charset -= intersection
            if len(charset) == 1:
                found |= charset
        
    number = ''
    for digit in output:
        number += SEGMENTS_TO_DIGIT[replace(mapping, digit)]
    sum_output_values += int(number)

print("PART 2: The sum of the 4 digit numbers is {}".format(sum_output_values))
