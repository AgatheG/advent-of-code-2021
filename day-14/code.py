from argparse import ArgumentParser
import numpy as np
from collections import deque, Counter

# To easily switch to input/test files
parser = ArgumentParser()
parser.add_argument("-i", "-input", default="input.txt", dest="file")
parser.add_argument("-s", "-steps", default="10", dest="steps", type=int)
args = parser.parse_args()

with open(args.file, "r") as file:
    template, instructions = file.read().split('\n\n')

queue = deque([template[i] + template[i+1] for i in range(len(template)-1)])
instructions = instructions.split('\n')
instructions = dict([instruction.split(' -> ') for instruction in instructions])

def join(template):
    res = ""
    for i in range(0,len(template) - 1,2):
        res += template[i]
    return res + template[-1][1]

for i in range(args.steps):
    new_queue = deque()
    print(i)
    while queue:
        current = queue.popleft()
        elem = instructions[current]
        new_queue.append(current[0]+elem)
        new_queue.append(elem+current[1])
    queue = new_queue
m = Counter(join(queue)).most_common()
print(m[0][1] - m[-1][1])