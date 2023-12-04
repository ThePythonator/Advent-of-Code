import json

def in_order(a, b):
    # 1 for a < b, 0 for a = b, -1 for a > b

    if type(a) == list and type(b) == int:
        b = [b]
    elif type(a) == int and type(b) == list:
        a = [a]

    # print(f'Entering:\t{a}\n\t\t{b}')

    if type(a) == list and type(b) == list:
        for i in range(min(len(a),len(b))):
            r = in_order(a[i], b[i])

            if r < 0:
                return -1
            elif r > 0:
                return 1

        return in_order(len(a), len(b))

    elif type(a) == int and type(b) == int:
        # print(f"both int, returning {1 if a < b else 0 if a == b else -1}")
        return 1 if a < b else 0 if a == b else -1
    
    input(f'ARGH: {a},{b}')
            

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# lines = """[1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]""".split('\n')

v = []
for i in range(0, len(lines), 3):
    a = json.loads(lines[i])
    b = json.loads(lines[i+1])

    if in_order(a, b) >= 0:
        v.append(i // 3 + 1)
        # print(i//3+1)

    # input(f"-> {in_order(a, b)}")

result = sum(v)

print(f'Result: {result}')
