matrix = []
richting = 'UP'
check = False
count = 0

def move(field, positioni, positionj, direction, done):
    field[positioni][positionj] = 'X'
    if direction == 'UP':
        if positioni == 0:
            done = True
        elif field[positioni-1][positionj] == '#':
            direction = "RIGHT"
        else:
            positioni -= 1
    elif direction == 'RIGHT':
        if positionj == xmax-1:
            done = True
        elif field[positioni][positionj+1] == '#':
            direction = "DOWN"
        else:
            positionj += 1
    elif direction == 'DOWN':
        if positioni == ymax-1:
            done = True
        elif field[positioni+1][positionj] == '#':
            direction = "LEFT"
        else:
            positioni += 1
    elif direction == 'LEFT':
        if positionj == 0:
            done = True
        if field[positioni][positionj-1] == '#':
            direction = "UP"
        else:
            positionj -= 1
    return field, positioni, positionj, direction, done


with open('data.txt') as f:
    for line in f:
        line.split()
        matrix.append(list(line.strip()))

ymax = len(matrix)
xmax = len(matrix[0])

for i in range(ymax):
    for j in range(xmax):
        if matrix[i][j] == '^':
            start = [i, j]

i, j = start

while not check:
    matrix, i, j, richting, check = move(matrix, i, j, richting, check)

for i in range(ymax):
    for j in range(xmax):
        if matrix[i][j] == 'X':
            count += 1

print(count)