import os

INPUT_FILE = os.path.join(os.path.dirname(__file__), "input.txt")

lookup_table = {}

with open(INPUT_FILE) as f:
    for line in f.readlines():
        line = line.strip().split(" ")
        a = line[0]
        b = line[10][:-1]
        c = int(line[3])
        if line[2] == "lose": c = -c
        if a not in lookup_table.keys():
            lookup_table[a] = {}
        lookup_table[a][b] = c

TOTAL_PEOPLE = len(lookup_table.keys())

def cost(a, b):
    return lookup_table[a][b] + lookup_table[b][a]

def solve(existing_assignment):
    if len(existing_assignment) == TOTAL_PEOPLE:
        return cost(existing_assignment[-1], existing_assignment[0])

    return max([cost(existing_assignment[-1], b) + solve(existing_assignment.copy() + [b]) for b in lookup_table.keys() if b not in existing_assignment])


result = solve([list(lookup_table.keys())[0]])

print(f'Result: {result}')