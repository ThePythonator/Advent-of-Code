import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def plots_reachable(lines, steps, x, y):
    totals = [0,0]
    visited = [set(), set()]
    q = [(steps, x, y)]
    while len(q) > 0:
        steps, x, y = q.pop(0)
        parity = (steps + 1) % 2
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx, ny = x + dx, y + dy
            mx = nx % len(lines[0])
            my = ny % len(lines)
            if lines[my][mx] != "#" and (nx,ny) not in visited[parity]:
                visited[parity].add((nx,ny))
                totals[parity] += 1
                if steps > 1:
                    q.append((steps - 1, nx, ny))
    return totals

def solve(lines, steps):
    pos = (0, 0)
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "S":
                pos = (j, i)
    
    result = plots_reachable(lines, steps, pos[0], pos[1])[0]

    return result


############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample.txt")) as f:
    sample = [line.strip() for line in f.readlines()]

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

SAMPLE_START = time()
sample_result = solve(sample, 6)
print("Sample:")
print(f"Time: {time() - SAMPLE_START}")
print(f"Result: {sample_result}")
print()

PUZZLE_START = time()
puzzle_result = solve(puzzle, 64)
print("Puzzle:")
print(f"Time: {time() - PUZZLE_START}")
print(f"Result: {puzzle_result}")
