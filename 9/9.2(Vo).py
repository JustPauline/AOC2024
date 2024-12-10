with open('data.txt') as f:
    line = f.read()

line = list(line)
index = 0
blocks = []
count = 0
indexlength = []
for number in line:
    number = int(number)
    if (count % 2) == 0:       #even
        file = [index] * number
        indexlength.append(number)
        index += 1
    else:                       #odd
        file = ['.'] * number
    count += 1
    blocks.extend(file)

indexlength = list(indexlength)
for getal in reversed(range(index)):
    for i in range(len(blocks)):
        if blocks[i:i+int(indexlength[getal])] == ['.'] * indexlength[getal] and i < blocks.index(getal):
            for j in range(len(blocks)):
                if blocks[j] == getal:
                    blocks[j] = '.'
            blocks[i:i+int(indexlength[getal])] = [getal] * indexlength[getal]
            break
checksum = 0
for i in range(len(blocks)):
    if blocks[i] != '.':
        checksum += i * int(blocks[i])
print(checksum)