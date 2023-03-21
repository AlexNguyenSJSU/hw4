def cacti_number(grid):
    result = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):

            if grid[i][j] == 0:
                check = True

                if i > 0 and grid[i - 1][j] == 1:
                    check = False
                if j > 0 and grid[i][j - 1] == 1:
                    check = False
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    check = False
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                    check = False
                if i < len(grid) - 1 and grid[i + 1][j] ==1:
                    check = False
                if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
                    check = False

                if check:
                    result += 1
                    grid[i][j] = 1

    return result
