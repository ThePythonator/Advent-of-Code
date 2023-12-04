# Guessed: 1248, 1262 (correct 2nd time)

def sim_option(o, c, ob_o, ob_c, g_o, g_ob, opt):
    ore = 0
    clay = 0
    obsidian = 0
    geodes = 0

    rbts = [1,0,0,0]

    t = 24

    new_opt = True
    new_rbt = -1

    while t > 0:
        t -= 1

        if new_opt:
            next_opt = 3 if len(opt) == 0 else opt.pop(0)
            new_opt = False

        if ore >= g_o and obsidian >= g_ob:
            new_rbt = 3
            ore -= g_o
            obsidian -= g_ob

        elif ore >= ob_o and clay >= ob_c and next_opt == 2:
            new_rbt = 2
            ore -= ob_o
            clay -= ob_c

        elif ore >= c and next_opt == 1:
            new_rbt = 1
            ore -= c

        elif ore >= o and next_opt == 0:
            new_rbt = 0
            ore -= o

        ore += rbts[0]
        clay += rbts[1]
        obsidian += rbts[2]
        geodes += rbts[3]

        if new_rbt >= 0:
            rbts[new_rbt] += 1
            new_rbt = -1
            new_opt = True

    #     print(24-t, ore, clay, obsidian, geodes, rbts)
            
    # print(ore, clay, obsidian, geodes, rbts)
    # input(f"Geodes: {geodes}")
    return geodes

def gen_options(o_cst, c_cst, ob_cst_o, ob_cst_c, g_cst_o, g_cst_ob):
    ore = 0
    clay = 0
    obsidian = 0
    geodes = 0

    o_rbts = 1
    c_rbts = 0
    ob_rbts = 0
    g_rbts = 0

    t = 24

    mx_o_rbts = max(o_cst, c_cst, ob_cst_o, g_cst_o)
    mx_c_rbts = ob_cst_c
    mx_ob_rbts = g_cst_ob

    # 0 = ore
    # 1 = clay
    # 2 = obsidian
    # 3 = geode

    opts = []

    JAMMY_FACTOR = [0,0,0]
    JAMMY_FACTOR = [3,2,1]

    while t > 0:
        t -= 1

        ore += o_rbts
        clay += c_rbts
        obsidian += ob_rbts
        geodes += g_rbts

        o_loss = []

        chs = []

        if ore >= g_cst_o and obsidian >= g_cst_ob:
            g_rbts += 1
            o_loss.append(g_cst_o)
            obsidian -= g_cst_ob
            # chs.append(3)

        if ore >= ob_cst_o and clay >= ob_cst_c and ob_rbts < mx_ob_rbts + JAMMY_FACTOR[2]:
            ob_rbts += 1
            o_loss.append(ob_cst_o)
            clay -= ob_cst_c
            chs.append(2)

        if ore >= c_cst and c_rbts < mx_c_rbts + JAMMY_FACTOR[1]:
            c_rbts += 1
            o_loss.append(c_cst)
            chs.append(1)

        if ore >= o_cst and o_rbts < mx_o_rbts + JAMMY_FACTOR[0]:
            o_rbts += 1
            o_loss.append(o_cst)
            chs.append(0)

        if len(o_loss) == 4: ore -= min(o_loss)

        opts.append(chs)

    return opts

def convert_seq(options):
    seqs = set()
    for round in options:
        temp = seqs.copy()
        for option in round:
            for item in temp:
                seqs.add(tuple(list(item)+[option]))
            if len(temp) == 0:
                seqs.add(tuple([option]))
    return seqs

def solve(a,b,c,d,e,f):
    options = gen_options(a,b,c,d,e,f)
    seqences = convert_seq(options)
    print(f"Trying {len(seqences)} possible sequences...")
    # input(len(seqences))
    # if (1,1,1,2,1,2) in seqences:
    #     print("Yes")
    #     sim_option(a,b,c,d,e,f,[1,1,1,2,1,2])
    # exit()
    return max([sim_option(a,b,c,d,e,f,list(seq)) for seq in seqences])

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

_lines = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian""".split('\n')

bp_qualities = []

for i, line in enumerate(lines):
    l = line.split(' ')
    geodes = solve(int(l[6]), int(l[12]), int(l[18]), int(l[21]), int(l[27]), int(l[30]))
    print(f"Blueprint {i+1} resulted in {geodes} geodes.")
    bp_qualities.append((i + 1) * geodes)

result = sum(bp_qualities)

print(f'Result: {result}')
