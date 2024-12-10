with open('data.txt') as f:
    matrix = [line.strip() for line in f]

ymax, xmax = len(matrix), len(matrix[0])
total = 0

for i in range(ymax):
    for j in range(xmax):
        if int(matrix[i][j]) == 0:
            def count_trails(x, y, value):
                if not (0 <= x < ymax and 0 <= y < xmax):
                    return 0
                if int(matrix[x][y]) != value:
                    return 0
                if value == 9:
                    return 1

                trails = 0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    trails += count_trails(x + dx, y + dy, value + 1)

                return trails

            total += count_trails(i, j, 0)

print(total)
