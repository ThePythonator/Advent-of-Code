from itertools import permutations

with open('in.txt') as f:
    lines = [int(line.strip()) for line in f.readlines()]

perms = permutations(lines, 3)

for perm in perms:
    if sum(perm) == 2020:
        print(perm,':',perm[0]*perm[1]*perm[2])
