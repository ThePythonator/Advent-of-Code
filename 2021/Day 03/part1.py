with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

total = len(lines)
counts = [0] * len(lines[0])

for item in lines:
    for i, char in enumerate(item):
        if char == '1':
            counts[i] += 1

gamma = ''
epsilon = ''

for c in counts:
    if c > total / 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

result = int(gamma, 2) * int(epsilon, 2)

print(f'Final: {gamma}, {epsilon}')
print(f'Result: {result}')
