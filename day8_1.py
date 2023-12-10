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
    while c != 'ZZZ':
        print(c)
        if dirs[steps % len(dirs)] == 'L':
            c = graph[c][0]
        elif dirs[steps % len(dirs)] == 'R':
            c = graph[c][1]
        steps += 1
    return steps


print(find_steps('AAA'))

# find the lcm
# gcd