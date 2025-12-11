import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

from functools import cache

############################################################
# Main solution code here

def solve(lines):
    graph = {}
    rgraph = {}
    for i, line in enumerate(lines):
        source, rest = line.split(": ")
        sinks = rest.split(" ")
        graph[source] = sinks
        for sink in sinks:
            if sink not in rgraph: rgraph[sink] = []
            rgraph[sink].append(source)

    @cache
    def count_paths(start, end, dac, fft):
        if start == end: return 1 if dac and fft else 0
        total = 0
        for label in rgraph.get(end, []):
            total += count_paths(start, label, dac or label == "dac", fft or label == "fft")
        return total
    
    result = count_paths("svr", "out", False, False)
    return result


############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample_2.txt")) as f:
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
