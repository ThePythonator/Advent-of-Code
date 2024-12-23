import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def get_boxes_affected(bx, by, boxes, walls, direction):
    # Get all boxes which would be affected by box (bx, by) moving one step in direction
    # This includes the box (bx, by)
    if boxes[by][bx] == 2:
        bx -= 1 # Shift it so (bx, by) refers to left corner
    to_check = [(bx + direction[0], by + direction[1])]
    if direction[0] == 0: to_check.append((bx + direction[0] + 1, by + direction[1]))
    boxes_affected = set()
    # print(to_check, bx, by, direction)
    for x, y in to_check:
        # print(x, y)
        if direction[0] > 0: x += 1 # Hacky
        # print(x, y)
        # input()
        if walls[y][x] == "#":
            # If the box is unpushable then an empty set is returned
            return set()
        elif boxes[y][x] > 0:
            # A box in the way
            affected = get_boxes_affected(x, y, boxes, walls, direction)
            # If a box is in the way but cannot be affected by the push then it is
            # immovable, so this box can't be moved either
            if len(affected) == 0: return set()
            boxes_affected.add((bx, by))
            boxes_affected = boxes_affected.union(affected)
        else:
            # Nothing is in the way
            boxes_affected.add((bx, by))
    return boxes_affected


def move(robot, boxes, walls, direction):
    px, py = robot[0] + direction[0], robot[1] + direction[1]
    
    if walls[py][px] == "#": return
    
    if boxes[py][px] > 0:
        boxes_affected = get_boxes_affected(px, py, boxes, walls, direction)
        if len(boxes_affected) == 0: return
        # Remove all the boxes which are affected
        for bx, by in boxes_affected:
            assert boxes[by][bx] == 1
            assert boxes[by][bx + 1] == 2
            boxes[by][bx] = 0
            boxes[by][bx + 1] = 0
        # Add the new locations back
        for bx, by in boxes_affected:
            nx, ny = bx + direction[0], by + direction[1]
            assert boxes[ny][nx] == 0
            assert boxes[ny][nx + 1] == 0
            boxes[ny][nx] = 1
            boxes[ny][nx + 1] = 2
    
    # Move the robot
    robot[0], robot[1] = px, py

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
                robot_pos = [j * 2, i]
            boxes[-1].append(1 if c == "O" else 0) # 1 indicates lhs
            boxes[-1].append(2 if c == "O" else 0) # 2 indicates rhs

        result += i
        walls.append("".join(c + c for c in line.replace("O", ".").replace("@", ".")))
    
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
            #         if robot_pos[0] == x and robot_pos[1] == y:
            #             print("@", end="")
            #         elif boxes[y][x]:
            #             print("[" if boxes[y][x] == 1 else "]", end="")
            #         else:
            #             print(c, end="")
            #     print()
            # input()
            
    result = 0
    for y, line in enumerate(boxes):
        for x, b in enumerate(line):
            if b == 1: result += 100 * y + x
    
    return result


############################################################
# Boilerplate

with open(os.path.join(SCRIPT_PATH, "sample_big.txt")) as f:
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
