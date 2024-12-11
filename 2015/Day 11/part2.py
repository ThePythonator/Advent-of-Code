import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

INPUT = 'vzbxxyzz'

a = 'abcdefghijklmnopqrstuvwxyz'

def inc_pass(p):
    s = ''
    carry = True
    for j in range(len(p)):
        c = p[-1-j]
        if carry:
            i = a.index(c) + 1

            if i > 25:
                i = 0
                carry = True
            
            else:
                carry = False
            
            c = a[i]
        
        s = c + s

    return s

def solve(s):
    running = True
    while running:
        s = inc_pass(s)

        if 'i' in s or 'o' in s or 'l' in s:
            continue

        triple = False
        for i in range(len(s) - 2):
            if a.index(s[i]) + 2 == a.index(s[i+1]) + 1 == a.index(s[i+2]):
                triple = True

        if not triple:
            continue
        
        doubles = 0

        i = 0
        while i < len(s) - 1:
            if s[i] == s[i+1]:
                doubles += 1
                i += 1
            i += 1
        
        if doubles < 2:
            continue

        return s

############################################################
# Boilerplate

UNITS = ["s", "ms", "μs"]

PUZZLE_START = time()
puzzle_result = solve(INPUT)
time_taken = time() - PUZZLE_START

unit_idx = 0
while time_taken < 1 and unit_idx < len(UNITS) - 1:
    time_taken *= 1000
    unit_idx += 1

print("Puzzle:")
print(f"Time: {time_taken:.2f}{UNITS[unit_idx]}")
print(f"Result: {puzzle_result}")
