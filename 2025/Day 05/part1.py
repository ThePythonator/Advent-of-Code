import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def in_range(val, ranges):
    i = 0
    if ranges[i][0] > val:
        return False
    
    while ranges[i][0] <= val:
        if ranges[i][1] >= val:
            return True
        i += 1
        if i >= len(ranges):
            return False

    return False

def solve(lines):
    ranges = []
    for i, line in enumerate(lines):
        if line == "":
            break
        ranges.append([int(v) for v in line.split("-")])

    ranges.sort()

    result = 0
    for i, line in enumerate(lines[i+1:]):
        val = int(line)
        if in_range(val, ranges):
            result += 1
    
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
