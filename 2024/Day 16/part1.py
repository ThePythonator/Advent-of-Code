import os
from time import time
import heapq
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def turn_left(dx, dy):
    if dx == 0:
        return dy, dx
    else: # dy == 0
        return dy, -dx

def turn_right(dx, dy):
    if dx == 0:
        return -dy, dx
    else: # dy == 0
        return dy, dx

def solve(lines):
    start = end = None
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "S":
                start = (j, i)
            elif c == "E":
                end = (j, i)
    q = [(0, start[0], start[1], 1, 0)]
    best_visited = [[{} for _ in range(len(lines[0]))] for _ in range(len(lines))]
    while len(q) > 0:
        c, x, y, dx, dy = heapq.heappop(q)
        # print(c, x, y, dx, dy)
        if (x, y) == end:
            return c
        if best_visited[y][x].get((dx, dy), c + 1) <= c:
            continue
        best_visited[y][x][(dx, dy)] = c
        lx, ly = turn_left(dx, dy)
        rx, ry = turn_right(dx, dy)
        # Check straight ahead:
        for nc, ndx, ndy in [(c+1, dx, dy), (c+1001, lx, ly), (c+1001, rx, ry)]:
            nx, ny = x+ndx, y+ndy
            if lines[ny][nx] != "#":
                heapq.heappush(q, (nc, nx, ny, ndx, ndy))
    
    return None


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
