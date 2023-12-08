import os
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

instructions = lines[0]

nodes = {}
for i, line in enumerate(lines[2:]):
    k, v = line.split(" = ")
    l, r = v[1:-1].split(", ")
    nodes[k] = (l, r)

result = 0
index = 0
current = "AAA"
while current != "ZZZ":
    current = nodes[current]["LR".index(instructions[index])]
    result += 1
    index += 1
    if index == len(instructions):
        index = 0

print(f"Result: {result}")
