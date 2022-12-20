from lib.aoc import nums
import functools
import sys
sys.setrecursionlimit(50000)


def calculate(time, costs):
    limits = []

    def cap(time, robots, counts):
        robots = [min(robots[i], limits[i]) for i in range(4)]
        counts = [
            min(counts[0], time * limits[0] - robots[0] * (time-1)),
            min(counts[1], time * costs[2][1] - robots[1] * (time-1)),
            min(counts[2], time * costs[3][1] - robots[2] * (time-1)),
            counts[3]
        ]
        return time, tuple(robots), tuple(counts)

    def affordable(i, counts):
        if i == 0:
            return counts[0] >= costs[0]
        elif i == 1:
            return counts[0] >= costs[1]
        elif i == 2:
            return counts[0] >= costs[2][0] and counts[1] >= costs[2][1]
        elif i == 3:
            return counts[0] >= costs[3][0] and counts[2] >= costs[3][1]

    def useful(i, robots, counts):
        useful = counts[i] + robots[i] * time < limits[i] * time
        useful &= robots[i] < limits[i]
        return useful

    @functools.cache
    def dfs(time, robots, counts):
        nonlocal limits, costs

        if time == 0:
            return counts[3]

        result = 0

        if affordable(0, counts) and useful(0, robots, counts):
            next_robots, next_counts = list(robots), list(counts)
            next_robots[0] += 1
            next_counts[0] -= costs[0]
            next_counts = [robots[i] + next_counts[i] for i in range(4)]
            result = max(result, dfs(
                *cap(time-1, tuple(next_robots), tuple(next_counts))))

        if affordable(1, counts) and useful(1, robots, counts):
            next_robots, next_counts = list(robots), list(counts)
            next_robots[1] += 1
            next_counts[0] -= costs[1]
            next_counts = [robots[i] + next_counts[i] for i in range(4)]
            result = max(result, dfs(
                *cap(time-1, tuple(next_robots), tuple(next_counts))))

        if affordable(2, counts) and useful(2, robots, counts):
            next_robots, next_counts = list(robots), list(counts)
            next_robots[2] += 1
            next_counts[0] -= costs[2][0]
            next_counts[1] -= costs[2][1]
            next_counts = [robots[i] + next_counts[i] for i in range(4)]
            result = max(result, dfs(
                *cap(time-1, tuple(next_robots), tuple(next_counts))))

        if affordable(3, counts):
            next_robots, next_counts = list(robots), list(counts)
            next_robots[3] += 1
            next_counts[0] -= costs[3][0]
            next_counts[2] -= costs[3][1]
            next_counts = [robots[i] + next_counts[i] for i in range(4)]
            result = max(result, dfs(
                *cap(time-1, tuple(next_robots), tuple(next_counts))))

        next_counts = [min(robots[i] + counts[i], 24) for i in range(4)]

        return max(result, dfs(time - 1, robots, tuple(next_counts)))

    limits = [
        max([costs[0], costs[1], costs[2][0], costs[3][0]]),
        costs[2][1],
        costs[3][1],
        99
    ]

    result = dfs(time, (1, 0, 0, 0), (0, 0, 0, 0))
    dfs.cache_clear()
    return result


def read_input(input):
    blueprints = []
    for line in input.splitlines():
        line = line.split(': ')[1]

        ns = list(nums(line))

        ore = ns[0]
        clay = ns[1]
        obsidian = (ns[2], ns[3])
        geode = (ns[4], ns[5])

        blueprints.append((ore, clay, obsidian, geode))

    return blueprints


def execute1(input):
    blueprints = read_input(input)

    quality = 0
    for i, blueprint in enumerate(blueprints):
        print('Calculating quality for blueprint', i+1)
        quality += (i+1) * calculate(24, blueprint)

    return quality


def execute2(input):
    blueprints = read_input(input)

    result = 1
    for i, blueprint in enumerate(blueprints[:3]):
        result *= calculate(32, blueprint)

    return result
