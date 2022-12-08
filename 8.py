def read_input(input):
    lines = list(input.splitlines())
    grid = {}

    for y, line in enumerate(lines):
        for x, item in enumerate(line):
            grid[(x, y)] = int(item)

    return grid


def dirs():
    return [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_visible(x, y, grid):

    for dir in dirs():
        nx, ny = x, y
        nx += dir[0]
        ny += dir[1]

        while (nx, ny) in grid:
            if grid[(nx, ny)] >= grid[(x, y)]:
                break
            nx += dir[0]
            ny += dir[1]

        if (nx, ny) not in grid:
            return 1

    return 0


def dist(x, y, grid):
    result = 1

    for dir in dirs():
        nx, ny = x, y
        nx += dir[0]
        ny += dir[1]
        d = 0

        while (nx, ny) in grid:
            d += 1
            if grid[(nx, ny)] >= grid[(x, y)]:
                break
            nx += dir[0]
            ny += dir[1]
    
        result *= d

    return result


def execute1(input):
    grid = read_input(input)

    result = 0
    for pos in grid.keys():
        result += is_visible(*pos, grid)
    
    return result


def execute2(input):
    grid = read_input(input)

    result = 0
    for pos in grid.keys():
        result = max(result, dist(*pos, grid))
    
    return result
