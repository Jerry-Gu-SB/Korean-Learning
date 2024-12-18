import random
import math
# get all the numbers in cur_nums.txt file in the same directory and put them all in seen_nums
seen_nums = set()

with open('cur_nums.txt', 'r') as f:
    for line in f:
        seen_nums.add(int(line.strip()))

# get a random number between 1 and 1671 inclusive
for i in range(5):
    # print the number out and then add it to the seen_nums set
    num = math.floor(1 + (1671 - 1) * random.random())

    while num in seen_nums:
        num = math.floor(1 + (1671 - 1) * random.random())

    seen_nums.add(num)
    print(num)

# write all the numbers in seen_nums to cur_nums.txt
with open('cur_nums.txt', 'w') as f:
    for num in seen_nums:
        f.write(str(num) + '\n')
