from functools import reduce
import operator

filename = "day2_input.txt"
file = open(filename, 'r')

lines = file.readlines()

total = 0
for line in lines:
    game_id, game = line.split(":")
    id = int(game_id.split(" ")[1])
    cases = game.split(";")
    colors = {"red": float("-inf"), "green": float("-inf"), "blue": float("-inf")}
    for case in cases:
        pairs = case.split(",")
        for pair in pairs:
            num, color = pair.strip().split(" ")
            num = int(num)
            colors[color] = max(colors[color], num)
    total += reduce(operator.mul, colors.values(), 1)

print(total)