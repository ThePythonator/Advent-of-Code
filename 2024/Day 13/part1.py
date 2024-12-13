import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

EPSILON = 0.000001

def solve(lines):
    result = 0
    button_a = None
    button_b = None
    for i, line in enumerate(lines):
        if line == "": continue
        label, rest = line.split(": ")
        if label == "Button A":
            button_a = [int(s.split("+")[1]) for s in rest.split(", ")]
        elif label == "Button B":
            button_b = [int(s.split("+")[1]) for s in rest.split(", ")]
        elif label == "Prize":
            x, y = [int(s.split("=")[1]) for s in rest.split(", ")]
            b_count = (button_a[1] * x - button_a[0] * y) / (button_a[1] * button_b[0] - button_a[0] * button_b[1])
            a_count = (x - b_count * button_b[0]) / button_a[0]
            if abs(a_count - round(a_count)) < EPSILON and abs(b_count - round(b_count)) < EPSILON:
                a_count = round(a_count)
                b_count = round(b_count)
                if a_count <= 100 and b_count <= 100:
                    result += a_count * 3 + b_count
    
    return result


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
