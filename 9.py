def move_closer(a, b):
    dx = 1 if a[0] < b[0] else 0 if a[0] == b[0] else -1
    dy = 1 if a[1] < b[1] else 0 if a[1] == b[1] else -1

    dist = max(abs(a[0] - b[0]), abs(a[1] - b[1]))

    if dist > 1:
        return (a[0] + dx, a[1] + dy)

    return a


def step(rope, dir):
    nrope = rope.copy()
    head = rope[0]

    nrope[0] = (head[0] + dir[0], head[1] + dir[1])

    for i in range(1, len(rope)):
        head = nrope[i-1]
        tail = rope[i]

        tail = move_closer(tail, head)
        nrope[i] = tail

    return nrope


def solve(input, rope_len):
    rope = [(0, 0) for _ in range(rope_len)]
    T = set({})
    DIRS = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }
    
    for elem in input.splitlines():
        dir, dist = elem.split()
        dist = int(dist)
        dir = DIRS[dir]

        T.add(rope[-1])

        for _ in range(dist):
            rope = step(rope, dir)
            T.add(rope[-1])

    return len(T)


def execute1(input):
    return solve(input, 2)


def execute2(input):
    return solve(input, 10)