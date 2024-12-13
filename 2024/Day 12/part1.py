import os
from time import time
from queue import Queue
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def search(lines, visited, sx, sy):
    name = lines[sy][sx]
    area = 0
    perimeter = 0
    q = Queue()
    q.put((sx, sy))
    while not q.empty():
        x, y = q.get()
        if (x, y) in visited:
            continue
        area += 1
        visited.add((x, y))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            px, py = x + dx, y + dy
            if px < 0 or px >= len(lines[0]) or py < 0 or py >= len(lines):
                perimeter += 1
                continue
            if lines[py][px] == name:
                if (px, py) not in visited:
                    q.put((px, py))
            else:
                perimeter += 1
    return name, area, perimeter

def solve(lines):
    regions = []
    visited = set()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if (j, i) not in visited:
                regions.append(search(lines, visited, j, i))
    result = 0
    for plant, area, perimeter in regions:
        result += area * perimeter
    return result


############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample.txt")) as f:
    sample = [line.strip() for line in f.readlines()]

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

UNITS = ["s", "ms", "μs"]

SAMPLE_START = time()
sample_result = solve(sample)
time_taken = time() - SAMPLE_START

unit_idx = 0
while time_taken < 1 and unit_idx < len(UNITS) - 1:
    time_taken *= 1000
    unit_idx += 1

print("Sample:")
print(f"Time: {time_taken:.2f}{UNITS[unit_idx]}")
print(f"Result: {sample_result}")
print()

PUZZLE_START = time()
puzzle_result = solve(puzzle)
time_taken = time() - PUZZLE_START

unit_idx = 0
while time_taken < 1 and unit_idx < len(UNITS) - 1:
    time_taken *= 1000
    unit_idx += 1

print("Puzzle:")
print(f"Time: {time_taken:.2f}{UNITS[unit_idx]}")
print(f"Result: {puzzle_result}")
