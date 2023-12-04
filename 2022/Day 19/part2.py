# Guessed: 25568, 27489, 37191 (correct)

def can_build(resources, cost):
    for i in range(len(resources)):
        if resources[i] < cost[i]:
            return False
    return True

def build(resources, cost):
    return [resources[i] - cost[i] for i in range(len(resources))]

# TODO: rewrite gen_options to generate all possible actual arrangements
# DFS through to get all arrangements

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3

TYPES = 4


MINUTES = 32

# state:
# [time, resources, robots]
TIME = 0
RESOURCES = 1
ROBOTS = 2

def copy_state(s):
    return [s[TIME], s[RESOURCES].copy(), s[ROBOTS].copy()]

def tuplify(s):
    return (s[TIME], tuple(s[RESOURCES]), tuple(s[ROBOTS]))

# This doesn't work :(
def solve(robot_costs):
    q = []

    # q.append([12, [1,7,1,0], [1,4,1,0]])
    q.append([MINUTES, [0,0,0,0], [1,0,0,0]])

    max_robots = [
        max([robot_costs[i][ORE] for i in range(TYPES)]),
        robot_costs[OBSIDIAN][CLAY],
        robot_costs[GEODE][OBSIDIAN],
        999999999
    ]

    max_geodes = 0

    visited = set()

    while len(q) > 0:
        state = q.pop()
        
        for i in range(TYPES - 1):
            # Not even sure if it'll help except near the very end
            # state[RESOURCES][i] = min(state[RESOURCES][i], max_robots[i] * state[TIME])
            # This is more agressive and might actually help, but may be wrong, but seems to work
            state[RESOURCES][i] = min(state[RESOURCES][i], max_robots[i] * 2)
            # state[RESOURCES][i] = min(state[RESOURCES][i], max_robots[i])

        t_state = tuplify(state)

        if t_state in visited:
            continue

        visited.add(t_state)

        if state[TIME] * (state[ROBOTS][GEODE] + (state[TIME] + 1) // 2) + state[RESOURCES][GEODE] <= max_geodes:
            continue

        new_resources = state[ROBOTS].copy()

        state[TIME] -= 1

        if state[TIME] == 0:
            max_geodes = max(max_geodes, new_resources[GEODE] + state[RESOURCES][GEODE])
            continue

        
        # print(state, max_geodes)
        # input()

        if can_build(state[RESOURCES], robot_costs[GEODE]):
            temp_state = copy_state(state)
            temp_state[RESOURCES] = build(temp_state[RESOURCES], robot_costs[GEODE])
            temp_state[ROBOTS][GEODE] += 1
            temp_state[RESOURCES] = [new_resources[i] + temp_state[RESOURCES][i] for i in range(TYPES)]
            q.append(temp_state)
            continue

        can_build_all = True
        for i in range(TYPES - 1):
            if can_build(state[RESOURCES], robot_costs[i]) and state[ROBOTS][i] < max_robots[i]:
                temp_state = copy_state(state)
                temp_state[RESOURCES] = build(temp_state[RESOURCES], robot_costs[i])
                temp_state[ROBOTS][i] += 1
                temp_state[RESOURCES] = [new_resources[i] + temp_state[RESOURCES][i] for i in range(TYPES)]
                q.append(temp_state)
            else:
                can_build_all = False

        if not can_build_all:
            state[RESOURCES] = [new_resources[i] + state[RESOURCES][i] for i in range(TYPES)]
            q.append(state)

    return max_geodes

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

_lines = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian""".split('\n')

values = []

for i in range(3):
# for i in range(len(lines)):
    l = lines[i].split(' ')
    geodes = solve([[int(l[6]),0,0,0], [int(l[12]),0,0,0], [int(l[18]),int(l[21]),0,0], [int(l[27]),0,int(l[30]),0]])
    print(f"Blueprint {i+1} resulted in {geodes} geodes.")
    values.append(geodes)

def product(x):
    return 1 if len(x) == 0 else x[0] * product(x[1:])

result = product(values)

print(f'Result: {result}')
