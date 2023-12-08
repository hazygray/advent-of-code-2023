import math
import collections

filename = "day7_input.txt"
file = open(filename, 'r')

lines = [line.split() for line in file.readlines()]

cards = "AKQT98765432J"
card_to_rank = {cards[k]: k for k in range(len(cards))}
def second_order(hand):
    return [card_to_rank[c] for c in hand]

def possible_hands(hand, hand_so_far, k):
    if k >= len(hand):
        return [hand_so_far]
    hands = []
    if hand[k] == 'J':
        hands = []
        for c in cards:
            hands += possible_hands(hand, hand_so_far + c, k + 1)
        return hands
    else:
        return possible_hands(hand, hand_so_far + hand[k], k + 1)

def score(line):
    hand, bid = line
    bid = int(bid)
    def subscore(hand):
        c = collections.Counter(hand) 
        if max(c.values()) == 1:
            return -1
        elif max(c.values()) == 2 and len(c.values()) == 4:
            return -2
        elif max(c.values()) == 2 and len(c.values()) == 3:
            return -3
        elif max(c.values()) == 3 and len(c.values()) == 3:
            return -4 
        elif max(c.values()) == 3 and len(c.values()) == 2:
            return -5 
        elif max(c.values()) == 4:
            return -6 
        elif max(c.values()) == 5:
            return -7 
        else:
            raise("should not happen")
    hands = possible_hands(hand, "", 0)
    return min([subscore(hand) for hand in hands]), second_order(hand)

lines.sort(key=score, reverse=True)
print(sum([(k + 1) * int(lines[k][1]) for k in range(len(lines))]))