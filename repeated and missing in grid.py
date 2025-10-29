def findMissingAndRepeatedValues(grid):
    n = len(grid)
    dici = {}
    for i in range(n):
        for j in range(len(grid[0])):
            val = grid[i][j]
            if val not in dici:
                dici[val] = 1
            else:
                dici[val] += 1
    a = []
    for key in dici:
        if dici[key] > 1:
            a.append(key)
            break
    for i in range(1, n * n + 1):
        if i not in dici:
            a.append(i)
            break

    return a
grid = [[1, 3], [2, 2]]
print(findMissingAndRepeatedValues(grid))
