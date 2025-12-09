import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

from math import sqrt, prod

############################################################
# Main solution code here

def solve(lines, connections):
    positions = []
    for i, line in enumerate(lines):
        x,y,z = [int(j) for j in line.split(",")]
        positions.append((x,y,z))

    dists = {i: {} for i in range(len(positions))}
    
    dist_lookup = []
    for i in range(len(positions)):
        for j in range(i+1, len(positions)): # i < j
            x1, y1, z1 = positions[i]
            x2, y2, z2 = positions[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            d = sqrt(dx * dx + dy * dy + dz * dz)
            dists[i][j] = d
            dists[j][i] = d
            dist_lookup.append((d, i, j))

    dist_lookup.sort()

    # Connect <connections> pairs of boxes
    groups = [{i} for i in range(len(positions))]
    for d, i, j in dist_lookup[:connections]:
        # Connect i and j
        # print(groups, i, j)
        for k, g in enumerate(groups):
            # Find i
            if i in g:
                idx_a = k
            if j in g:
                idx_b = k

        if idx_a == idx_b: continue

        # Delete both groups and add a new one
        new_g = groups[idx_a].union(groups[idx_b])
        # print(new_g)
        # print(idx_a, idx_b)
        if idx_a < idx_b:
            del groups[idx_b]
            del groups[idx_a]
        else:
            del groups[idx_a]
            del groups[idx_b]
        # print(new_g)
        groups.append(new_g)

    group_lens = [len(g) for g in groups]
    group_lens.sort(reverse=True)
    # print(group_lens, groups)
    return prod(group_lens[:3])


############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample.txt")) as f:
    sample = [line.strip() for line in f.readlines()]

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

UNITS = ["s", "ms", "μs"]

SAMPLE_START = time()
sample_result = solve(sample, 10)
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
puzzle_result = solve(puzzle, 1000)
time_taken = time() - PUZZLE_START

unit_idx = 0
while time_taken < 1 and unit_idx < len(UNITS) - 1:
    time_taken *= 1000
    unit_idx += 1

print("Puzzle:")
print(f"Time: {time_taken:.2f}{UNITS[unit_idx]}")
print(f"Result: {puzzle_result}")
