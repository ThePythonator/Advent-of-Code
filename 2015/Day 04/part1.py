import hashlib
import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

SECRET = 'ckczppom'

def solve(secret):
    result = 1
    found = False
    n = 5
    while not found:
        res = hashlib.md5((secret+str(result)).encode()).hexdigest()
        if res[:n] == '0'*n:
            found = True
        else:
            result += 1
    return result

UNITS = ["s", "ms", "μs"]

PUZZLE_START = time()
puzzle_result = solve(SECRET)
time_taken = time() - PUZZLE_START

unit_idx = 0
while time_taken < 1 and unit_idx < len(UNITS) - 1:
    time_taken *= 1000
    unit_idx += 1

print("Puzzle:")
print(f"Time: {time_taken:.2f}{UNITS[unit_idx]}")
print(f"Result: {puzzle_result}")
