DIRS = {
    0: [1, 0], 1: [0, 1], 2: [-1, 0], 3: [0, -1]
}

DIR_REVS = {
    0: 2, 1: 3, 2: 0, 3: 1
}

UP = 3
DOWN = 1 
LEFT = 2
RIGHT = 0


def read_input(puzzle_input):
    board_input, steps_input = puzzle_input.split('\n\n')
    board = set()
    walls = set()

    for y, line in enumerate(board_input.splitlines()):
        for x, item in enumerate(line):
            if item == '.' or item == '#':
                board.add((x, y))
            if item == '#':
                walls.add((x, y))

    starts = []
    for y in range(len(board_input.splitlines())):
        for x in range(max(map(len, board_input.splitlines()))):
            if (x, y) not in board:
                continue
            if is_inner_corner((x, y), board):
                starts.append((x, y))

    steps_input = steps_input.replace('R', ' R ')
    steps_input = steps_input.replace('L', ' L ')
    steps_input = steps_input.split(' ')

    return board, walls, starts, steps_input


def is_inner_corner(pos, board):
    empty = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (pos[0]+i, pos[1]+j) not in board:
                empty += 1
    return empty == 1


def is_edge(pos, board):
    empty = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (pos[0]+i, pos[1]+j) not in board:
                empty += 1
    return pos in board and empty >= 2


def is_corner(pos, board):
    return len(edge_dirs(pos, board)) > 1


def edge_dirs(pos, board):
    dirs = []
    if not is_edge(pos, board):
        return dirs
    if (pos[0]+1, pos[1]) not in board:
        dirs.append(0)
    if (pos[0], pos[1]+1) not in board:
        dirs.append(1)
    if (pos[0]-1, pos[1]) not in board:
        dirs.append(2)
    if (pos[0], pos[1]-1) not in board:
        dirs.append(3)
    return dirs


def adjacent_edges(pos, board):
    edges = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 and j != 0:
                continue
            if is_edge((pos[0]+i, pos[1]+j), board):
                edges.append((pos[0]+i, pos[1]+j))
    return edges


def generate_wraps(board):
    wrap = {}
    width = max([x for x, _ in board]) + 1
    height = max([y for _, y in board]) + 1

    for y in range(height):
        left, right = width, -1
        for x in range(width):
            if (x, y) in board:
                left = min(left, x)
                right = max(right, x)
        
        wrap[((left, y), LEFT)] = ((right, y), LEFT)
        wrap[((right, y), RIGHT)] = ((left, y), RIGHT)
    
    for x in range(width):
        top, bottom = height, -1
        for y in range(height):
            if (x, y) in board:
                top = min(top, y)
                bottom = max(bottom, y)

        wrap[((x, top), UP)] = ((x, bottom), UP)
        wrap[((x, bottom), DOWN)] = ((x, top), DOWN)

    return wrap


def generate_cube_wraps(starts, board):
    wraps = {}
    visited_edges = set()
    visited_corners = set()

    queue = []
    for start in starts:
        queue.append([tuple([edge, edge_dirs(edge, board)[0]]) for edge in adjacent_edges(start, board)])

    while len(queue) > 0:
        edges = queue.pop(0)
        assert len(edges) == 2

        a_pos, a_dir = edges[0]
        b_pos, b_dir = edges[1]

        visited_edges.add(a_pos)
        visited_edges.add(b_pos)

        wraps[(a_pos, a_dir)] = (b_pos, DIR_REVS[b_dir])
        wraps[(b_pos, b_dir)] = (a_pos, DIR_REVS[a_dir])

        if is_corner(a_pos, board) and is_corner(b_pos, board):
            continue

        def next_direction(pos, direction):
            nonlocal board
            for other_dir in edge_dirs(pos, board):
                if direction != other_dir:
                    return other_dir

        if is_corner(a_pos, board) and a_pos not in visited_corners:
            visited_corners.add(a_pos)
            for next_b in adjacent_edges(b_pos, board):
                if next_b in visited_edges:
                    continue

                a_dir = next_direction(a_pos, a_dir)
                visited_edges.add(next_b)

                queue.append([tuple([a_pos, a_dir]), tuple([next_b, b_dir])])

            continue

        if is_corner(b_pos, board) and b_pos not in visited_corners:
            visited_corners.add(b_pos)
            for next_a in adjacent_edges(a_pos, board):
                if next_a in visited_edges:
                    continue

                b_dir = next_direction(b_pos, b_dir)
                visited_edges.add(next_a)

                queue.append([tuple([next_a, a_dir]), tuple([b_pos, b_dir])])

            continue

        for next_a in adjacent_edges(a_pos, board):
            for next_b in adjacent_edges(b_pos, board):

                if is_corner(next_a, board) and is_corner(next_b, board):
                    visited_edges.add(next_a)
                    visited_edges.add(next_b)
                    queue.append([tuple([next_a, a_dir]), tuple([next_b, b_dir])])
                    continue

                if next_a in visited_edges:
                    continue
                if next_b in visited_edges:
                    continue

                visited_edges.add(next_a)
                visited_edges.add(next_b)
                queue.append([tuple([next_a, a_dir]), tuple([next_b, b_dir])])

    return wraps


def traverse(command, pos, dir, board, walls, wraps):
    if command == 'R':
        dir = (dir+1) % 4
        return pos, dir
    if command == 'L':
        dir = (dir-1) % 4
        return pos, dir

    for _ in range(int(command)):
        if (pos, dir) in wraps:
            next_pos, next_dir = wraps[(pos, dir)]
            if next_pos in walls:
                continue
            pos = next_pos
            dir = next_dir
            continue
        next_pos = (pos[0] + DIRS[dir][0], pos[1] + DIRS[dir][1])
        if next_pos not in board or next_pos in walls:
            continue
        pos = next_pos

    return pos, dir


def execute1(input):
    board, walls, _, steps = read_input(input)

    wraps = generate_wraps(board)

    pos = (0, 0)
    while pos not in board:
        pos = (pos[0]+1, pos[1])

    dir = 0
    for step in steps:
        pos, dir = traverse(step, pos, dir, board, walls, wraps)

    return (pos[1] + 1) * 1000 + (pos[0] + 1) * 4 + dir


def execute2(puzzle_input):
    board, walls, starts, steps = read_input(puzzle_input)

    wraps = generate_cube_wraps(starts, board)

    pos = (0, 0)
    while pos not in board:
        pos = (pos[0]+1, pos[1])

    dir = 0
    for step in steps:
        pos, dir = traverse(step, pos, dir, board, walls, wraps)

    return (pos[1] + 1) * 1000 + (pos[0] + 1) * 4 + dir
