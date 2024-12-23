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
    all_changes = {}
    for i, line in enumerate(lines):
        n = int(line)
        last_price = n % 10
        last_changes = []
        for j in range(2000):
            n = next_secret_number(n)
            price = n % 10
            change = price - last_price
            last_changes.append(change)
            if len(last_changes) > 4:
                last_changes.pop(0)
            if len(last_changes) == 4:
                t = tuple(last_changes)
                if t not in all_changes:
                    all_changes[t] = {i: price}
                elif i not in all_changes[t]:
                    all_changes[t][i] = price
            last_price = price
    return max(sum(d.values()) for d in all_changes.values())


############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample2.txt")) as f:
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
