with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]


true_length = len(''.join(lines))
total_length = len(''.join(lines).replace('\\','\\\\').replace('\"','\\\"')) + len(lines) * 2



result = total_length - true_length

print(f'Result: {result}')