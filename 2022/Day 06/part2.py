with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

n = 14

b = ""
for i, c in enumerate(lines[0]):
    b += c

    if len(b) > n:
        b = b[1:]

    if len(set(b)) == n:
        result = i + 1
        break

print(f'Result: {result}')
