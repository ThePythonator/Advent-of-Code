import os
from time import time
import heapq
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def count_trails(lines, sx, sy):
    count = 0
    q = [(0, sx, sy)]
    while len(q) > 0:
        h, x, y = heapq.heappop(q)
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            px, py = x + dx, y + dy
            if px >= 0 and px < len(lines[0]) and py >= 0 and py < len(lines):
                if lines[py][px] == h + 1:
                    if h == 8:
                        count += 1
                    else:
                        heapq.heappush(q, (h + 1, px, py))
    return count

def solve(lines):
    starting_points = []
    int_map = []
    for i, line in enumerate(lines):
        int_map.append([])
        for j, c in enumerate(line):
            if c == "0":
                starting_points.append((j, i))
            int_map[i].append(int(c))
    result = 0
    for x, y in starting_points:
        result += count_trails(int_map, x, y)
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
