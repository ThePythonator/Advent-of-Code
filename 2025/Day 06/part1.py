import os
from time import time
from math import prod
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    all_nums = []
    for i, line in enumerate(lines):
        if line[0] in "+*":
            ops = line.split()
        else:
            all_nums.append([int(i) for i in line.split()])
    
    result = 0
    for i, op in enumerate(ops):
        if op == "+":
            result += sum(num[i] for num in all_nums)
        elif op == "*":
            result += prod(num[i] for num in all_nums)

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
