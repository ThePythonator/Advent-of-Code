with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

parsed = {}

def solve(target):
    global parsed
    t = parsed[target]
    if len(t) == 1:
        return t[0]
    else:
        lhs = solve(t[0])
        rhs = solve(t[2])
        
        if t[1] == '+':
            return lhs + rhs
        elif t[1] == '-':
            return lhs - rhs
        elif t[1] == '*':
            return lhs * rhs
        elif t[1] == '/':
            return lhs // rhs

for line in lines:
    l = line.replace(':','').split(' ')
    if len(l) == 2:
        l[1] = int(l[1])
    parsed[l[0]] = l[1:]

result = solve('root')

print(f'Result: {result}')
