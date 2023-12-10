import re
filename = "day9_input.txt"
file = open(filename, 'r')

lines = [[int(num) for num in line] for line in [line.strip().split() for line in file.readlines()]]

def add_next(nums):
    if nums[0] == 0 and nums[-1] == 0:
        return nums
    next_ = add_next([nums[k] - nums[k - 1] for k in range(1, len(nums))])
    return nums + [nums[-1] + next_[-1]]

total = 0
for line in lines:
    line = line[::-1]
    line = add_next(line)
    total += line[-1]
print(total)