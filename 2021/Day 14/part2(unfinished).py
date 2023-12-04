def from_rule(rules, pair):
    for rule in rules:
        if rule[0] == pair:
            return rule[1]
    return '?'

def step(poly, rules):
    new_poly = ''
    for i in range(len(poly)-1):
        pair = poly[i:i+2]
        new_poly += poly[i] + from_rule(rules, pair)

    return new_poly + poly[-1]

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

poly = lines[0]

rules = [item.split(' -> ') for item in lines[2:]]

for rule in rules:
    rules.append([rule[0], step(rule, rules)])

print(rules)

##d = {}
##for c in poly:
##    if c not in d:
##        d[c] = 0
##        
##    d[c] += 1
##
##ma = max(d[k] for k in d.keys())
##mi = min(d[k] for k in d.keys())
##
##print(f'Result: {ma-mi}')
