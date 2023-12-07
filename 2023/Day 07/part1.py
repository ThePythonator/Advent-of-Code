import os
SCRIPT_PATH = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(SCRIPT_PATH, "input.txt")) as f:
    lines = [line.strip() for line in f.readlines()]


hands = {
    "5": [],
    "4": [],
    "3+2": [],
    "3": [],
    "2+2": [],
    "2": [],
    "1": []
}

for i, line in enumerate(lines):
    cards, bid = line.split()
    bid = int(bid)
    cs = {}
    for c in cards:
        if c not in cs:
            cs[c] = 0
        cs[c] += 1

    maxv = 0
    for k, v in cs.items():
        maxv = max(maxv, v)
        
    if maxv > 3:
        hands[str(maxv)].append((cards, bid))
    elif maxv == 3:
        if len(cs.keys()) == 2:
            hands["3+2"].append((cards, bid))
        else:
            hands["3"].append((cards, bid))
    elif maxv == 2:
        if len(cs.keys()) == 3:
            hands["2+2"].append((cards, bid))
        else:
            hands["2"].append((cards, bid))
    else:
        hands["1"].append((cards, bid))

ranks = []
c = 0
for k in ["5", "4", "3+2", "3", "2+2", "2", "1"]:
    sort = sorted(hands[k], key=lambda x: ["23456789TJQKA".index(y) for y in x[0]], reverse=True)
    ranks += [(sort[i], i + c) for i in range(len(hands[k]))]
    c += len(hands[k])

result = sum([rank[0][1] * (len(lines) - rank[1]) for rank in ranks])

print(f"Result: {result}")
