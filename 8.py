def read_input(input):
    lines = list(input.splitlines())
    grid = {}

    for y, line in enumerate(lines):
        for x, item in enumerate(line):
            grid[(x, y)] = int(item)

    return grid


def dirs():
    return [(0, 1), (1, 0), (0, -1), (-1, 0)]


def move(a, b):
    return tuple(sum(t) for t in zip(a, b))


def is_visible(pos, grid):

    for dir in dirs():
        npos = move(pos, dir)

        while True:
            if npos not in grid:
                return 1
            if grid[npos] >= grid[pos]:
                break
            npos = move(npos, dir)

    return 0


def dist(pos, grid):
    result = 1

    for dir in dirs():
        npos = move(pos, dir)
        d = 0

        while npos in grid:
            d += 1
            if grid[npos] >= grid[pos]:
                break
            npos = move(npos, dir)

        result *= d

    return result


def execute1(input):
    grid = read_input(input)

    result = 0
    for pos in grid.keys():
        result += is_visible(pos, grid)

    return result


def execute2(input):
    grid = read_input(input)

    result = 0
    for pos in grid.keys():
        result = max(result, dist(pos, grid))

    return result
