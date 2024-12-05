matrix = []

with open('data.txt') as f:
    for line in f:
        matrix.append(line.strip())

ymax = len(matrix)
xmax = len(matrix[0])

count = 0

for i in range(ymax):
    for j in range(xmax):
        if matrix[i][j] == 'X':
            # Backwards
            if j >= 3 and matrix[i][j-1] == 'M' and matrix[i][j-2] == 'A' and matrix[i][j-3] == 'S':
                count += 1
            # Diagonal left up
            if i >= 3 and j >= 3 and matrix[i-1][j-1] == 'M' and matrix[i-2][j-2] == 'A' and matrix[i-3][j-3] == 'S':
                count += 1
            # Up
            if i >= 3 and matrix[i-1][j] == 'M' and matrix[i-2][j] == 'A' and matrix[i-3][j] == 'S':
                count += 1
            # Diagonal right up
            if i >= 3 and j <= xmax - 4 and matrix[i-1][j+1] == 'M' and matrix[i-2][j+2] == 'A' and matrix[i-3][j+3] == 'S':
                count += 1
            # Normal
            if j <= xmax - 4 and matrix[i][j+1] == 'M' and matrix[i][j+2] == 'A' and matrix[i][j+3] == 'S':
                count += 1
            # Diagonal right down
            if i <= ymax - 4 and j <= xmax - 4 and matrix[i+1][j+1] == 'M' and matrix[i+2][j+2] == 'A' and matrix[i+3][j+3] == 'S':
                count += 1
            # Down
            if i <= ymax - 4 and matrix[i+1][j] == 'M' and matrix[i+2][j] == 'A' and matrix[i+3][j] == 'S':
                count += 1
            # Diagonal down left
            if i <= ymax - 4 and j >= 3 and matrix[i+1][j-1] == 'M' and matrix[i+2][j-2] == 'A' and matrix[i+3][j-3] == 'S':
                count += 1

print(count)
