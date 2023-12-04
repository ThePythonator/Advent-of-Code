from itertools import permutations

def perm_sum(last25):
    out = []
    for perm in permutations(last25, 2):
        if sum(perm) not in out:
            out.append(sum(perm))

    return out

def all_contiguous_perms(l,m=None):
    for i in range(len(l)):
        for j in range(2, (len(l) if m is None else m)-i):
            yield l[i:i+j]
        

with open('in.txt') as f:
    lines = [int(line.strip()) for line in f.readlines()]

last25 = []
total = lines.copy()

for i in range(25):
    last25.append(lines.pop(0))

for i in range(len(lines)):
    num = lines.pop(0)
    if num in perm_sum(last25):
        last25.append(num)
        last25.pop(0)
    else:
        result = num
##        print(num)
        break

searchable = total[:i+26]

for perm in all_contiguous_perms(searchable):
    if sum(perm) == result:
        print(max(perm)+min(perm))
##        print(perm)
##        print(searchable.index(perm[0]))
##        print(searchable[478:492])
##        print(sum(perm))
        break
