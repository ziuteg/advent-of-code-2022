def read_input(input):
    stone = set()
    sand = set()
    limit = -9999999

    for line in input.splitlines():
        px, py = None, None

        for item in line.split(' -> '):
            x, y = map(int, item.split(','))
            limit = max(limit, y)

            if px is not None:
                if x == px:
                    for dy in range(min(py, y), max(py, y)+1):
                        stone.add((x, dy))
                elif y == py:
                    for dx in range(min(px, x), max(px, x)+1):
                        stone.add((dx, y))
                        
            px, py = x, y

    return stone, sand, limit


def simulate_sand(stone, sand, x, y, limit):
    if y > limit:
        raise Exception('limit exceeded')

    if (x, y) in sand:
        return False
    if (x, y) in stone:
        return False

    if simulate_sand(stone, sand, x, y+1, limit):
        return True
    if simulate_sand(stone, sand, x-1, y+1, limit):
        return True
    if simulate_sand(stone, sand, x+1, y+1, limit):
        return True

    sand.add((x, y))
    return True


def execute1(input):
    stone, sand, limit = read_input(input)

    initial_pos = (500, 0)

    while True:
        try:
            simulate_sand(stone, sand, *initial_pos, limit)
        except Exception as e:
            break

    return len(sand)


def execute2(input):
    stone, sand, limit = read_input(input)
    limit += 2

    for x in range(-99999, 99999):
        stone.add((x, limit))

    initial_pos = (500, 0)

    while True:
        simulate_sand(stone, sand, *initial_pos, limit)
        if initial_pos in sand:
            break

    return len(sand)
