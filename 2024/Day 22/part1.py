import os
from time import time
from functools import cache
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

@cache
def next_secret_number(n):
    n ^= n << 6
    n %= 16777216
    n ^= n >> 5
    n %= 16777216
    n ^= n << 11
    n %= 16777216
    return n

def solve(lines):
    result = 0
    for i, line in enumerate(lines):
        n = int(line)
        n = 123
        for _ in range(2000):
            n = next_secret_number(n)
        result += n
    return result


############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample1.txt")) as f:
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
