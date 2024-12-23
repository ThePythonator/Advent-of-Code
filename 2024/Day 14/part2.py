import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def _solve(lines, area, t):
    final_positions = []
    for i, line in enumerate(lines):
        pos, vel = [[int(j) for j in s.replace("p=","").replace("v=","").split(",")] for s in line.split(" ")]
        final_positions.append(((pos[0] + vel[0] * t) % area[0], (pos[1]  + vel[1] * t) % area[1]))

    midx, midy = area[0] // 2, area[1] // 2
    quads = [0]*4
    grid = [[0] * area[0] for i in range(area[1])]
    for pos in set(final_positions):
        grid[pos[1]][pos[0]] += 1
        if pos[0] < midx:
            if pos[1] < midy:
                quads[0] += 1
            elif pos[1] > midy:
                quads[1] += 1
        elif pos[0] > midx:
            if pos[1] < midy:
                quads[2] += 1
            elif pos[1] > midy:
                quads[3] += 1

    if max(quads) > min(quads) * 5:
        # print("\n".join("".join(str(s) if s > 0 else "." for s in g) for g in grid))
        # print(f"Steps required: {t}")
        return True
    return False

def solve(lines, area):
    for i in range(10000):
        if _solve(lines, area, i): return i
    return -1


############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample.txt")) as f:
    sample = [line.strip() for line in f.readlines()]

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

UNITS = ["s", "ms", "μs"]

SAMPLE_START = time()
sample_result = solve(sample, (11, 7))
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
puzzle_result = solve(puzzle, (101, 103))
time_taken = time() - PUZZLE_START

unit_idx = 0
while time_taken < 1 and unit_idx < len(UNITS) - 1:
    time_taken *= 1000
    unit_idx += 1

print("Puzzle:")
print(f"Time: {time_taken:.2f}{UNITS[unit_idx]}")
print(f"Result: {puzzle_result}")
