import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

import math

def solve(lines):
    # Parse workflows
    workflows = {}
    for line in lines:
        if line == "":
            break
        name, workflow = line.replace("}", "").split("{")
        parsed_workflow = []
        for w in workflow.split(","):
            if ":" in w:
                cond, jmp = w.split(":")
                attr = cond[0]
                cmp = cond[1]
                val = int(cond[2:])
            else:
                jmp = w
                attr = cmp = val = None
            parsed_workflow.append((attr, cmp, val, jmp))
        workflows[name] = parsed_workflow

    items = [
        (
            "in", {
                "x":(1,4000),
                "m":(1,4000),
                "a":(1,4000),
                "s":(1,4000)
            }
        )
    ]

    result = 0
    while len(items) > 0:
        workflow, attrs = items.pop()

        if workflow == "A":
            result += math.prod([ma - mi + 1 for mi, ma in attrs.values()])
            continue
        elif workflow == "R":
            continue

        # Simulate item
        for attr, cmp, val, jmp in workflows[workflow]:
            if cmp is None:
                items.append((jmp, attrs))
                break
            mi, ma = attrs[attr]
            if cmp == "<":
                if mi < val:
                    if ma < val:
                        items.append((jmp, attrs))
                    else:
                        new_attrs = attrs.copy()
                        new_attrs[attr] = (mi, val - 1)
                        attrs[attr] = (val, ma)
                        items.append((jmp, new_attrs))
            elif cmp == ">":
                if ma > val:
                    if mi > val:
                        items.append((jmp, attrs))
                    else:
                        new_attrs = attrs.copy()
                        new_attrs[attr] = (val + 1, ma)
                        attrs[attr] = (mi, val)
                        items.append((jmp, new_attrs))

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
