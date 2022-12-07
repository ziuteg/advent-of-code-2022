from collections import defaultdict


def read_input(input):
    fs = defaultdict(int, {})
    paths = defaultdict(list, {})
    current_dir = []

    for line in input.splitlines():
        cmd = list(line.split())
        if cmd[0] == '$':
            if cmd[1] == 'cd':
                if cmd[2] == '..':
                    current_dir.pop()
                else:
                    k = '/' + '/'.join(current_dir[1:])
                    current_dir.append(cmd[2])
                    v = '/' + '/'.join(current_dir[1:])
                    if v != '/':
                        paths[k].append(v)
        elif cmd[0] != 'dir':
            fs['/' + '/'.join(current_dir[1:])] += int(cmd[0])

    return fs, paths


def dfs(dir, fs, paths, sizes):
    size = 0

    for subdir in paths[dir]:
        size += dfs(subdir, fs, paths, sizes)

    size += fs[dir]
    sizes.append(size)

    return size


def execute1(input):
    fs, paths = read_input(input)

    sizes = []
    dfs('/', fs, paths, sizes)

    return sum(filter(lambda x: x < 100000, sizes))


def execute2(input):
    fs, paths = read_input(input)

    sizes = []
    total = dfs('/', fs, paths, sizes)

    free = 70000000 - total
    target = 30000000

    result = 70000000
    for size in sizes:
        if size + free > target:
            result = min(result, size)

    return result
