with open("input.txt", "r") as file:
    commands = file.read().split("\n")

# PART 1

COMMANDS = {
    "forward": lambda horizontal, depth, value: (horizontal + value, depth),
    "down": lambda horizontal, depth, value: (horizontal, depth + value),
    "up": lambda horizontal, depth, value: (horizontal, depth - value),
}

horizontal, depth = 0, 0
for command in commands:
    action, value = command.split(" ")
    horizontal, depth = COMMANDS[action](horizontal, depth, int(value))

print("PART 1", horizontal*depth)

# PART 2

COMMANDS = {
    "forward": lambda horizontal, depth, aim, value: (horizontal + value, depth + value * aim, aim),
    "down": lambda horizontal, depth, aim, value: (horizontal, depth, aim + value),
    "up": lambda horizontal, depth, aim, value: (horizontal, depth, aim - value),
}

horizontal, depth, aim = 0, 0, 0
for command in commands:
    action, value = command.split(" ")
    horizontal, depth, aim = COMMANDS[action](horizontal, depth, aim, int(value))

print("PART 2", horizontal*depth)
