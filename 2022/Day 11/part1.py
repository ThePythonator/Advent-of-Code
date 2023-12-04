class Monkey:
    def __init__(self, items, op, test, t, f):
        self._items = items
        self._op = lambda old : eval(op)
        self._test = lambda x : x % test == 0
        self._t = t
        self._f = f

        self._inspections = 0

    def play(self):
        self._inspections += 1
        n = self._op(self._items.pop(0))
        n //= 3
        return self._t if self._test(n) else self._f, n

    def has_items(self):
        return len(self._items) > 0

    def inspections(self):
        return self._inspections

    def add(self, n):
        self._items.append(n)
            

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

monkeys = []

for i in range(0, len(lines), 7):
    items = [int(i) for i in lines[i+1].split(': ')[-1].split(', ')]
    operation = lines[i+2].split(': ')[-1].split(' = ')[-1]
    test = int(lines[i+3].split(' ')[-1])
    if_t = int(lines[i+4].split(' ')[-1])
    if_f = int(lines[i+5].split(' ')[-1])

    monkeys.append(Monkey(items, operation, test, if_t, if_f))
    
rounds = 20
for r in range(rounds):
    for m in monkeys:
        
        while m.has_items():
            i, n = m.play()

            monkeys[i].add(n)

s = sorted([m.inspections() for m in monkeys], reverse=True)
result = s[0] * s[1]

print(f'Result: {result}')
