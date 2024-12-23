import os
from time import time
from itertools import combinations
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    graph = {}
    nodes = set()
    for i, line in enumerate(lines):
        l,r = line.split("-")
        nodes.add(l)
        nodes.add(r)
        if l not in graph: graph[l] = set()
        if r not in graph: graph[r] = set()
        graph[l].add(r)
        graph[r].add(l)
    
    components = []
    for node in nodes:
        connected = {node}
        for n in nodes:
            if all(n in graph[a] for a in connected):
                # n is connected to all items in connected
                connected.add(n)
        components.append(connected)
    return ",".join(sorted(max(components, key=len)))


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
