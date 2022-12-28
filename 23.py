from collections import defaultdict


N = [(1, -1), (0, -1), (-1, -1)]
S = [(1, 1), (0, 1), (-1, 1)]
W = [(-1, 0), (-1, -1), (-1, 1)]
E = [(1, 0), (1, -1), (1, 1)]

DIRECTIONS = {
    0: N,
    1: S,
    2: W,
    3: E,
}

STEPS = {
    0: (0, -1),
    1: (0, 1),
    2: (-1, 0),
    3: (1, 0),
}


def should_move(pos, positions):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if (pos[0] + dx, pos[1] + dy) in positions:
                return True
    return False


def conflict(pos, positions, s):
    for dir in DIRECTIONS[s]:
        if (pos[0] + dir[0], pos[1] + dir[1]) in positions:
            return True
    return False


def propose_move(pos, positions, round):
    if not should_move(pos, positions):
        return None

    for i in range(4):
        s = (round + i) % 4

        if conflict(pos, positions, s):
            continue

        step = STEPS[s]
        return (pos[0] + step[0], pos[1] + step[1])

    return None


def make_move(pos, moves, proposals):
    if pos not in moves:
        return pos

    next_pos = moves[pos]
    if proposals[next_pos] != 1:
        return pos

    return next_pos


def simulate(positions, round):
    proposals = defaultdict(int)
    next_positions = set()
    moves = {}

    for pos in positions:
        if proposal := propose_move(pos, positions, round):
            proposals[proposal] += 1
            moves[pos] = proposal

    for pos in positions:
       move = make_move(pos, moves, proposals)
       next_positions.add(move)

    positions = next_positions

    return positions, len(moves) > 0


def read_input(input):
    positions = set()
    for y, line in enumerate(input.splitlines()):
        for x, item in enumerate(line):
            if item == '#':
                positions.add((x, y))
    return positions


def execute1(input):
    positions = read_input(input)

    for round in range(10):
        positions, _ = simulate(positions, round)

    x_min = min([x for x, _ in positions])
    x_max = max([x for x, _ in positions])
    y_min = min([y for _, y in positions])
    y_max = max([y for _, y in positions])
    return (x_max - x_min + 1) * (y_max - y_min + 1) - len(positions)


def execute2(input):
    positions = read_input(input)

    for round in range(10000):
        positions, moved = simulate(positions, round)
        if not moved:
            return round + 1
