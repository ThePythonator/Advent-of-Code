import os
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()] + [""]

groups = []
current_group = []
for i, line in enumerate(lines):
    if line == "":
        groups.append(current_group)
        current_group = []
    else:
        current_group.append(line)

def h_reflection(group, column, smudges_left):
    a = column
    b = column + 1
    while a >= 0 and b < len(group[0]):
        for z in range(len(group)):
            if group[z][a] != group[z][b]:
                if smudges_left > 0:
                    smudges_left -= 1
                else:
                    return False
        a -= 1
        b += 1
    return smudges_left == 0

def v_reflection(group, row, smudges_left):
    a = row
    b = row + 1
    while a >= 0 and b < len(group):
        for z in range(len(group[0])):
            if group[a][z] != group[b][z]:
                if smudges_left > 0:
                    smudges_left -= 1
                else:
                    return False
        a -= 1
        b += 1
    return smudges_left == 0

result = 0
for group in groups:
    for i in range(len(group[0])):
        if i < len(group[0]) - 1 and h_reflection(group, i, 1):
            result += i + 1
            break
    for i in range(len(group)):
        if i < len(group) - 1 and v_reflection(group, i, 1):
            result += 100 * (i + 1)
            break

print(f"Result: {result}")
