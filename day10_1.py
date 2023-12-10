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
visited = {}
max_cycle = 0
while queue:
    y, x, dist = queue.popleft()
    if (y, x) in visited:
        continue
    visited[(y, x)] = dist
    for ny, nx in get_neighbors(y, x):
        if (ny, nx) in visited:
            max_cycle = max(max_cycle, visited[(y, x)] + visited[(ny, nx)] + 1)
        else:
            queue.append((ny, nx, dist + 1))

def visualize():
    line = ""
    for y in range(len(grid)):
        for x in range(len(grid[0]) * 1 // 3):
            if (y, x) in visited:
                line += "{:>3}".format(str(visited[(y, x)]))
            else:
                line += "{:>3}".format('.')
        line += "\n"
    return line

print(visualize())
print(max_cycle // 2)