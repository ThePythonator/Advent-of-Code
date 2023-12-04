import os
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

def get_num(a, b):
    s = 0
    while a < len(lines) and lines[b][a] in "1234567890":
        s = 10 * s + int(lines[b][a])
        a += 1
    return s

starts = []
result = 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c not in "1234567890.":
            # print(c)
            for tx in [-1, 0, 1]:
                for ty in [-1, 0, 1]:
                    dx = tx
                    dy = ty
                    if y + dy >= 0 and y + dy < len(lines):
                        if x + dx >= 0 and x + dx < len(lines[0]):
                            if lines[y + dy][x + dx] in "1234567890":
                                while x + dx >= 1 and lines[y + dy][x + dx - 1] in "1234567890":
                                    dx -= 1
                                if (x + dx, y + dy) not in starts and lines[y + dy][x + dx] in "1234567890":
                                    result += get_num(x + dx, y + dy)
                                    # print(get_num(x + dx, y + dy))
                                    # input()
                                    starts.append((x + dx, y + dy))

print(f'Result: {result}')
