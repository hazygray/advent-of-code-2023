import re
filename = "day4_input.txt"
file = open(filename, 'r')

total = 0
lines = file.readlines()

decrements = [0] * (len(lines) + 1)
current = 1

for k in range(len(lines)):
    current += decrements[k]
    total += current
    card, game = lines[k].split(':')
    winning, have = game.split('|')
    winning_nums = winning.split()
    have_nums = have.split()
    won = len(set(winning_nums).intersection(set(have_nums)))
    if won > 0:
        decrements[k + won + 1] -= current
        current += current

print(total)