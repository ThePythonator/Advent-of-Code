import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    s = [0,0]
    r = [0,0]
    visited = set()
    i = 0
    for c in lines[0]:
        p = s if i % 2 == 0 else r
        i += 1
        visited.add(str(p))
        if c == '>': p[0] += 1
        if c == '<': p[0] -= 1
        if c == 'v': p[1] += 1
        if c == '^': p[1] -= 1
    return len(visited)

############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

UNITS = ["s", "ms", "μs"]

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
