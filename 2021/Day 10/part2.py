scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
pairs = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'#,
    #')': '(',
    #']': '[',
    #'}': '{',
    #'>': '<'
}

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

##lines = ['[({(<(())[]>[[{[]{<()<>>',
##'[(()[<>])]({[<{<<[]>>(',
##'{([(<{}[<>[]}>{[]{[(<()>',
##'(((({<>}<{<{<>}{[]{[]{}',
##'[[<[([]))<([[{}[[()]]]',
##'[{[{({}]{}}([{[{{{}}([]',
##'{<[[]]>}<{[{[{[]{()[[[]',
##'[<(<(<(<{}))><([]([]()',
##'<{([([[(<>()){}]>(<<{{',
##'<{([{{}}[<[[[<>{}]]]>[]']

results = []
for line in lines:
    s = []
    corrupt = False
    for char in line:
        if char in '([{<':
            s.append(char)
        elif char in ')]}>':
            if char != pairs[s[-1]]:
                # Corrupt
                corrupt = True
                break
            else:
                s.pop(-1)

    if corrupt: continue

    total = 0
    # Reached end, must be incomplete
    while len(s) > 0:
        total *= 5
        total += scores[pairs[s.pop(-1)]]
        
    results.append(total)
    
results.sort()
result = results[int((len(results) - 1) / 2)]

print(f'Result: {result}')
