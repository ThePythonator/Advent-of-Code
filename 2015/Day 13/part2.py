import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def cost(lookup_table, a, b):
    if a == "You" or b == "You": return 0
    return lookup_table[a][b] + lookup_table[b][a]

def _solve(lookup_table, existing_assignment, total_people):
    if len(existing_assignment) == total_people:
        return cost(lookup_table, existing_assignment[-1], existing_assignment[0])

    return max([cost(lookup_table, existing_assignment[-1], b) + _solve(lookup_table, existing_assignment.copy() + [b], total_people) for b in lookup_table.keys() if b not in existing_assignment])

def solve(lines):
    lookup_table = {}
    for line in lines:
        line = line.split(" ")
        a = line[0]
        b = line[10][:-1]
        c = int(line[3])
        if line[2] == "lose": c = -c
        if a not in lookup_table.keys():
            lookup_table[a] = {}
        lookup_table[a][b] = c
    TOTAL_PEOPLE = len(lookup_table.keys()) + 1
    return _solve(lookup_table, ["You"], TOTAL_PEOPLE)

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
