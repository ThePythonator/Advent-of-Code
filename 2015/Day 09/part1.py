import itertools
import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    distances = {}

    for line in lines:
        l = line.split(' ')
        s = l[0]
        e = l[2]
        d = int(l[4])

        if s not in distances.keys():
            distances[s] = {}
        
        if e not in distances.keys():
            distances[e] = {}

        distances[s][e] = d
        distances[e][s] = d

    result = 9999999

    p = itertools.permutations(distances.keys())

    for t in p:
        r = 0
        for i in range(len(t) - 1):
            r += distances[t[i]][t[i+1]]

        result = min(r, result)
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
