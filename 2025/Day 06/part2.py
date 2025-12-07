import os
from time import time
from math import prod
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    for i, line in enumerate(lines):
        if line[0] in "+*":
            ops = line.split()
            dists = []
            for j, c in enumerate(line):
                if c != " ":
                    dists.append(j)
    
    all_nums = []
    for line in lines:
        if line[0] in "+*": break

        last_dist = 0
        nums = []
        for dist in dists[1:] + [len(line)+1]:
            nums.append(line[last_dist:dist-1])
            last_dist = dist
        all_nums.append(nums)

    result = 0
    for i, op in enumerate(ops):
        nums_ = [num[i] for num in all_nums]
        nums = []
        for i in range(max(len(n) for n in nums_)):
            s = ""
            for n in nums_:
                if i < len(n):
                    s += n[i]
            nums.append(int(s))
        if op == "+":
            result += sum(nums)
        elif op == "*":
            result += prod(nums)
    return result

############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample.txt")) as f:
    sample = [line.rstrip() for line in f.readlines()]

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.rstrip() for line in f.readlines()]

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
