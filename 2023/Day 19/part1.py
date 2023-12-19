import os
from time import time
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

############################################################
# Main solution code here

def solve(lines):
    result = 0
    # Parse workflows
    workflows = {}
    parsing_workflows = True
    for line in lines:
        if line == "":
            parsing_workflows = False
            continue
        if parsing_workflows:
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
        else:
            # Parsing items
            attrs = line.replace("{", "").replace("}", "").split(",")
            parsed_attrs = {}
            for attr in attrs:
                a, v = attr.split("=")
                parsed_attrs[a] = int(v)
            
            # Simulate item
            current_workflow = "in"
            while current_workflow not in ["A", "R"]:
                for attr, cmp, val, jmp in workflows[current_workflow]:
                    lhs = parsed_attrs.get(attr, None)
                    if (cmp == "<" and lhs < val) or (cmp == ">" and lhs > val) or cmp is None:
                        current_workflow = jmp
                        break

            if current_workflow == "A":
                result += sum(parsed_attrs.values())

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
