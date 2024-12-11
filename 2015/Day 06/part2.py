import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    grid = [[0]*1000 for i in range(1000)]
    for line in lines:
        s = line.split(' ')
        start = [int(i) for i in s[-3].split(',')]
        end = [int(i) for i in s[-1].split(',')]
        for x in range(start[0], end[0]+1):
            for y in range(start[1], end[1]+1):
                if s[0] == "toggle":
                    grid[y][x] += 2
                
                elif s[1] == "on":
                    grid[y][x] += 1

                elif s[1] == "off":
                    grid[y][x] = max(grid[y][x] - 1, 0)
    return sum([sum(row) for row in grid])

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
