import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def try_reps(s, e, reps):
    result = set()

    if len(s) % reps != 0:
        c = 10 ** (len(s) // reps)
    else:
        c = int(s[:len(s)//reps])

    if reps > len(e):
        return None

    s = int(s)
    e = int(e)

    code = int(str(c) * reps)

    while code <= e:
        c += 1
        if code >= s:
            result.add(code)
        code = int(str(c) * reps)

    return result

def solve(lines):
    result = set()
    for i, line in enumerate(lines):
        ranges = line.split(",")
        for range in ranges:
            s, e = range.split("-")
            
            reps = 2
            while True:
                r = try_reps(s, e, reps)
                if r is None:
                    break
                result.update(r)
                # if len(r):
                #     print(s, e, reps, r)
                #     print(result)
                reps += 1
    
    return sum(result)


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
