with open('input.txt') as f:
    lines = [[int(i) for i in line.strip().split('x')] for line in f.readlines()]
    
result = 0
for box in lines:
    l,w,h = box
    sides = [l*w,l*h,w*h]
    area = min(sides) + 2 * sum(sides)
    result += area

print(f'Result: {result}')
    
