import os
from time import time
from itertools import product
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    locks = []
    keys = []
    i = 0
    while i < len(lines):
        sublist = []
        while i < len(lines):
            val = lines[i]
            i += 1
            if val == "": break
            sublist.append(val)
        l = []
        h = len(sublist)
        for j in range(len(sublist[0])):
            l.append(sum(1 if line[j] == "#" else 0 for line in sublist))
        if sublist[0][0] == ".": # Must be a key
            keys.append((h, l))
        else:
            locks.append((h, l))
    result = 0
    for (h1, l), (h2, k) in product(locks, keys):
        assert h1 == h2
        h = h1
        failed = False
        for a, b in zip(l, k):
            if a + b > h:
                failed = True
        if not failed: result += 1
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
