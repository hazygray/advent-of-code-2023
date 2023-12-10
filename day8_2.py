import re

filename = "day8_input.txt"
file = open(filename, 'r')

lines = [line.strip() for line in file.readlines()]
dirs = lines[0]
nodelines = lines[2:]

graph = {}
for nodeline in nodelines:
    pattern = re.compile(r'[A-Z]+')
    s, l, r = list([num for num in re.findall(r'[A-Z]+', nodeline)])
    graph[s] = [l, r]

def find_steps(c):
    steps = 0
    while c[-1] != 'Z':
        if dirs[steps % len(dirs)] == 'L':
            c = graph[c][0]
        elif dirs[steps % len(dirs)] == 'R':
            c = graph[c][1]
        steps += 1
    return steps

nums = []
for node in graph:
    if node[-1] == 'A':
        nums.append(find_steps(node))

def gcd(a, b):
    if b < a:
        a, b = b, a
    if b % a == 0:
        return a
    return gcd(a, b % a)


def lcm(nums):
    c = 1
    for num in nums:
        g = gcd(c, num)
        c *= num
        c //= g
    return c

print(lcm(nums))