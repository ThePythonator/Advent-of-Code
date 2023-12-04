with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


total_length = len(''.join(lines))
true_length = len(bytes(''.join([line[1:-1] for line in lines]), "utf-8").decode("unicode_escape"))

result = total_length - true_length

print(f'Result: {result}')