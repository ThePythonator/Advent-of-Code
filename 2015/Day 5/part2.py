with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


vowels = 'aeiou'

nasty = ['ab','cd','pq','xy']

result = 0
for line in lines:
    v = len([i for i in range(len(line) - 2) if line.count(line[i:i+2]) >= 2])
    r = len([i for i in range(len(line) - 2) if line[i] == line[i + 2]])

    result += 1 if v >= 1 and r >= 1 else 0

print(f'Result: {result}')