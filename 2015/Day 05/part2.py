import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    vowels = 'aeiou'
    nasty = ['ab','cd','pq','xy']
    result = 0
    for line in lines:
        v = len([i for i in range(len(line) - 2) if line.count(line[i:i+2]) >= 2])
        r = len([i for i in range(len(line) - 2) if line[i] == line[i + 2]])
        result += 1 if v >= 1 and r >= 1 else 0
    return result

############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

UNITS = ["s", "ms", "μs"]

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
