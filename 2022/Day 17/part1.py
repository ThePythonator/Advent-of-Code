ROCKS = [
    [
        ['#','#','#','#']
    ],
    [
        ['.','#','.'],
        ['#','#','#'],
        ['.','#','.']
    ],
    [
        ['.','.','#'],
        ['.','.','#'],
        ['#','#','#']
    ],
    [
        ['#'],
        ['#'],
        ['#'],
        ['#']
    ],
    [
        ['#','#'],
        ['#','#']
    ]
]

WIDTH = 7

NEW_ROW = ['.' for i in range(WIDTH)]

TUNNEL = [NEW_ROW.copy()]

# Bottom left
# y coord is above highest rock in room, or floor
START = [2, 3]

def get_next_start(tunnel):
    for i, row in enumerate(tunnel):
        if '#' not in row:
            return [START[0], i + START[1]]
            
    return [START[0], i + START[1] + 1]

def collisions(tunnel, rock_index, rock_pos):
    x, y = rock_pos
    for row in ROCKS[rock_index][::-1]:
        if y >= len(tunnel):
            break

        for i, c in enumerate(tunnel[y]):
            p = i - x

            if p >= 0 and p < len(row) and row[p] == c == '#':
                return True

        y += 1

    return False

def place_rock(tunnel, rock_index, rock_pos):
    x, y = rock_pos

    while y + len(ROCKS[rock_index]) > len(tunnel):
        tunnel.append(NEW_ROW)

    for row in ROCKS[rock_index][::-1]:
        s = []

        for i, c in enumerate(tunnel[y]):
            p = i - x

            if p >= 0 and p < len(row) and row[p] == '#':
                s.append('#')

            else:
                s.append(c)

        tunnel[y] = s

        y += 1

    return tunnel


with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

s = lines[0]
# s = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

pos = None
r_i = -1 # rock index
new_rock = True

k = 0
running = True
r_c = 0
while running:
    c = s[k]
    k += 1
    k %= len(s)

    # If create new rock:
    if new_rock:
        pos = get_next_start(TUNNEL)
        r_i += 1
        r_i %= 5

        new_rock = False

    if c == '<':
        pos[0] -= 1

        if pos[0] < 0 or collisions(TUNNEL, r_i, pos):
            pos[0] += 1
    
    elif c == '>':
        pos[0] += 1
        
        if pos[0] + len(ROCKS[r_i][0]) - 1 >= WIDTH or collisions(TUNNEL, r_i, pos):
            pos[0] -= 1

    pos[1] -= 1

    if pos[1] < 0 or collisions(TUNNEL, r_i, pos):
        pos[1] += 1

        new_rock = True

        TUNNEL = place_rock(TUNNEL, r_i, pos)

        r_c += 1

        if r_c >= 2022:
            running = False

result = len(TUNNEL)

print(f'Result: {result}')
