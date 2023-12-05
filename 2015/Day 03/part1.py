with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

p = [0,0]

visited = set()

for c in lines[0]:
    visited.add(str(p))

    if c == '>': p[0] += 1
    if c == '<': p[0] -= 1
    if c == 'v': p[1] += 1
    if c == '^': p[1] -= 1

result = len(visited)

print(f'Result: {result}')
