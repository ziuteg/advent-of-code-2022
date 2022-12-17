
ROCKS = [[
        '####'
    ], [
        '.#.',
        '###',
        '.#.'
    ], [
        '..#',
        '..#',
        '###'
    ], [
        '#',
        '#',
        '#',
        '#'
    ], [
        '##',
        '##'
    ]
]

WIDTHS = [4, 3, 3, 1, 2]


def collision(rock, pos, rocks):
    if pos[1] - len(rock) + 1 < 0:
        return True
    for y, line in enumerate(rock):
        for x, c in enumerate(line):
            if c == '#':
                if (pos[0] + x, pos[1] - y) in rocks:
                    return True
    return False


def add_rock(rock, pos, rocks):
    top = 0
    for y, line in enumerate(rock):
        for x, c in enumerate(line):
            if c == '#':
                rocks.add((pos[0] + x, pos[1] - y))
                top = max(top, pos[1] - y)
    return top


def simulate(jet_pattern, turns):
    rock_index = 0
    jet_index = 0
    initial_pos=(2,3)
    top = 0
    rocks = set()
    WIDTH = 7

    diffs = []
    history = []

    for i in range(turns):
        prev_top = top
        rock = ROCKS[rock_index]
        width = WIDTHS[rock_index]

        pos = initial_pos
        pos = (pos[0], pos[1] + len(rock) - 1)

        while True:
            prev_pos = pos
            side = jet_pattern[jet_index]

            if side == '>' and pos[0] + width < WIDTH:
                pos = (pos[0] + 1, pos[1])
            elif side == '<' and pos[0] > 0:
                pos = (pos[0] - 1, pos[1])

            jet_index = (jet_index + 1) % len(jet_pattern)

            if collision(rock, pos, rocks):
                pos = prev_pos

            prev_pos = pos
            pos = (pos[0], pos[1] - 1)

            if collision(rock, pos, rocks):
                top = max(top, add_rock(rock, prev_pos, rocks))
                break

        diffs.append(top - prev_top)
        history.append(top)

        initial_pos = (initial_pos[0], top+3 + 1)
        rock_index = (rock_index + 1) % len(ROCKS)

    return history, diffs


def execute1(input):
    history, _ = simulate(input, 2022)
    return history[-1]+1


def execute2(input):
    history, diffs = simulate(input, 2022*10)

    # Take an arbitrary offset and pattern length and find cycle.
    offset_idx = 500
    pattern_len = 100
    repeat_idx = 0

    for i in range(offset_idx+1, len(diffs) - pattern_len):
        if diffs[i:i+pattern_len] == diffs[offset_idx:offset_idx+pattern_len]:
            repeat_idx = i
            break

    TARGET = 1000000000000
    
    step_len = repeat_idx - offset_idx
    step_sum = sum(diffs[offset_idx:repeat_idx])
    num_steps = (TARGET - offset_idx) // step_len
    rest_len = (TARGET - offset_idx) % step_len
    
    result = history[offset_idx] + num_steps * step_sum
    result += sum(diffs[offset_idx:offset_idx+rest_len])
    
    return result
