import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

INPUT = 1321131112

def solve(n):
    n = str(n)

    for i in range(40):
        t = 0
        l = n[0]
        r = ''
        for c in n:
            if c != l:
                r += str(t) + l
                l = c
                t = 0
            t += 1

        r += str(t) + c
        n = r

    return len(n)

############################################################
# Boilerplate

UNITS = ["s", "ms", "μs"]

PUZZLE_START = time()
puzzle_result = solve(INPUT)
time_taken = time() - PUZZLE_START

unit_idx = 0
while time_taken < 1 and unit_idx < len(UNITS) - 1:
    time_taken *= 1000
    unit_idx += 1

print("Puzzle:")
print(f"Time: {time_taken:.2f}{UNITS[unit_idx]}")
print(f"Result: {puzzle_result}")
