import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    grid = [["#"]]
    position = [0,0]
    for line in lines:
        direction, distance, colour = line.split()
        distance = int(distance)
        while distance > 0:
            if direction == "R":
                position[0] += 1
            elif direction == "D":
                position[1] += 1
            elif direction == "L":
                position[0] -= 1
            elif direction == "U":
                position[1] -= 1
            if position[0] < 0:
                position[0] += 1
                for i in range(len(grid)):
                    grid[i].insert(0, ".")
            elif position[0] >= len(grid[0]):
                for i in range(len(grid)):
                    grid[i].append(".")
            if position[1] < 0:
                position[1] += 1
                grid.insert(0, ["."]*len(grid[0]))
            elif position[1] >= len(grid):
                grid.append(["."]*len(grid[0]))
            grid[position[1]][position[0]] = "#"
            distance -= 1
    
    result = 0
    for y, l in enumerate(grid):
        in_trench = False
        last_c = "."
        last_in_trench = False
        entry_corner = exit_corner = ""
        inside = False
        trench_length = 0
        for x, c in enumerate(l):
            if c == "#":
                if last_c == ".":
                    in_trench = True
                    entry_corner = "U" if y > 0 and grid[y-1][x] == "#" else "D"
            elif c == ".":
                if last_c == "#":
                    in_trench = False
                    exit_corner = "D" if y < len(grid) - 1 and grid[y+1][x-1] == "#" else "U"
            if in_trench:
                trench_length += 1
            if last_in_trench and not in_trench and (trench_length == 1 or entry_corner != exit_corner):
                inside = not inside
                trench_length = 0
            if inside or c == "#":
                result += 1
            last_c = c
            last_in_trench = in_trench

    return result

############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample.txt")) as f:
    sample = [line.strip() for line in f.readlines()]

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    puzzle = [line.strip() for line in f.readlines()]

SAMPLE_START = time()
sample_result = solve(sample)
print("Sample:")
print(f"Time: {time() - SAMPLE_START}")
print(f"Result: {sample_result}")
print()

PUZZLE_START = time()
puzzle_result = solve(puzzle)
print("Puzzle:")
print(f"Time: {time() - PUZZLE_START}")
print(f"Result: {puzzle_result}")
