# Guessed: 16394 (mistake), 950 (correct)

from collections import Counter

def add_positions(a, b):
    return [a[0] + b[0], a[1] + b[1]]

def swap_plus(a):
    return [a[1], a[0]]

def swap_minus(a):
    return [-a[1], -a[0]]

def get_propositions(elves, order):
    propositions = []
    counts = Counter()
    for e in elves:
        c = 0
        proposition = e
        for o in order:
            p = add_positions(e, o)
            if p not in elves and add_positions(p, swap_plus(o)) not in elves and add_positions(p, swap_minus(o)) not in elves:
                if c == 0:
                    proposition = p
                c += 1
            elif c > 0:
                break
        if c == 4:
            proposition = e
        counts[tuple(proposition)] += 1
        propositions.append(proposition)
    return propositions, counts

def filter_propositions(elves, propositions, counts):
    return [elves[j] if counts[tuple(propositions[j])] > 1 else propositions[j] for j in range(len(propositions))]

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

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

elves = [[x,y] for y in range(len(lines)) for x in range(len(lines[0])) if lines[y][x] == '#']

order = [[0,-1],[0,1],[-1,0],[1,0]]

i = 0
running = True
while running:
    # s = ['.'*14] * 12
    # for x,y in elves:
    #     s[y] = s[y][:x] + '#' + s[y][x+1:]
    # print('\n'.join(s))
    # input()
    propositions, counts = get_propositions(elves, order)
    if elves == propositions:
        running = False
    elves = filter_propositions(elves, propositions, counts)
    order = order[1:] + [order[0]]
    i += 1
    print(f'Finished round {i}.')

# s = ['.'*14] * 12
# for x,y in elves:
#     s[y] = s[y][:x] + '#' + s[y][x+1:]
# print('\n'.join(s))
# input()
result = i

print(f'Result: {result}')
