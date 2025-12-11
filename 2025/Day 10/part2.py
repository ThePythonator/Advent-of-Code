import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

############################################################
# Main solution code here

def bfs(targets, schematics):
    visited = set()
    q = [(0, tuple(0 for _ in range(len(targets))))]
    while len(q) > 0:
        dist, state = q.pop(0)
        if state == targets:
            return dist
        if state in visited:
            continue
        visited.add(state)
        # Find adj nodes
        for schematic in schematics:
            new_state = tuple(s if i not in schematic else s + 1 for i, s in enumerate(state))
            skip = False
            for i in range(len(new_state)):
                if targets[i] < new_state[i]:
                    skip = True
                    break
            if not skip and new_state not in visited:
                q.append((dist + 1, new_state))

def lp(targets, schematics):
    A = np.array([[1 if t in s else 0 for s in schematics] for t in range(len(targets))])
    b = np.array(targets)

    # Objective (minimise sum)
    c = np.ones(A.shape[1])

    # Lower bound = upper bound
    linear_constraints = LinearConstraint(A, b, b)

    int_bounds = Bounds(np.full(A.shape[1], 0), np.full(A.shape[1], np.inf))
    integrality = np.ones(A.shape[1])

    result = milp(c=c, constraints=linear_constraints, bounds=int_bounds, integrality=integrality)

    if result.success:
        return round(result.fun)
    
    raise RuntimeError

def solve(lines):
    result = 0
    for i, line in enumerate(lines):
        items = line.split(" ")
        schematics = tuple(set(int(v) for v in s[1:-1].split(",")) for s in items[1:-1])
        # joltages = tuple(int(v) for v in items[-1][1:-1].split(","))


        joltages = list(int(v) for v in items[-1][1:-1].split(","))

        # BFS
        # result += bfs(joltages, schematics)
        result += lp(joltages, schematics)

        # print(f"Progress: {i+1}/{len(lines)}")

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
