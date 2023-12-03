import re
from collections import defaultdict
filename = "day3_input.txt"
file = open(filename, 'r')

lines = [line.strip() for line in file.readlines()]
gears = defaultdict(list)

def check_neighbors(y, x, num, visited):
    def safe_check(y, x):
        if y >= 0 and y < len(lines) and x >= 0 and x < len(lines[0]):
            if lines[y][x] != '.' and not lines[y][x].isnumeric():
                return True
        return False
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy == 0 and dx == 0:
                continue
            ny, nx = y + dy, x + dx
            if (ny, nx) in visited:
                continue
            visited.add((ny, nx))
            if safe_check(ny, nx):
                gears[(ny, nx)].append(num)

total = 0
for y in range(len(lines)):
    for match in re.finditer(r'[0-9]+', lines[y]):
        visited = set([])
        num = int(lines[y][match.start():match.end()])
        for x in range(match.start(), match.end()):
            check_neighbors(y, x, num, visited)

total = 0
for k, v in gears.items():
    if len(v) == 2:
        total += v.pop() * v.pop()
print(total)