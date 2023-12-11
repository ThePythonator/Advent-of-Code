import os
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

for i, line in enumerate(lines):
    if "S" in line:
        start_pos = (line.index("S"), i)

lookup = {
    "-": [(-1, 0), (1, 0)],
    "|": [(0, -1), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(-1, 0), (0, 1)],
    "L": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)]
}

def get_valid_adjacents(cx, cy, start=False):
    v = []
    for (dx, dy), valid in zip([(-1, 0), (1, 0), (0, -1), (0, 1)], ["L-F", "J-7", "7|F", "J|L"]):
        if start or (dx, dy) in lookup[lines[cy][cx]]:
            x, y = [cx + dx, cy + dy]
            if x >= 0 and x < len(lines[0]) and y >= 0 and y < len(lines) and lines[y][x] in valid:
                v.append((x,y))
    return v


q = get_valid_adjacents(*start_pos, start=True)
visited = set([start_pos])

while len(q) > 0:
    pos = q.pop(0)
    visited.add(pos)
    options = get_valid_adjacents(*pos)
    for option in options:
        if option not in visited:
            q.append(option)

result = len(visited) // 2
print(f"Result: {result}")
