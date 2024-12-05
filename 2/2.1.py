count = 0

with open('data.txt')as f:
    for line in f:
        order = False
        check = True
        line = line.strip()
        line = line.split(' ')
        line = [int(item) for item in line]

        ascending = sorted(line)
        descending = sorted(line, reverse=True)
        if line == ascending or line == descending:
            order = True
        else:
            continue
        for i in range(len(line)-1):
            if abs(int(line[i]) - int(line[i+1])) > 3 or line[i] == line[i+1]:
                check = False
        if order and check:
            count += 1
print(count)