from collections import deque

filename = "day10_input.txt"
file = open(filename, 'r')

grid = [[c for c in line.strip()] for line in file.readlines()]

neighbors = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)],
    '.': [],
    'S': [(-1, 0), (1, 0), (0, -1), (0, 1)]
}

def get_neighbors(y, x):
    res = []
    for dy, dx in neighbors[grid[y][x]]:
        ny, nx = y + dy, x + dx
        if ny >= 0 and ny < len(grid) and nx >= 0 and nx < len(grid[0]) and grid[ny][nx] != '.':
            if grid[y][x] != 'S' or (y, x) in get_neighbors(ny, nx):
                res.append((ny, nx))
    return res

def find_start():
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                return y, x

y, x = find_start()

queue = deque([(y, x, 0)])
in_loop = {}
max_cycle = 0
while queue:
    y, x, dist = queue.popleft()
    if (y, x) in in_loop:
        continue
    in_loop[(y, x)] = dist
    for ny, nx in get_neighbors(y, x):
        if (ny, nx) in in_loop:
            max_cycle = max(max_cycle, in_loop[(y, x)] + in_loop[(ny, nx)] + 1)
        else:
            queue.append((ny, nx, dist + 1))

all_tiles = len(grid) * len(grid[0])

on_path = set([])
expanded_grid = []
for y in range(len(grid)):
    row = []
    for x in range(len(grid[0])):
        row.append(grid[y][x])
        if (y, x) in in_loop:
            on_path.add((len(expanded_grid), len(row) - 1))
        row.append('X')
    expanded_grid.append(row)
    expanded_grid.append(['X'] * len(row))

grid = expanded_grid

added = set([])
for y, x in on_path:
    if expanded_grid[y][x] != 'S':
        for ny, nx in get_neighbors(y, x):
            added.add((ny, nx))
on_path = on_path.union(added)

outside = set([])
def bfs(y, x):
    def get_neighbors(y, x):
        res = []
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if ny >= 0 and ny < len(grid) and nx >= 0 and nx < len(grid[0]):
                res.append((ny, nx))
        return res
    if (y, x) in outside or (y, x) in on_path:
        return 0
    total_count = 0
    outside.add((y, x))
    if grid[y][x] != 'X':
        total_count += 1
    queue = deque([(y, x)])
    while queue:
        y, x = queue.popleft()
        for ny, nx in get_neighbors(y, x):
            if (ny, nx) not in outside and (ny, nx) not in on_path:
                if expanded_grid[ny][nx] != 'X':
                    total_count += 1
                outside.add((ny, nx))
                queue.append((ny, nx))
    return total_count

def visualize():
    line = ""
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'X':
                line += "{:>3}".format('.')
            elif (y, x) in on_path:
                line += "{:>3}".format('X')
            elif (y, x) in outside:
                line += "{:>3}".format('O')
            else:
                line += "{:>3}".format('I')
        line += "\n"
    return line

outside_total = 0
for y in range(len(grid)):
    outside_total += bfs(y, 0)
    outside_total += bfs(y, len(grid[0]) - 1)
for x in range(len(grid[0])):
    outside_total += bfs(0, x)
    outside_total += bfs(len(grid) - 1, x)

print(visualize())
print(all_tiles - max_cycle - outside_total)