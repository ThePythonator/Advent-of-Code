with open('input.txt') as f:
    lines = [[int(i) for i in line.strip().split('x')] for line in f.readlines()]
    
result = 0
for box in lines:
    l,w,h = box
    perimeters = [2*(l+w),2*(l+h),2*(w+h)]
    area = min(perimeters) + l*w*h
    result += area

print(f'Result: {result}')

