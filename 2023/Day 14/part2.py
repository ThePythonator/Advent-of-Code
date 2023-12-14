import os
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

result = 0

def vert(dir): # 1 is south, -1 is north
    start_i = len(lines) - 1 if dir == 1 else 0
    stop_i = len(lines) if dir == -1 else -1
    for i in range(start_i, stop_i, dir * -1):
        for j in range(len(lines[0])):
            if lines[i][j] == "O":
                z = i
                while ((dir < 0 and z > 0) or (dir > 0 and z < len(lines) - 1)) and lines[z + dir][j] == ".":
                    lines[z + dir] = lines[z + dir][:j] + "O" + lines[z + dir][j + 1:]
                    lines[z] = lines[z][:j] + "." + lines[z][j + 1:]
                    z += dir

def horz(dir): # 1 is east, -1 is west
    start_j = len(lines[0]) - 1 if dir == 1 else 0
    stop_j = len(lines[0]) if dir == -1 else -1
    for j in range(start_j, stop_j, dir * -1):
        for i in range(len(lines)):
            if lines[i][j] == "O":
                z = j
                while ((dir < 0 and z > 0) or (dir > 0 and z < len(lines[0]) - 1)) and lines[i][z + dir] == ".":
                    lines[i] = lines[i][:z + dir] + "O" + lines[i][z + dir + 1:]
                    lines[i] = lines[i][:z] + "." + lines[i][z + 1:]
                    z += dir

def cycle():
    vert(-1)
    horz(-1)
    vert(1)
    horz(1)

cache = []

SUBLIST_LEN = 4

window = []

def is_sublist(smaller, bigger):
    for i in range(len(bigger) - len(smaller) + 1):
        if bigger[i:i+len(smaller)] == smaller:
            return i
    return -1

# while lines not in cache:
while is_sublist(window, cache) < 0 or len(window) < SUBLIST_LEN:
    cache.append(lines.copy())
    cycle()
    window.append(lines.copy())
    if len(window) > SUBLIST_LEN:
        del window[0]

a = is_sublist(window, cache)
period = len(cache) - (a + SUBLIST_LEN - 1)

b = (1000000000 - a) % period
b += a

result = 0
for i, line in enumerate(cache[b]):
    result += (len(lines) - i) * line.count("O")

print(f"Result: {result}")
