import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def move(robot, boxes, walls, direction):
    px, py = robot[0] + direction[0], robot[1] + direction[1]
    tx, ty = px, py
    while walls[ty][tx] != "#" and boxes[ty][tx]:
        tx += direction[0]
        ty += direction[1]
    if walls[ty][tx] == "#":
        return
    robot[0], robot[1] = px, py
    if boxes[py][px]:
        boxes[py][px] = False
        boxes[ty][tx] = True

def solve(lines):
    result = 0
    robot_pos = None
    boxes = []
    walls = []
    for i, line in enumerate(lines):
        if line == "": break
        boxes.append([])
        for j, c in enumerate(line):
            if c == "@":
                robot_pos = [j, i]
            boxes[-1].append(c == "O")

        result += i
        walls.append(line.replace("O", ".").replace("@", "."))
    
    for line in lines[i+1:]:
        for d in line:
            direction = None
            if d == "^": direction = ( 0, -1)
            if d == ">": direction = ( 1,  0)
            if d == "v": direction = ( 0,  1)
            if d == "<": direction = (-1,  0)
            if direction: move(robot_pos, boxes, walls, direction)
            # print(d)
            # for y, line in enumerate(walls):
            #     for x, c in enumerate(line):
            #         if boxes[y][x]:
            #             print("O", end="")
            #         elif robot_pos[0] == x and robot_pos[1] == y:
            #             print("@", end="")
            #         else:
            #             print(c, end="")
            #     print()
            # input()
            
    result = 0
    for y, line in enumerate(boxes):
        for x, b in enumerate(line):
            if b: result += 100 * y + x
    
    return result


############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample_small.txt")) as f:
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
