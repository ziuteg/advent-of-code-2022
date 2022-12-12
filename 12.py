from collections import deque


def bfs(grid, starts, end):
    queue = deque([(0, start) for start in starts])
    visited = set(starts)

    while len(queue) > 0:
        dist, node = queue.popleft()

        if node == end:
            return dist

        for dir in [(1,0), (-1,0), (0, 1), (0, -1)]:
            next = (node[0]+dir[0], node[1]+dir[1])

            if next in visited:
                continue
            if next not in grid:
                continue
            if grid[node] + 1 < grid[next]:
                continue
            
            queue.append((dist+1, next))
            visited.add(next)

    return -1


def execute1(input):
    grid = {}
    starts = []

    for y, line in enumerate(input.splitlines()):
        for x, item in enumerate(line):
            if item == 'S':
                grid[(x, y)] = ord('a')
                starts.append((x, y))
            elif item == 'E':
                end = (x, y)
                grid[(x, y)] = ord('z')
            else:
                grid[(x,y)] = ord(item)

    return bfs(grid, starts, end)


def execute2(input):
    grid = {}
    starts = []

    for y, line in enumerate(input.splitlines()):
        for x, item in enumerate(line):
            if item == 'S' or item == 'a':
                grid[(x, y)] = ord('a')
                starts.append((x, y))
            elif item == 'E':
                end = (x, y)
                grid[(x, y)] = ord('z')
            else:
                grid[(x,y)] = ord(item)

    return bfs(grid, starts, end)
