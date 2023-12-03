import re
filename = "day3_input.txt"
file = open(filename, 'r')

lines = [line.strip() for line in file.readlines()]

def check_neighbors(y, x):
    def safe_check(y, x):
        if y >= 0 and y < len(lines) and x >= 0 and x < len(lines[0]):
            if lines[y][x] != '.' and not lines[y][x].isnumeric():
                print(lines[y][x])
                return True
        return False
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy == 0 and dx == 0:
                continue
            ny, nx = y + dy, x + dx
            if safe_check(ny, nx):
                return True
    return False

total = 0
for y in range(len(lines)):
    for match in re.finditer(r'[0-9]+', lines[y]):
        for x in range(match.start(), match.end()):
            if check_neighbors(y, x):
                total += int(lines[y][match.start():match.end()])
                break

print(total)