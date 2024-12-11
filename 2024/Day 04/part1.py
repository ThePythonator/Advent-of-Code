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
    vlines = [""] * len(lines[0])
    lr_dlines = [""] * (len(lines) + len(lines[0]) - 1)
    lr_idx = len(lines) - 1
    rl_dlines = [""] * (len(lines) + len(lines[0]) - 1)
    rl_idx = 0
    
    for i, line in enumerate(lines):
        result += count_overlapping(line, "XMAS")
        result += count_overlapping(line, "SAMX")
        for j, c in enumerate(line):
            vlines[j] += c
            lr_dlines[lr_idx + j] += c
            rl_dlines[rl_idx + j] += c
        lr_idx -= 1
        rl_idx += 1

    for lines in [vlines, lr_dlines, rl_dlines]:
        for line in lines:
            result += count_overlapping(line, "XMAS")
            result += count_overlapping(line, "SAMX")

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
