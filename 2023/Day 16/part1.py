import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def move_in_dir(pos, d, w, h):
    if d == 0 and pos[0] < w - 1:
        return (pos[0] + 1, pos[1], d)
    elif d == 1 and pos[1] < h - 1:
        return (pos[0], pos[1] + 1, d)
    elif d == 2 and pos[0] > 0:
        return (pos[0] - 1, pos[1], d)
    elif d == 3 and pos[1] > 0:
        return (pos[0], pos[1] - 1, d)
    else:
        return None

def append_if_not_null(l, a):
    if a is not None:
        l.append(a)

def solve(lines):
    visited = set()
    w = len(lines[0])
    h = len(lines)

    # (x, y, dir)
    # dir is 0 for E, 1 for S, 2 for W, 3 for N
    beams = [(0, 0, 0)]
    # beams = [(1, 0, 0)]
    # visited.add((0, 0, 0))
    while len(beams) > 0:
        beam = beams.pop()

        if beam in visited:
            continue

        d = beam[2]
        visited.add(beam)

        c = lines[beam[1]][beam[0]]

        if c == ".":
            append_if_not_null(beams, move_in_dir(beam[:2], d, w, h))
        elif c == "/":
            new_d = 3 - d
            append_if_not_null(beams, move_in_dir(beam[:2], new_d, w, h))
        elif c == "\\":
            if d < 2:
                new_d = 1 - d
            else:
                new_d = 5 - d
            append_if_not_null(beams, move_in_dir(beam[:2], new_d, w, h))
        elif c == "-":
            if d % 2 == 0:
                append_if_not_null(beams, move_in_dir(beam[:2], d, w, h))
            else:
                append_if_not_null(beams, move_in_dir(beam[:2], 0, w, h))
                append_if_not_null(beams, move_in_dir(beam[:2], 2, w, h))
        elif c == "|":
            if d % 2 == 1:
                append_if_not_null(beams, move_in_dir(beam[:2], d, w, h))
            else:
                append_if_not_null(beams, move_in_dir(beam[:2], 1, w, h))
                append_if_not_null(beams, move_in_dir(beam[:2], 3, w, h))
    
    unique = set(v[:2] for v in visited)

    return len(unique)

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
