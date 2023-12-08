import math
import collections

filename = "day7_input.txt"
file = open(filename, 'r')

lines = [line.split() for line in file.readlines()]

cards = "AKQJT98765432"
card_to_rank = {cards[k]: k for k in range(len(cards))}
def second_order(hand):
    return [card_to_rank[c] for c in hand]

def score(line):
    hand, bid = line
    bid = int(bid)
    c = collections.Counter(hand) 
    if max(c.values()) == 1:
        return -1, *second_order(hand)
    elif max(c.values()) == 2 and len(c.values()) == 4:
        return -2, *second_order(hand)
    elif max(c.values()) == 2 and len(c.values()) == 3:
        return -3, *second_order(hand)
    elif max(c.values()) == 3 and len(c.values()) == 3:
        return -4, *second_order(hand) 
    elif max(c.values()) == 3 and len(c.values()) == 2:
        return -5, *second_order(hand) 
    elif max(c.values()) == 4:
        return -6, *second_order(hand) 
    elif max(c.values()) == 5:
        return -7, *second_order(hand) 
    else:
        raise("should not happen")

lines.sort(key=score, reverse=True)
print(sum([(k + 1) * int(lines[k][1]) for k in range(len(lines))]))