rules = []
updates = []
total = 0
correct = []

with open('testdata.txt') as f:
    for line in f:
        if '|' in line:
            rules.append(line.strip().split('|'))
        else:
            updates.append(line.strip().split(','))

updates.pop(0)
for update in updates:
    check = True
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                check = False
                break
    if check:
        correct.append(update)

for entry in correct:
    index = int(len(entry)/2)
    total += int(entry[index])
print(total)