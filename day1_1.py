import re

filename = "day1_input.txt"
file = open(filename, 'r')

lines = file.readlines()

total = 0

for line in lines:
    pattern = re.compile(r'[0-9]')
    nums = list([num for num in re.findall(pattern, line)])
    total += int(nums[0] + nums[-1])
print(total)