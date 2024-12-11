import os
import re
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def count_overlapping(text, target):
    return sum(1 for _ in re.finditer(f"(?={target})", text))

def solve(lines):
    result = 0
    for i in range(len(lines) - 2):
        for j in range(len(lines[0]) - 2):
            diag_one = lines[i+1][j+1] == "A" and ((lines[i][j] == "S" and lines[i+2][j+2] == "M") or (lines[i][j] == "M" and lines[i+2][j+2] == "S"))
            diag_two = lines[i+1][j+1] == "A" and ((lines[i+2][j] == "S" and lines[i][j+2] == "M") or (lines[i+2][j] == "M" and lines[i][j+2] == "S"))
            if diag_one and diag_two:
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
