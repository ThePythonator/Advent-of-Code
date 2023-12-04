with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

t = 0
for i,c in enumerate(lines[0]):
    if c == '(':
        t += 1
    elif c == ')':
        t -= 1

    if t == -1:
        result = i + 1
        break

print(f'Result: {result}')
