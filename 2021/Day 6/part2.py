def count_sim(f_l, days):
    return sum([table[days][item-1] for item in f_l])

with open('input.txt') as f:
    fish = [int(item) for item in f.readlines()[0].strip().split(',')]

#fish = [3,4,3,1,2]

table = [[1]*9]
for i in range(1,257):
    row = []
    for j in range(9):
        c = 0
        if j == 0 and i > 1:
            c += table[i - 1][8] + table[i - 1][6]
        else:
            c += table[i - 1][j - 1]
        row.append(c)
    table.append(row)

r = count_sim(fish, 256)

print(f'Results: {r}')