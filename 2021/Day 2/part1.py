with open('input.txt') as f:
    lines = [line.strip().split(' ') for line in f.readlines()]

depth = 0
dist = 0
for item in lines:
    cmd = item[0]
    amt = int(item[1])

    if cmd == 'forward':
        dist += amt
    elif cmd == 'down':
        depth += amt
    elif cmd == 'up':
        depth -= amt

print(f'Depth: {depth}, dist: {dist}')
print(f'Result: {depth*dist}')