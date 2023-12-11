import os
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

SIZE = 1000000

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]


h_expansions = set()
v_expansions = set()

for i, line in enumerate(lines):
    if "#" not in line:
        h_expansions.add(i)

for i in range(len(lines[0])):
    if all(lines[j][i] == "." for j in range(len(lines))):
        v_expansions.add(i)

nodes = []
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "#":
            nodes.append((j, i))

def get_expansions_overlaps(expansions, a, b):
    return len([i for i in range(a, b+1) if i in expansions])

def get_dist(a, b):
    c = min(a[0], b[0])
    d = max(a[0], b[0])
    e = min(a[1], b[1])
    f = max(a[1], b[1])
    h_extra = get_expansions_overlaps(v_expansions, c, d)
    v_extra = get_expansions_overlaps(h_expansions, e, f)
    return d - c + f - e + (h_extra + v_extra) * (SIZE - 1)

distances = []
for i in range(len(nodes)):
    for j in range(i+1, len(nodes)):
        distances.append(get_dist(nodes[i], nodes[j]))

result = sum(distances)
print(f"Result: {result}")
