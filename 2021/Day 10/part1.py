scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
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

total = 0
for line in lines:
    #corrupt = False
    s = []
    for char in line:
        if char in '([{<':
            s.append(char)
        elif char in ')]}>':
            if char != pairs[s[-1]]:
                # Corrupt
                total += scores[char]
                #corrupt = True
                break
            else:
                s.pop(-1)

print(f'Result: {total}')
