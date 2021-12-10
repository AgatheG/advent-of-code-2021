import numpy as np
from collections import deque
from argparse import ArgumentParser

# To easily switch to input/test files
parser = ArgumentParser()
parser.add_argument("-i", "-input", default="input.txt", dest="file")
args = parser.parse_args()

with open(args.file, "r") as file:
    lines = file.read().split('\n')

CLOSING_CHARS_CORRUPTION = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

CLOSING_CHARS_COMPLETION = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

MATCHING_CHARS = {
    '(': ')',
    '[':']',
    '{': '}',
    '<': '>'
}

# PARTS 1 & 2

syntax_error_score, autocomplete_scores = 0, list()
for line in lines:
    opening_chars, line_is_corrupt = deque(), False
    for char in line:
        if char in MATCHING_CHARS:
            opening_chars.appendleft(char)
        else:
            last_opening_char = opening_chars.popleft()
            if MATCHING_CHARS[last_opening_char] != char:
                syntax_error_score += CLOSING_CHARS_CORRUPTION[char]
                line_is_corrupt = True
                break

    if not line_is_corrupt:
        autocomplete_line_score = 0
        while opening_chars:
            closing_char_score = CLOSING_CHARS_COMPLETION[MATCHING_CHARS[opening_chars.popleft()]]
            autocomplete_line_score = autocomplete_line_score*5 + closing_char_score
        autocomplete_scores.append(autocomplete_line_score)

print("PART 1: The total syntax error score is {}".format(syntax_error_score))
print("PART 2: The middle score is {}".format(np.median(autocomplete_scores)))
