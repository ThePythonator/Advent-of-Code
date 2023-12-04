with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

nums = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

result = 0
for line in lines:
    ints = []
    for i in range(len(line)):
        for j, s in enumerate(nums):
            if line[i:].startswith(s):
                ints.append(j + 1)
            elif line[i] in "123456789":
                ints.append(int(line[i]))
    result += 10 * int(ints[0]) + int(ints[-1])

print(f'Result: {result}')
