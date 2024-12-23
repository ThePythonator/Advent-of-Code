import os
from time import time
from itertools import permutations, product
from functools import cache
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

TOTAL = 25

def keypad_is_valid(move, lx, ly, x, y):
    if lx == 0 and ly == 1 and y == 0:
        return move != "^" + ">" * x
    elif ly == 0 and x == 0 and y == 1:
        return move != "<" * lx + "v"
    return True

def get_keypad_moves(target, x, y):
    lx,ly = x,y
    if target == "^":
        diff = [1 - x, 0 - y]
    elif target == "A":
        diff = [2 - x, 0 - y]
    elif target == "<":
        diff = [0 - x, 1 - y]
    elif target == "v":
        diff = [1 - x, 1 - y]
    elif target == ">":
        diff = [2 - x, 1 - y]
    moves = []
    while diff[0] < 0:
        moves.append("<")
        x -= 1
        diff[0] += 1
    while diff[0] > 0:
        moves.append(">")
        x += 1
        diff[0] -= 1
    while diff[1] < 0:
        moves.append("^")
        y -= 1
        diff[1] += 1
    while diff[1] > 0:
        moves.append("v")
        y += 1
        diff[1] -= 1
    if len(moves) == 0:
        return None, x, y
    elif len(set(moves)) == 1:
        return ["".join(moves)], x, y
    else:
        return ["".join(l) for l in set(permutations(moves)) if keypad_is_valid("".join(l), lx, ly, x, y)], x, y

def find_arrows(target_str):
    commands = []
    x,y = [2, 0]
    for target in target_str:
        m, x, y = get_keypad_moves(target, x, y)
        if m is not None:
            commands.append([m, ["A"]])
        else:
            commands.append([["A"]])
    return commands

def numpad_is_valid(move, lx, ly, x, y):
    if lx == 0 and ly < 3 and y == 3:
        dx, dy = x - lx, y - ly
        return move != "v" * dy + ">" * dx
    elif ly == 3 and x == 0 and y < 3:
        dx, dy = lx - x, ly - y
        return move != "<" * dx + "^" * dy
    return True

@cache
def get_numpad_moves(target, x, y):
    lx, ly = x, y
    if target == "7":
        diff = [0 - x, 0 - y]
    elif target == "8":
        diff = [1 - x, 0 - y]
    elif target == "9":
        diff = [2 - x, 0 - y]
    elif target == "4":
        diff = [0 - x, 1 - y]
    elif target == "5":
        diff = [1 - x, 1 - y]
    elif target == "6":
        diff = [2 - x, 1 - y]
    elif target == "1":
        diff = [0 - x, 2 - y]
    elif target == "2":
        diff = [1 - x, 2 - y]
    elif target == "3":
        diff = [2 - x, 2 - y]
    elif target == "0":
        diff = [1 - x, 3 - y]
    elif target == "A":
        diff = [2 - x, 3 - y]
    moves = []
    while diff[0] < 0:
        moves.append("<")
        x -= 1
        diff[0] += 1
    while diff[0] > 0:
        moves.append(">")
        x += 1
        diff[0] -= 1
    while diff[1] < 0:
        moves.append("^")
        y -= 1
        diff[1] += 1
    while diff[1] > 0:
        moves.append("v")
        y += 1
        diff[1] -= 1
    if len(moves) == 0:
        return None, x, y
    elif len(set(moves)) == 1:
        return ["".join(moves)], x, y
    else:
        return ["".join(l) for l in set(permutations(moves)) if numpad_is_valid("".join(l), lx, ly, x, y)], x, y

def find_numbers(target_str):
    commands = []
    x,y = [2, 3]
    for target in target_str:
        m, x, y = get_numpad_moves(target, x, y)
        if m is not None:
            commands.append([m, ["A"]])
        else:
            commands.append([["A"]])
    return commands

@cache
def _solve_keypad(i, keys_opts):
    if i == 0: return len(keys_opts[0])
    res = None
    for opt in keys_opts:
        commands = find_arrows(opt)
        next_opts = [tuple("".join(p) for p in product(*digit)) for digit in commands]
        val = sum(_solve_keypad(i - 1, k_opts) for k_opts in next_opts)
        if res:
            res = min(res, val)
        else:
            res = val
    return res

@cache
def _solve(code):
    # Find commmands for first keypad
    commands = find_numbers(code)
    next_opts = [tuple("".join(p) for p in product(*digit)) for digit in commands]
    # Each of "digit" is guaranteed to end in A so can be treated independently (cursor is reset)
    return sum(_solve_keypad(TOTAL, digit) for digit in next_opts)

def solve(lines):
    result = 0
    for i, line in enumerate(lines):
        result += int(line[:-1]) * _solve(line)
    return result

# 11716272 too low (seemed to predict 3996 for all???)

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
