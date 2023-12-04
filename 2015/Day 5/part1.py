with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


vowels = 'aeiou'

nasty = ['ab','cd','pq','xy']

result = 0
for line in lines:
    v = len([c for c in line if c in vowels])
    n = len([p for p in nasty if p in line])
    r = len([i for i in range(len(line) - 1) if line[i] == line[i + 1]])

    result += 1 if v >= 3 and n == 0 and r >= 1 else 0

print(f'Result: {result}')