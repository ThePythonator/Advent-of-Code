import os
from time import time
import heapq
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines, sx, sy):
    corrupted = [[False for _ in range(sx)] for _ in range(sy)]
    for i, line in enumerate(lines):
        x, y = [int(j) for j in line.split(",")]
        # heapq.heappush(incoming, (i, x, y))
        corrupted[y][x] = True

    q = [(0, 0, 0, 1, 0)]
    visited = {}
    while len(q) > 0:
        # input(q)
        c, x, y, dirx, diry = heapq.heappop(q)
        if visited.get((x, y), c + 1) <= c:
            continue
        visited[(x, y)] = c
        # print(c, x, y)
        if x == sx - 1 and y == sy - 1:
            # for l in corrupted: print("".join("#" if c else "." for c in l))
            return c
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if dx == -dirx and y == -diry:
                continue
            px, py = x + dx, y + dy
            if px < 0 or px >= len(corrupted[0]) or py < 0 or py >= len(corrupted):
                continue
            if not corrupted[py][px]:
                if visited.get((px, py), c + 2) > c + 1:
                    heapq.heappush(q, (c + 1, px, py, dx, dy))
                    
    return -1


############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample.txt")) as f:
    sample = [line.strip() for line in f.readlines()]

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

UNITS = ["s", "ms", "μs"]

SAMPLE_START = time()
sample_result = solve(sample[:12], 7, 7)
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
puzzle_result = solve(puzzle[:1024], 71, 71)
time_taken = time() - PUZZLE_START

unit_idx = 0
while time_taken < 1 and unit_idx < len(UNITS) - 1:
    time_taken *= 1000
    unit_idx += 1

print("Puzzle:")
print(f"Time: {time_taken:.2f}{UNITS[unit_idx]}")
print(f"Result: {puzzle_result}")
