import math
filename = "day6_input.txt"
file = open(filename, 'r')

_, racevalues = file.readline().split(":")
race = int("".join(racevalues.split()))

_, distancevalues = file.readline().split(":")
distance = int("".join(distancevalues.split()))

def quadratic(a, b, c):
    s1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    s2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return sorted([s1, s2])

def calculate(t, d):
    s1, s2 = quadratic(-1, t, -d)
    s1 = math.ceil(s1)
    s2 = math.floor(s2)
    return s2 - s1 + 1

total = calculate(race, distance + 1)

print(total)
