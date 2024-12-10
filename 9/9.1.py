with open('testdata.txt') as f:
    line = f.read()

line = list(line)
index = 0
blocks = []
count = 0
for number in line:
    number = int(number)
    if (count % 2) == 0:       #even
        file = [index] * number
        # print(file)
        index += 1
    else:                       #odd
        file = ['.'] * number
    count += 1
    blocks.extend(file)

for i in range(len(blocks)):
    while blocks[-1] == '.':
        blocks.pop(-1)
    if blocks[i] == '.':
        blocks[i] = blocks[-1]
        blocks.pop(-1)
    if '.' not in blocks:
        break

checksum = 0
for i in range(len(blocks)):
    checksum += i * int(blocks[i])
print(checksum)