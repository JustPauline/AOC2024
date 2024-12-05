import re

with open('data.txt')as f:
    data = f.read()

multiplications = re.findall(r"mul\(\d+,\d+\)", data)

total = 0
for som in multiplications:
    som = som.strip('mul()').split(',')
    total += int(som[0])*int(som[1])

print(total)