with open('input.txt') as f:
    fish = [line.strip() for line in f.readlines()][0].split(',')

fish = [int(f) for f in fish]

def sim_day(fish):
    new_fish = []
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 6
            new_fish.append(8)
            
        else:
            fish[i] -= 1
            
    return fish + new_fish

for i in range(80):
    fish = sim_day(fish)

print(f'Result: {len(fish)}')
