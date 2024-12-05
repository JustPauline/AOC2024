count = 0
unsafe = []

def checksafety(line):
    order = False
    check = True

    ascending = sorted(line)
    descending = sorted(line, reverse=True)
    if line == ascending or line == descending:
        order = True
    for i in range(len(line) - 1):
        if abs(int(line[i]) - int(line[i + 1])) > 3 or line[i] == line[i + 1]:
            check = False
    if order and check:
        return True

with open('data.txt')as f:
    for line in f:
        line = line.strip()
        line = line.split(' ')
        line = [int(item) for item in line]
        if checksafety(line):
            count+=1
        else:
            unsafe.append(line)


for line in unsafe:
    for i in range(len(line)):
        modified = line[:i] + line[i+1:]
        if checksafety(modified):
            print(modified)
            count += 1
            break
print(count)