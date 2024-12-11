import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    wires = {'b': 956}
    lines.remove('14146 -> b')

    while len(lines) > 0:
        lines_to_remove = []

        for line in lines:
            a,b = line.split(' -> ')
            a = a.split(' ')

            if len(a) == 1:
                try:
                    wires[b] = int(a[0])
                except ValueError:
                    if a[0] not in wires.keys():
                        continue
                    wires[b] = wires[a[0]]

            elif a[0] == 'NOT':
                if a[1] not in wires.keys():
                    continue
                wires[b] = 2**16 - 1 - wires[a[1]]

            else:
                try:
                    lhs = int(a[0])
                except ValueError:
                    if a[0] not in wires.keys():
                        continue
                    lhs = wires[a[0]]

                try:
                    rhs = int(a[2])
                except ValueError:
                    if a[2] not in wires.keys():
                        continue
                    rhs = wires[a[2]]

                if a[1] == 'AND':
                    wires[b] = lhs & rhs
                elif a[1] == 'OR':
                    wires[b] = lhs | rhs
                elif a[1] == 'LSHIFT':
                    wires[b] = lhs * (2 ** rhs)
                elif a[1] == 'RSHIFT':
                    wires[b] = lhs // (2 ** rhs)
            
            lines_to_remove.append(line)

        for line in lines_to_remove:
            lines.remove(line)

    return wires['a']

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
