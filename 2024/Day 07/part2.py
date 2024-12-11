import os
from time import time
import heapq
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def can_make(target, values):
    q = []
    heapq.heappush(q, (1, values[0]))
    while len(q) > 0:
        idx, val = heapq.heappop(q)
        if idx == len(values):
            if val == target:
                return True
        else:
            add_val = val + values[idx]
            if add_val <= target:
                heapq.heappush(q, (idx + 1, add_val))

            mul_val = val * values[idx]
            if mul_val <= target:
                heapq.heappush(q, (idx + 1, mul_val))

            concat_val = int(str(val) + str(values[idx]))
            if concat_val <= target:
                heapq.heappush(q, (idx + 1, concat_val))
    return False

def solve(lines):
    result = 0
    for i, line in enumerate(lines):
        target, rest = line.split(": ")
        target = int(target)
        values = [int(j) for j in rest.split()]
        if can_make(target, values):
            result += target
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
