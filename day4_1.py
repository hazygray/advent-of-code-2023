import re
filename = "day4_input.txt"
file = open(filename, 'r')

total = 0
for line in file.readlines():
    card, game = line.split(':')
    winning, have = game.split('|')
    winning_nums = winning.split()
    have_nums = have.split()
    won = set(winning_nums).intersection(set(have_nums))
    if won:
        total += 2 ** (len(won) - 1)

print(total)