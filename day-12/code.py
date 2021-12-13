from argparse import ArgumentParser
from collections import defaultdict, deque, Counter

# To easily switch to input/test files
parser = ArgumentParser()
parser.add_argument("-i", "-input", default="input.txt", dest="file")
args = parser.parse_args()

SEPARATOR = '-'
START = 'start'
END = 'end'

with open(args.file, "r") as file:
    raw_mapping = file.read().split('\n')
    mapping = defaultdict(list)
    for p in raw_mapping:
        start, end = p.split(SEPARATOR)
        mapping[start].append(end)
        mapping[end].append(start)

# PART 1
queue = deque([[cave] for cave in mapping[START]])
nr_paths = 0
while queue:
    current_path = queue.popleft()
    uniques = set(current_path)
    for cave in mapping[current_path[-1]]:
        if cave == START:
            continue
        if cave == END:
            nr_paths += 1
        elif cave.isupper() or cave not in uniques:
            queue.appendleft(current_path + [cave])

print("PART 1: There are {} available paths.".format(nr_paths))

# PART 2
queue = deque([[cave] for cave in mapping[START]])
nr_paths = 0
while queue:
    current_path = queue.popleft()
    count = Counter([cave for cave in current_path if cave.islower()])
    can_visit_small = not count or count.most_common(1)[0][1] <= 1
    for cave in mapping[current_path[-1]]:
        if cave == START:
            continue
        if cave == END:
            nr_paths += 1
        elif cave.isupper() or cave not in count or (can_visit_small and count[cave] == 1):
            queue.appendleft(current_path + [cave])

print("PART 2: There are {} available paths.".format(nr_paths))
