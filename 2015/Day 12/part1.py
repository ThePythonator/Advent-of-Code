with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

l = lines[0]

l = l.replace('{', ',').replace('}', ',').replace('[', ',').replace(']', ',').replace(':', ',')

result = 0
for item in l.split(','):
    if "\"" in item or item == "": continue

    result += int(item)

print(f'Result: {result}')