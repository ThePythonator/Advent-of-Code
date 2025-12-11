import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def bfs(targets, schematics):
    visited = set()
    q = [(0, tuple(False for _ in range(len(targets))))]
    while len(q) > 0:
        dist, state = q.pop(0)
        if state == targets:
            return dist
        if state in visited:
            continue
        visited.add(state)
        # Find adj nodes
        for schematic in schematics:
            new_state = tuple(s if i not in schematic else not s for i, s in enumerate(state))
            if new_state not in visited:
                q.append((dist + 1, new_state))

def solve(lines):
    result = 0
    for i, line in enumerate(lines):
        items = line.split(" ")
        target_indicators = tuple(v == "#" for v in items[0][1:-1])
        schematics = tuple(set(int(v) for v in s[1:-1].split(",")) for s in items[1:-1])

        # BFS
        result += bfs(target_indicators, schematics)

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
