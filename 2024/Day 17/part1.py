import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    registers = [0, 0, 0]
    program = None
    for i, line in enumerate(lines):
        if i < 3:
            registers[i] = int(line.split(": ")[1])
        elif i == 4:
            program = [int(j) for j in line.replace("Program: ", "").split(",")]
        
    inst_ptr = 0
    output = []
    while inst_ptr < len(program):
        opcode = program[inst_ptr]
        literal = operand = program[inst_ptr + 1]
        combo = operand if operand < 4 else None if operand == 7 else registers[operand - 4]

        inst_ptr += 2

        if opcode == 0:
            numerator = registers[0]
            denominator = 1 << combo
            registers[0] = int(numerator // denominator)
        elif opcode == 1:
            registers[1] ^= literal
        elif opcode == 2:
            registers[1] = combo % 8
        elif opcode == 3:
            if registers[0] != 0:
                inst_ptr = literal
        elif opcode == 4:
            registers[1] ^= registers[2]
        elif opcode == 5:
            output.append(combo % 8)
        elif opcode == 6:
            numerator = registers[0]
            denominator = 1 << combo
            registers[1] = int(numerator // denominator)
        elif opcode == 7:
            numerator = registers[0]
            denominator = 1 << combo
            registers[2] = int(numerator // denominator)
    
    return ",".join(str(i) for i in output)


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
