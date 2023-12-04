with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

result = 0
for line in lines:
    ints = []
    for c in line:
        if c in "0123456789":
            ints.append(c)
    result += 10 * int(ints[0]) + int(ints[-1])

print(f'Result: {result}')
