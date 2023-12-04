def add_positions(a, b):
    return [a[0] + b[0], a[1] + b[1]]

def swap_plus(a):
    return [a[1], a[0]]

def swap_minus(a):
    return [-a[1], -a[0]]

def get_propositions(elves, order):
    propositions = []
    for e in elves:
        c = 0
        proposition = e
        for o in order:
            p = add_positions(e, o)
            if p not in elves and add_positions(p, swap_plus(o)) not in elves and add_positions(p, swap_minus(o)) not in elves:
                if c == 0:
                    proposition = p
                c += 1
        if c == 4:
            proposition = e
        propositions.append(proposition)
    return propositions

def filter_propositions(elves, propositions):
    return [elves[j] if propositions.count(propositions[j]) > 1 else propositions[j] for j in range(len(propositions))]

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

_lines = """.....
..##.
..#..
.....
..##.
.....""".split('\n')

_lines = """..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............""".split('\n')

elves = []
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == '#':
            elves.append([x,y])

order = [[0,-1],[0,1],[-1,0],[1,0]]

for i in range(10):
    # s = ['.'*14] * 12
    # for x,y in elves:
    #     s[y] = s[y][:x] + '#' + s[y][x+1:]
    # print('\n'.join(s))
    # input()
    propositions = get_propositions(elves, order)
    elves = filter_propositions(elves, propositions)
    order = order[1:] + [order[0]]

# s = ['.'*14] * 12
# for x,y in elves:
#     s[y] = s[y][:x] + '#' + s[y][x+1:]
# print('\n'.join(s))
# input()
result = (1 + max([x for x,y in elves]) - min([x for x,y in elves])) * (1 + max([y for x,y in elves]) - min([y for x,y in elves])) - len(elves)

print(f'Result: {result}')
