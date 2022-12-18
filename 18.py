import sys
sys.setrecursionlimit(10000)


def neighbours(pos):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if abs(dx) + abs(dy) + abs(dz) != 1:
                    continue
                yield (pos[0] + dx, pos[1] + dy, pos[2] + dz)


def execute1(input):
    cubes = set()

    for line in input.splitlines():
        x, y, z = map(int, line.split(','))
        cubes.add((x, y, z))

    result = 0
    for cube in cubes:
        result += 6
        
        for next_cube in neighbours(cube):
            if next_cube in cubes:
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
    for next_pos in neighbours(pos):
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
