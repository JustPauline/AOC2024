rules = []
updates = []
total = 0
incorrect = []

def checkorder(line):
    check = True
    for rule in rules:
        if rule[0] in line and rule[1] in line:
            if line.index(rule[0]) > line.index(rule[1]):
                check = False
                break
    if check:
        return True

with open('data.txt') as f:
    for line in f:
        if '|' in line:
            rules.append(line.strip().split('|'))
        else:
            updates.append(line.strip().split(','))

updates.pop(0)

for update in updates:
    if not checkorder(update):
        incorrect.append(update)

for update in incorrect:
    while not checkorder(update):
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    update[update.index(rule[0])], update[update.index(rule[1])] = update[update.index(rule[1])], update[update.index(rule[0])]

    index = int(len(update)/2)
    total += int(update[index])
print(total)