import re
filename = "day5_input.txt"
file = open(filename, 'r')

lines = [line.strip() for line in file.readlines()]
seedline, lines = lines[0], lines[1:]
_, seeds = seedline.split(":")
seeds = [int(seed) for seed in seeds.split()]

maps = []
ind = 0

def is_mapline(line):
    return re.match(r'[a-z]', line)

def is_rangeline(line):
    return re.match(r'[0-9]', line)

while ind < len(lines):
    if is_mapline(lines[ind]):
        ind += 1
        mp = {}
        while ind < len(lines) and not is_mapline(lines[ind]):
            if is_rangeline(lines[ind]):
                dest, src, rng = [int(num) for num in lines[ind].split()]
                mp[(src, rng)] = dest
            ind += 1
        maps.append(mp)
        continue
    ind += 1

def to_location(seed):
    current = seed
    for mp in maps:
        for src, rng in mp:
            if current >= src and current < src + rng:
                offset = current - src
                dest = mp[(src, rng)]
                current = dest + offset
                break
    return current

print(min([to_location(seed) for seed in seeds]))