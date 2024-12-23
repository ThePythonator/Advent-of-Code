import os
from time import time
import heapq
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def find_route(start, end, lines):
    q = [(0, *start)]
    best = {}
    while len(q) > 0:
        t, x, y = heapq.heappop(q)
        if best.get((x,y), t+1) < t:
            continue
        best[(x,y)] = t
        if (x, y) == end:
            # Work out route
            route = [end]
            c = t
            while (x, y) != start:
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    px, py = x+dx, y+dy
                    if best.get((px,py), c) == c - 1:
                        c -= 1
                        route.append((px, py))
                        x,y = px,py
                        break
            return t, route[::-1]
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            px, py = x+dx, y+dy
            if lines[py][px] != "#":
                heapq.heappush(q, (t+1, px, py))
    return -1, []

def _solve(start, end, lines, min_save):
    best_t, route = find_route(start, end, lines)
    lookup = {pos: i for i, pos in enumerate(route)}
    count = 0
    for i, (x, y) in enumerate(route):
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            px, py = x+dx, y+dy
            if lines[py][px] == "#":
                # Only worth cheating through walls
                idx = lookup.get((px+dx, py+dy), 0)
                if idx - i - 2 >= min_save:
                    count += 1
    return count

def solve(lines, min_save):
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "S":
                start = (j, i)
            elif c == "E":
                end = (j, i)
    return _solve(start, end, lines, min_save)


############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample.txt")) as f:
    sample = [line.strip() for line in f.readlines()]

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

UNITS = ["s", "ms", "μs"]

SAMPLE_START = time()
sample_result = solve(sample, 0)
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
puzzle_result = solve(puzzle, 100)
time_taken = time() - PUZZLE_START

unit_idx = 0
while time_taken < 1 and unit_idx < len(UNITS) - 1:
    time_taken *= 1000
    unit_idx += 1

print("Puzzle:")
print(f"Time: {time_taken:.2f}{UNITS[unit_idx]}")
print(f"Result: {puzzle_result}")
