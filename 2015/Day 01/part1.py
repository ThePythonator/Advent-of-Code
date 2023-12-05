with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

result = 0
for c in lines[0]:
    if c == '(':
        result += 1
    elif c == ')':
        result -= 1

print(f'Result: {result}')
