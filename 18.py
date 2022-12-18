import sys
sys.setrecursionlimit(10000)


def execute1(input):
    cubes = set()

    for line in input.splitlines():
        x, y, z = map(int, line.split(','))
        cubes.add((x, y, z))

    result = 0
    for cube in cubes:
        result += 6
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    if (abs(x) + abs(y) + abs(z)) == 1:
                        if (cube[0] + x, cube[1] + y, cube[2] + z) in cubes:
                            result -= 1

    return result


def dfs(pos, cubes, visited, limit):
    if pos in visited:
        return 0
    if any([pos[i] < -1 or pos[i] >= limit[i] for i in range(len(pos))]):
        return 0
    if pos in cubes:
        return 0

    visited.add(pos)

    result = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                next_pos = (pos[0] + dx, pos[1] + dy, pos[2] + dz)

                if sum([abs(pos[i] - next_pos[i]) for i in range(len(pos))]) != 1:
                    continue

                if next_pos in cubes:
                    result += 1

                result += dfs(next_pos, cubes, visited, limit)

    return result


def execute2(input):
    cubes = set()
    x_max, y_max, z_max = 1, 1, 1

    for line in input.splitlines():
        x, y, z = map(int, line.split(','))
        x_max = max(x_max, x)
        y_max = max(y_max, y)
        z_max = max(z_max, z)
        cubes.add((x, y, z))

    return dfs((-1, -1, -1), cubes, set(), (x_max+2, y_max+2, z_max+2))
