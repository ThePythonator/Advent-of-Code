with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

wires = {}

while len(lines) > 0:

    lines_to_remove = []

    for line in lines:
        a,b = line.split(' -> ')

        a = a.split(' ')

        if len(a) == 1:
            try:
                wires[b] = int(a[0])

            except ValueError:
                if a[0] not in wires.keys():
                    continue

                wires[b] = wires[a[0]]

        elif a[0] == 'NOT':
            if a[1] not in wires.keys():
                continue
            
            wires[b] = 2**16 - 1 - wires[a[1]]

        else:
            try:
                lhs = int(a[0])

            except ValueError:
                if a[0] not in wires.keys():
                    continue

                lhs = wires[a[0]]

            try:
                rhs = int(a[2])

            except ValueError:
                if a[2] not in wires.keys():
                    continue

                rhs = wires[a[2]]

            if a[1] == 'AND':
                wires[b] = lhs & rhs

            elif a[1] == 'OR':
                wires[b] = lhs | rhs

            elif a[1] == 'LSHIFT':
                wires[b] = lhs * (2 ** rhs)

            elif a[1] == 'RSHIFT':
                wires[b] = lhs // (2 ** rhs)

        
        lines_to_remove.append(line)

    for line in lines_to_remove:
        lines.remove(line)

result = wires['a']

print(f'Result: {result}')