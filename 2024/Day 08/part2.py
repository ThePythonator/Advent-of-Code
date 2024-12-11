import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def add(a, b):
    return tuple(c + d for c, d in zip(a, b))

def subtract(a, b):
    return tuple(c - d for c, d in zip(a, b))

def solve(lines):
    antinodes = set()
    antenna_positions = {}
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c != ".":
                if c not in antenna_positions:
                    antenna_positions[c] = []
                antenna_positions[c].append((j, i))
    for antenna, positions in antenna_positions.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                # pair i, j
                diff = subtract(positions[i], positions[j])
                a1 = add(positions[i], diff)
                a2 = subtract(positions[j], diff)
                antinodes.add(positions[i])
                antinodes.add(positions[j])
                while a1[0] >= 0 and a1[0] < len(lines[0]) and a1[1] >= 0 and a1[1] < len(lines):
                    antinodes.add(a1)
                    a1 = add(a1, diff)
                while a2[0] >= 0 and a2[0] < len(lines[0]) and a2[1] >= 0 and a2[1] < len(lines):
                    antinodes.add(a2)
                    a2 = subtract(a2, diff)
    return len(antinodes)


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
