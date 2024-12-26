import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    values = {}
    for i, line in enumerate(lines):
        if line == "": break
        var, val = line.split(": ")
        values[var] = int(val)
    ops = []
    for line in lines[i+1:]:
        l, op, r, _, res = line.split(" ")
        ops.append((l, op, r, res))
    while len(ops) > 0:
        for i in range(len(ops)-1, -1, -1):
            l, op, r, res = ops[i]
            if l in values and r in values:
                if op == "AND":
                    values[res] = values[l] and values[r]
                elif op == "OR":
                    values[res] = values[l] or values[r]
                elif op == "XOR":
                    values[res] = values[l] != values[r]
                del ops[i]
    i = 0
    k = f"z{i:02}"
    result = 0
    power = 1
    while k in values:
        if values[k]: result += power
        power *= 2
        i += 1
        k = f"z{i:02}"
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
