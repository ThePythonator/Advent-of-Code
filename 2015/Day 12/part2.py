import json
import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def traverse(j):
    if type(j) == dict and "red" in j.values():
        return 0

    if type(j) == str:
        return 0

    if type(j) == int:
        return j
    
    if type(j) == list:
        return sum([traverse(i) for i in j])

    if type(j) == dict:
        return sum([traverse(i) for i in j.values()])

    print(j)
    input("oops")

def solve(lines):
    return traverse(json.loads(lines[0]))

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