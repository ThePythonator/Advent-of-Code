import os
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]

result = 0
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "O":
            z = i
            while z > 0 and lines[z - 1][j] == ".":
                lines[z - 1] = lines[z - 1][:j] + "O" + lines[z - 1][j + 1:]
                lines[z] = lines[z][:j] + "." + lines[z][j + 1:]
                z -= 1
            result += len(lines) - z

for line in lines: print(line)

print(f"Result: {result}")
