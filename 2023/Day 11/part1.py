import os
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

expanded = []
for line in lines:
    if "#" not in line:
        expanded.append(line)
    expanded.append(line)

for i in range(len(lines[0])-1, -1, -1):
    if all(lines[j][i] == "." for j in range(len(lines))):
        for j in range(len(expanded)):
            expanded[j] = expanded[j][:i] + "." + expanded[j][i:]

nodes = []
for i, expline in enumerate(expanded):
    for j, c in enumerate(expline):
        if c == "#":
            nodes.append((j, i))

def get_dist(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

distances = []
for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        distances.append(get_dist(nodes[i], nodes[j]))

result = sum(distances)
print(f"Result: {result}")
