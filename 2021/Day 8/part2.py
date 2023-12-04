UNIQUE = [1, 4, 7, 8]
NON_UNIQUE = [0, 2, 3, 5, 6, 9]

#  0000
# 1    2
# 1    2
#  3333
# 4    5
# 4    5
#  6666

SEGMENTS = [
    [0, 1, 2, 4, 5, 6],
    [2, 5],
    [0, 2, 3, 4, 6],
    [0, 2, 3, 5, 6],
    [1, 2, 3, 5],
    [0, 1, 3, 5, 6],
    [0, 1, 3, 4, 5, 6],
    [0, 2, 5],
    [0, 1, 2, 3, 4, 5, 6],
    [0, 1, 2, 3, 5, 6]
]

def decode(digits):
    results = {key: -1 for key in digits}
    mapping = {key: -1 for key in 'abcdefg'}
   
    for digit in digits:
        for d in UNIQUE:
            if len(digit) == len(SEGMENTS[d]):
                # Must be that digit
                results[digit] = d

    # Sorry about hardcoding stuff
   
    # Find segment 0
    one = seven = four = eight = None
    for k in results.keys():
        if results[k] == 7:
            seven = k

        elif results[k] == 1:
            one = k

        elif results[k] == 8:
            eight = k

        elif results[k] == 4:
            four = k

    letter = [c for c in seven if c not in one][0]
    mapping[letter] = 0


    # Find segment 2
    b = []
    for k in results.keys():
        if len(k) == 6:
            # 6, 9 or 0
            b.append(k)

    six = None
    for item in b:
        t = 0
        for char in item:
            if char in one:
                t += 1
        if t == 1:
            six = item # must be 6

    b.remove(six)

    nine = None
    for item in b:
        t = 0
        for char in four:
            if char in item:
                t += 1

        if t == len(SEGMENTS[4]):
            nine = item # must be 9

    b.remove(nine)
    zero = b[0] # must be 0
    b.remove(zero)

    letter = [char for char in eight if char not in six][0]
    mapping[letter] = 2
   

    five = nine
    five = five.replace(letter, '')

    # Find segment 5
    letter = [char for char in one if char not in six][0]
    mapping[letter] = 5
   
    # Find segment 6
    letter = [char for char in [char for char in nine if char not in four] if mapping[char] != 0][0]
    mapping[letter] = 6

    # Find segment 3
    letter = [char for char in eight if char not in zero][0]
    mapping[letter] = 3

    # Find segment 4
    letter = [char for char in [char for char in six if char not in five] if mapping[char] != 2][0]
    mapping[letter] = 4

    # Get '3'
    # Made of seven + seg3 + seg6
    three = seven
    for k in mapping.keys():
        if mapping[k] in [3, 6]:
            three += k
    three = ''.join(sorted(three))

    # Get '2'
    # Last left
    two = None
    for digit in digits:
        if digit not in [zero, one, three, four, five, six, seven, eight, nine]:
            two = digit

    # Find segment 1
    letter = [char for char in [char for char in eight if char not in two] if mapping[char] != 5][0]
    mapping[letter] = 1

    results[zero] = 0
    results[one] = 1
    results[two] = 2
    results[three] = 3
    results[four] = 4
    results[five] = 5
    results[six] = 6
    results[seven] = 7
    results[eight] = 8
    results[nine] = 9

    return results

def get_value(num, results):
    value = 0
    power = 1000
    for digit in num:
        value += power * results[digit]
        power /= 10
    return int(value)  

with open('input.txt') as f:
    lines = [line.strip().split(' | ') for line in f.readlines()]


data = [[[''.join(sorted(s)) for s in item.split(' ')] for item in line] for line in lines]

total = 0
for line in data:
    results = decode(line[0])
    total += get_value(line[1], results)

print(f'Result: {total}')