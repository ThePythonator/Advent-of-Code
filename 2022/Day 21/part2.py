with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

parsed = {}

def reverse_solve(start, value, target):
    t = parsed[start]
    if start == 'humn':
        return value
    elif len(t) == 1:
        return t[0]
    else:
        lhs = solve(t[0])
        rhs = solve(t[2])
        # print(start, value, parsed[start])
        # print('l,r',lhs,rhs)
        # input()

        n = t[0] if lhs is None else t[2]
        o = lhs if lhs is not None else rhs
        
        if t[1] == '+':
            return reverse_solve(n, value - o, target)
        elif t[1] == '-':
            if lhs is not None:
                return reverse_solve(n, o - value, target)
            else:
                return reverse_solve(n, o + value, target)
        elif t[1] == '*':
            return reverse_solve(n, value // o, target)
        elif t[1] == '/':
            if lhs is not None:
                return reverse_solve(n, o // value, target)
            else:
                return reverse_solve(n, o * value, target)

def solve(target):
    t = parsed[target]
    if target == 'humn':
        return None
    elif len(t) == 1:
        return t[0]
    elif target == 'root':
        lhs = solve(t[0])
        rhs = solve(t[2])
        
        n = t[0] if lhs is None else t[2]
        value = lhs if lhs is not None else rhs

        return reverse_solve(n, value, 'humn')
    else:
        lhs = solve(t[0])
        rhs = solve(t[2])

        if lhs is None or rhs is None:
            return None
        
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
