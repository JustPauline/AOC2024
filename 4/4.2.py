matrix = []

with open('data.txt') as f:
    for line in f:
        matrix.append(line.strip())

ymax = len(matrix)
xmax = len(matrix[0])

count = 0

for i in range(1, ymax-1):
    for j in range(1, xmax-1):
        if matrix[i][j] == 'A':
            # diagonal left down MAS
            if matrix[i-1][j-1] == "M" and matrix[i+1][j+1] == 'S':
                if matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S':
                    count += 1
                if matrix[i-1][j+1] == 'S' and matrix[i+1][j-1] == 'M':
                    count += 1
            # diagonal right up MAS
            if matrix[i-1][j-1] == "S" and matrix[i+1][j+1] == 'M':
                if matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S':
                    count += 1
                if matrix[i-1][j+1] == 'S' and matrix[i+1][j-1] == 'M':
                    count += 1
print(count)
