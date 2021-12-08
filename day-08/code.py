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

S = 0
for signal, output in lines:
    for digit in output:
        if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit)==7:
            S +=1
print(S)

D = {
    0: {"a", "b", "c", "e", "f", "g"},
    1: {"c", "f"},
    2: {"a", "c", "d", "e", "g"},
    3: {"a", "c", "d", "f", "g"},
    4: {"b", "c", "d", "f"},
    5: {"a", "b", "d", "f", "g"},
    6: {"a", "b", "d", "e", "f", "g"},
    7: {"a", "c", "f"},
    8: {"a", "b", "c", "d", "e", "f", "g"},
    9: {"a", "b", "c", "d", "f", "g"}
}

I = {
    "".join(sorted(v)): str(k) for k, v in D.items()
}
K = {
    2: (1,),
    3: (7,),
    4: (4,),
    5: (2, 3, 5),
    6: (0, 6, 9),
    7: (8,),
}

def replace(mapping, string):
    characters = []
    for s in string:
        characters += mapping[s]
    return "".join(sorted(characters))

SS = 0
for signal, output in lines:
    mapping = {
        l: set(list('abcdefg')) for l in 'abcdefg'
    }
    found = set()
    for letters in [*signal, *output]:
        potentials, qotentials = set(), set(list('abcdefg'))
        for d in K[len(letters)]:
            potentials |= D[d]
            qotentials &= D[d]
        s = set()
        for key, charset in mapping.items():
            if len(charset) == 1:
                continue
            charset -= found
            if key in letters:
                charset &= potentials
            else:
                charset -= qotentials
            if len(charset) == 1:
                found |= charset
    number = ''
    for digit in output:
        number += I[replace(mapping, digit)]
    SS += int(number)
print(SS)