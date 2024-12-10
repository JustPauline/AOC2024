with open('data.txt') as f:
    matrix = [line.strip() for line in f]

ymax, xmax = len(matrix), len(matrix[0])
total_score = 0

for i in range(ymax):
    for j in range(xmax):
        if int(matrix[i][j]) == 0:
            visited = [[False] * xmax for _ in range(ymax)]

            def checkpaths(x, y, value):
                if not (0 <= x < ymax and 0 <= y < xmax) or visited[x][y] or int(matrix[x][y]) != value:
                    return set()

                visited[x][y] = True
                reachable_nines = set()
                if value == 9:
                    reachable_nines.add((x, y))
                else:
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        reachable_nines.update(checkpaths(x + dx, y + dy, value + 1))

                visited[x][y] = False
                return reachable_nines

            total_score += len(checkpaths(i, j, 0))

print(total_score)
