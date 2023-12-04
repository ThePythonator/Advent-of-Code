with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

max_coord = 4000000

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def clamped_min_max(p, r):
    return [max(0, min(max_coord, p - r)), max(0, min(max_coord, p + r))]

class Sensor:
    def __init__(self, pos, nearest_beacon):
        self.pos = pos
        self.beacon = nearest_beacon
        self.range = dist(pos, nearest_beacon)

# lines = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3""".split('\n')

sensors = []
beacons = set()

for line in lines:
    l = line.split(' ')
    a = int(l[2].split('=')[1].split(',')[0])
    b = int(l[3].split('=')[1].split(':')[0])
    c = int(l[-2].split('=')[1].split(',')[0])
    d = int(l[-1].split('=')[1])

    sensors.append(Sensor([a,b], [c,d]))
    beacons.add((c,d))

result = 0

for y in range(max_coord):
    c = sum([1 for b in beacons if b[1] == y])

    intervals = []
    for s in sensors:
        d = abs(y - s.pos[1])

        if d <= s.range:
            intervals.append(clamped_min_max(s.pos[0], s.range - d))

    intervals.sort()

    condensed_intervals = []

    current_start, current_stop = intervals[0]
    for start, stop in intervals[1:]:
        if start <= current_stop:
            current_stop = max(stop, current_stop)
        else:
            condensed_intervals.append((current_start, current_stop))
            current_start, current_stop = start, stop
    condensed_intervals.append((current_start, current_stop))

    if condensed_intervals[0] != (0, 4000000):
        if len(condensed_intervals) == 1:
            x = 0 if condensed_intervals[0][0] != 0 else 4000000

        else:
            x = condensed_intervals[0][1] + 1
            
        # print(intervals)
        # print(condensed_intervals)
        # print("x,y:", x, y)

        result = x * 4000000 + y
        break

    # r = sum([1 + b - a for a, b in condensed_intervals]) - c

print(f'Result: {result}')
