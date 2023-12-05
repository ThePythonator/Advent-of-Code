with open('input.txt') as f:
    lines = [line.strip('\n') for line in f.readlines()]

stack_lines = []

for n, line in enumerate(lines):
    if line == "":
        break
    else:
        stack_lines.append(line)

lines = lines[n+1:]

stacks = [[] for i in range(len(stack_lines[-1].split('   ')))]

stack_lines = stack_lines[:-1]

for line in reversed(stack_lines):
    print(line)
    for i in range(1, len(line), 4):
        if line[i] != ' ':
            stacks[i//4].append(line[i])

for line in lines:
    l = line.split(' ')
    a,b,c = int(l[1]), int(l[3]), int(l[5])
    for i in range(a):
        t = stacks[b-1].pop()
        stacks[c-1].append(t)

result = ''
for s in stacks:
    result += s[-1]

print(f'Result: {result}')
