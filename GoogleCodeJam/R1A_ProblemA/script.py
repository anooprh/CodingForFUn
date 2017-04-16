import sys

FILENAME = sys.argv[1]
# FILENAME = "sample_input.txt"

file = open(FILENAME)

T = int(file.readline().strip())

for i in range(T):
    line = file.readline().strip()
    R, C = map(int, line.split(' '))

    grid = []
    ig = {}
    firstRow = None
    for j in range(R):
        row = []
        line = file.readline().strip()
        for k in range(C):
            row.append(line[k])
            if line[k] != '?' and firstRow is None:
                firstRow = j

            # if line[k] == '?': continue
            #
            # if line[k] in ig:
            #     ig[line[k]].add((j, k))
            # else:
            #     ig[line[k]] = {(j, k)}
        grid.append(row)

    # for char in ig:
    #     indices = ig[char]
    #     topRow = R
    #     bottomRow = -1
    #     leftCol = C
    #     rightCol = -1
    #     for (r, c) in indices:
    #         topRow = min(topRow, r)
    #         bottomRow = max(bottomRow, r)
    #         leftCol = min(leftCol, c)
    #         rightCol = max(rightCol, r)
    #         for j in range(topRow, bottomRow + 1):
    #             for k in range(leftCol, rightCol + 1):
    #                 grid[i][j] = char

    for j in range(firstRow):
        grid[j] = grid[firstRow]

    for j in range(R):
        last = None
        first = None
        for k in range(C):
            if grid[j][k] == '?':
                if last is not None:
                    grid[j][k] = last
            else:
                if first is None:
                    first = k
                    for l in range(first):
                        grid[j][l] = grid[j][k]
                last = grid[j][k]
        if last is None:
            grid[j] = grid[j-1]

    ans = 0
    print "Case #" + str(i + 1) + ": "
    for j in range(R):
        print ''.join(grid[j])
