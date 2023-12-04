with open('in.txt') as f:
    lines = [int(line.strip()) for line in f.readlines()]

lines.sort()

start = 0
end = max(lines)+3

lines = [start]+lines+[end]

##diffs = [0,0,0]
##
##for i in range(1,len(lines)):
##    diffs[lines[i]-lines[i-1]-1] += 1
##
##print(diffs[0]*diffs[2])
