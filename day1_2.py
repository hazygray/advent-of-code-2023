import re

filename = "day1_input.txt"
file = open(filename, 'r')

lines = file.readlines()

digit_strs = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digits = "123456789"

def check_line(reverse=False):
    found = None
    r = range(0, len(line))
    if reverse:
        r = reversed(r)
    for k in r:
        if found != None:
            break
        if line[k] in digits:
            found = line[k]
        for j in range(len(digit_strs)):
            if line[k:k + len(digit_strs[j])] == digit_strs[j]:
                found = str(j + 1)
                break
    return found

total = 0
for line in lines:
    first = check_line()
    last = check_line(reverse=True)
    total += int(first + last)
print(total)
