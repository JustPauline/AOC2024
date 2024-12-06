def move(field, positioni, positionj, direction):
    done = False
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


matrix = []
count = 0

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

for i in range(ymax):
    for j in range(xmax):
        visited = set()
        x, y = start
        obstructed = matrix
        richting = 'UP'
        check = False
        if [i, j] != start and obstructed[i][j] != '#':
            obstructed[i][j] = '#'
            while not check:
                state = (x, y, richting)
                if state in visited:
                    count += 1
                    print(count)
                    break
                else:
                    visited.add(state)
                    obstructed, x, y, richting, check = move(obstructed, x, y, richting)
            obstructed[i][j] = '.'
print(count)