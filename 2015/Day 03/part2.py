with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

s = [0,0]
r = [0,0]

visited = set()

i = 0
for c in lines[0]:
    p = s if i % 2 == 0 else r
    i += 1

    visited.add(str(p))

    if c == '>': p[0] += 1
    if c == '<': p[0] -= 1
    if c == 'v': p[1] += 1
    if c == '^': p[1] -= 1

result = len(visited)

print(f'Result: {result}')
