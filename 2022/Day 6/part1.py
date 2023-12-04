with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

b = ""
for i, c in enumerate(lines[0]):
    b += c

    if len(b) > 4:
        b = b[1:]

    if len(set(b)) == 4:
        result = i + 1
        break

print(f'Result: {result}')
