import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    x = y = 0
    vertices = []
    for line in lines:
        direction, distance, colour = line.split()
        direction = colour[-2]
        # distance = int(distance)
        # direction = "0" if direction == "R" else "1" if direction == "D" else "2" if direction == "L" else "3"
        distance = int(colour[2:-2], 16)
        if direction == "0":
            x += distance
        elif direction == "1":
            y += distance
        elif direction == "2":
            x -= distance
        elif direction == "3":
            y -= distance
        vertices.append((x,y))

    ys = sorted(vertices, key=lambda x:(x[1],x[0]))
    rows = []
    while len(ys) > 0:
        # Remove all ys in the same layer
        vs = [ys.pop(0)]
        while len(ys) > 0 and ys[0][1] == vs[0][1]:
            vs.append(ys.pop(0))
        rows.append(vs)

    result = 0
    lines = [] # x coords of existing lines
    prev_y = 0
    for i in range(len(rows)):
        row = rows[i]
        lines.sort()
        y = row[0][1]

        for j in range(0, len(lines), 2):
            # Get extruded shape width and height
            result += (lines[j+1] - lines[j] + 1) * (y - prev_y - 1)

        directions = {x: "L" for x in lines}
        for x, y in row:
            terminated = False
            for p_x in lines[::-1]:
                if x == p_x:
                    # The line terminates here
                    lines.remove(p_x)
                    terminated = True
                    directions[p_x] = "U"
                    break

            if not terminated:
                # The line starts here
                lines.append(x)
                directions[x] = "D"

        # Get width of current row
        inside = 0
        last_x = 0
        last_d = ""
        w = 0
        for x, d in sorted(directions.items()):
            if inside == 1:
                if d == "L":
                    inside = 0
                    w += x - last_x + 1
                else:
                    inside = 1.5

            elif inside == 0.5:
                assert d != "L"
                if d != last_d:
                    inside = 1
                else:
                    inside = 0
                    w += x - last_x + 1

            elif inside == 1.5:
                assert d != "L"
                if d != last_d:
                    inside = 0
                    w += x - last_x + 1
                else:
                    inside = 1

            else:
                inside = 1 if d == "L" else 0.5
                last_x = x

            last_d = d

        result += w

        prev_y = y
        

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
