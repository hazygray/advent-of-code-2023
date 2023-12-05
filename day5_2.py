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

map_names = []
while ind < len(lines):
    if is_mapline(lines[ind]):
        map_names.append(lines[ind])
        ind += 1
        mp = {}
        while ind < len(lines) and not is_mapline(lines[ind]):
            if is_rangeline(lines[ind]):
                dest, src, rng = [int(num) for num in lines[ind].split()]
                offset = dest - src
                mp[(src, rng)] = offset
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

seed_intervals = [(seeds[k], seeds[k + 1]) for k in range(0, len(seeds), 2)]

def dfs(maps, mp_ind, src, rng):
    if rng <= 0:
        return float("inf")
    if mp_ind >= len(maps):
        return src
    
    result = float("inf") 

    prev = src
    for s, r in sorted(maps[mp_ind].keys()):
        if s > src + rng:
            break
        current = max(s, src)
        next_ = max(current, min(s + r, src + rng))
        offset = maps[mp_ind][(s, r)]
        result = min(result, dfs(maps, mp_ind + 1, prev, current - prev))
        result = min(result, dfs(maps, mp_ind + 1, current + offset, next_ - current))

        prev = next_

    current = src + rng
    result = min(result, dfs(maps, mp_ind + 1, prev, current - prev))

    return result


print(min([dfs(maps, 0, src, rng) for src, rng in seed_intervals]))