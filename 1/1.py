left = []
right = []

with open('data.txt')as f:
    for line in f:
        line = line.strip()
        sep = line.split(' ')
        left.append(int(sep[0]))
        right.append(int(sep[-1]))

# Part 1
# left.sort()
# right.sort()
#
# total = 0
#
# for i in range(len(left)):
#     difference = abs(left[i] - right[i])
#     total += difference
#
# print(total)

# Part 2
totalscore = 0
for value in left:
    score = value * right.count(value)
    totalscore += score

print(totalscore)