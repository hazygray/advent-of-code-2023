import itertools
import math

filename = "day11_input.txt"
file = open(filename, 'r')

grid = [[c for c in line.strip()] for line in file.readlines()]

row_offsets = [0] * (len(grid) + 1)
for r in range(len(grid)):
    st = set(grid[r])
    row_offsets[r + 1] = row_offsets[r]
    if len(st) == 1 and grid[r][0] == '.':
        row_offsets[r + 1] += 1


col_offsets = [0] * (len(grid[0]) + 1)
for c in range(len(grid[0])):
    st = set([grid[r][c] for r in range(len(grid))])
    col_offsets[c + 1] = col_offsets[c]
    if len(st) == 1 and grid[0][c] == '.':
        col_offsets[c + 1] += 1

coords = []
for r in range(len(grid)):
    for c in range(len(grid)):
        if grid[r][c] == "#":
            r_offset = row_offsets[r]
            c_offset = col_offsets[c]
            coords.append((r + r_offset, c + c_offset))

total = 0
for a, b in itertools.combinations(coords, 2):
    ax, ay = a
    bx, by = b
    total += abs(bx - ax) + abs(by - ay)
print(total)