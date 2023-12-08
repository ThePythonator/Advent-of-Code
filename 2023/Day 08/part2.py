import os, math
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

instructions = lines[0]

nodes = {}
currents = []
for i, line in enumerate(lines[2:]):
    k, v = line.split(" = ")
    l, r = v[1:-1].split(", ")
    nodes[k] = (l, r)
    if k[-1] == "A":
        currents.append(k)

result = 0
index = 0
count = 0
lasts = [[] for _ in range(len(currents))]
while any(len(last) < 2 for last in lasts):
    count = 0
    choice = "LR".index(instructions[index])
    for i in range(len(currents)):
        currents[i] = nodes[currents[i]][choice]
        if currents[i][-1] == "Z":
            count += 1
            lasts[i].append(result)
    result += 1
    index += 1
    if index == len(instructions):
        index = 0

diffs = [last[-1] - last[-2] for last in lasts]
result = math.lcm(*diffs)

print(f"Result: {result}")
