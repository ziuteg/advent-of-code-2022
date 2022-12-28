from collections import deque


DIRECTIONS = {
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0),
    '>': (1, 0),
}

MOVES = {
    (0, 0),
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
}


def move_blizzards(blizzards, limits):
    new_blizzards = set()
    for pos, dir in blizzards:
        new_position = (pos[0] + dir[0], pos[1] + dir[1])
        if new_position[0] < 1:
            new_position = (limits[0] - 2, pos[1])
        if new_position[0] >= limits[0] - 1:
            new_position = (1, pos[1])
        if new_position[1] < 1:
            new_position = (pos[0], limits[1] - 2)
        if new_position[1] >= limits[1] - 1:
            new_position = (pos[0], 1)
        new_blizzards.add((new_position, dir))
    return new_blizzards


def get_blizzard_positions(blizzards):
    return set([pos for pos, _ in blizzards])


def read_input(input):
    grid = set()
    blizzards = set()
    width = len(input.splitlines()[0])
    height = len(input.splitlines())
    start = (1, 0)
    end = (width - 2, height - 1)

    for y, line in enumerate(input.splitlines()):
        for x, item in enumerate(line):
            if item == '#':
                continue
            grid.add((x, y))
            if item != '.':
                blizzards.add(((x, y), DIRECTIONS[item]))

    return grid, blizzards, start, end, (width, height)


def bfs(grid, blizzards, start, targets, limits):
    blizzards = move_blizzards(blizzards, limits)
    blizzard_positions = get_blizzard_positions(blizzards)
    blizzard_step = 0

    queue = deque([(start, blizzard_step)])
    visited = set()

    while len(queue) > 0:
        pos, step = queue.popleft()
        if pos == targets[-1]:
            queue.clear()
            visited.clear()
            targets.pop()
            result = step
            if len(targets) == 0:
                break

        if step > blizzard_step:
            blizzards = move_blizzards(blizzards, limits)
            blizzard_positions = get_blizzard_positions(blizzards)
            blizzard_step = step

        for move in MOVES:
            next_pos = (pos[0] + move[0], pos[1] + move[1])
            state = (next_pos, step + 1)
            if next_pos not in grid:
                continue
            if state in visited:
                continue
            if next_pos in blizzard_positions:
                continue
            queue.append(state)
            visited.add(state)

    return result


def execute1(input):
    grid, blizzards, start, end, limits = read_input(input)
    return bfs(grid, blizzards, start, [end], limits)


def execute2(input):
    grid, blizzards, start, end, limits = read_input(input)
    return bfs(grid, blizzards, start, [end, start, end], limits)
