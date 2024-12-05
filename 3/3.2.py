import re

with open('data.txt')as f:
    data = f.read()

mul_pattern = re.compile(r"mul\(\d+,\d+\)")
do_pattern = re.compile(r"do\(\)")
dont_pattern = re.compile(r"don't\(\)")

enabled = True
total = 0

for instruction in re.finditer(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data):
    instr = instruction.group()
    if do_pattern.match(instr):
        enabled = True
    elif dont_pattern.match(instr):
        enabled = False
    elif mul_pattern.match(instr) and enabled:
        operands = list(map(int, instr.strip("mul()").split(',')))
        total += operands[0] * operands[1]

print(total)
