import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    rules = True
    rule_dict = {}
    result = 0
    for i, line in enumerate(lines):
        if line == "":
            rules = False
            continue
    
        if rules:
            l, r = [int(j) for j in line.split("|")]
            if r not in rule_dict:
                rule_dict[r] = set()
            rule_dict[r].add(l)
        else:
            pages = [int(j) for j in line.split(",")]
            all_pages = set(pages)
            previous = set()
            valid = True
            req_lookup = []
            for page in pages:
                reqs = rule_dict.get(page, set()).intersection(all_pages)
                req_lookup.append((page, reqs))
                missing = reqs - previous
                if len(missing) > 0:
                    # This update is invalid
                    valid = False
                previous.add(page)
            
            if not valid:
                req_lookup.sort(key = lambda t: len(t[1]))
                previous = set()
                new_pages = []
                for page, reqs in req_lookup:
                    missing = reqs - previous
                    assert len(missing) == 0
                    previous.add(page)
                    new_pages.append(page)
                result += new_pages[len(new_pages) // 2]
    
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
