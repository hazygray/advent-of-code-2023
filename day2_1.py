filename = "day2_input.txt"
file = open(filename, 'r')

lines = file.readlines()

total = 0

q = {"red": 12, "green": 13, "blue": 14}

total = 0
for line in lines:
    game_id, game = line.split(":")
    id = int(game_id.split(" ")[1])
    cases = game.split(";")
    ok = True
    for case in cases:
        pairs = case.split(",")
        for pair in pairs:
            num, color = pair.strip().split(" ")
            if int(num) > q[color]:
                ok = False
    if ok:
        total += id
print(total)